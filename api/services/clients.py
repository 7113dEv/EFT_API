from pydantic import ValidationError
import requests
from api import settings
from api.constants import API_QUERIES_FILE_PATH, ITEM_QUERY_NAME
from api.data.serializers import IconSerializer, ItemSerializer, ItemMarketDataSerializer
from api.graphql.helpers import load_query
from api.redis.clients import RedisClient
from api.redis.helpers import add_to_redis

class BaseAPIClient():
    def __init__(self, retry: int = 0):
        self.retry = retry

    def post(self, request_query: str, variables: dict = None):
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(settings.TARKOV_DEV_API_URL, headers=headers, json={"query": request_query, "variables": variables})
            response.raise_for_status()
        except requests.exceptions.HTTPError as req_err:
             print(f"Request exception occurred. Error: {req_err.response}. Args: {req_err.args}")
        # TODO: Exponential backoff strat

        return response.json()


class ItemClient(BaseAPIClient):
    def __init__(self, retry: int = 0):
        super().__init__(retry)

    def get_items(self):
        all_items = []

        try:
            redis_client = RedisClient()
            query = load_query(API_QUERIES_FILE_PATH, ITEM_QUERY_NAME)
            response = self.post(query)

            response_data = response["data"]
            for raw_item in response_data["items"]:
                try:
                    icon_data = {
                        "background_color": raw_item["backgroundColor"],
                        "icon_link": raw_item["iconLink"],
                        "grid_image_link": raw_item["gridImageLink"],
                        "base_image_link": raw_item["baseImageLink"],
                        "inspect_image_link": raw_item["inspectImageLink"],
                        "image_512_px_link": raw_item["image512pxLink"],
                        "image_8x_link": raw_item["image8xLink"],
                    }

                    market_data = {
                        "avg_24h_price": raw_item["avg24hPrice"],
                        "last_low_price": raw_item["lastLowPrice"],
                        "change_last_48h": raw_item["changeLast48h"],
                        "change_last_48th_percent": raw_item["changeLast48hPercent"],
                        "low_24h_price": raw_item["low24hPrice"],
                        "high_24h_price": raw_item["high24hPrice"],
                        "last_offer_count": raw_item["lastOfferCount"],
                    }

                    item_data = {
                        "bsgid": raw_item["id"],
                        "name": raw_item["name"],
                        "normalized_name": raw_item["normalizedName"],
                        "base_price": raw_item["basePrice"],
                        "width": raw_item["width"],
                        "height": raw_item["height"],
                        "wiki_link": raw_item["wikiLink"],
                        "types": raw_item["types"],
                        "image_data": icon_data,
                        "market_data": market_data,
                    }

                    # Serialize / validate data before moving on
                    item = ItemSerializer(**item_data)
                    item_n_name = item.normalized_name

                    # TODO: Move to periodic celery task
                    if not redis_client.key_exists(item_n_name):
                        add_to_redis(item_n_name, item, redis_client=redis_client)
                    
                except ValidationError as ve:
                    raise ve
                except Exception as e:
                    raise e       
        except Exception as e:
            print(f"Exception during get items request: {e}")

        return all_items
