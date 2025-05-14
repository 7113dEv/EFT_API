# Write scrips here
from api.services.clients import ItemClient

client = ItemClient()

test = client.get_items()

from api.redis.clients import RedisClient
r_c = RedisClient()
