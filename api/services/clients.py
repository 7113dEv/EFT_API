import requests

from api import settings
from api.graphql.helpers import load_query



class BaseClient():
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


class ItemClient(BaseClient):
    def __init__(self, retry: int = 0):
        super().__init__(retry)

    def get_items(self):
        query = load_query("api/graphql/api_queries.gql", "GetItems")
        response = self.post(query)

        print(response)
