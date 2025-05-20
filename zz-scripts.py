# Write scrips here
from api import create_app
from api.services.clients import ItemClient

app = create_app()
with app.app_context():
    client = ItemClient()
    client.get_items(cache_data=False, save_data=True)

    # from api.redis.clients import RedisClient
    # r_c = RedisClient()
    # data = {}

    # print("Getting keys...")
    # for key in r_c._redis.scan_iter():
    #     value = r_c._redis.get(key)
    #     data[key] = value

    # print(data)

