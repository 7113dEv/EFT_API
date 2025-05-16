# Write scrips here
from api.services.clients import ItemClient

client = ItemClient()
client.get_items()

from api.redis.clients import RedisClient
r_c = RedisClient()
test = r_c.get_value("pile_of_meds")
print(test)