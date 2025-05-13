# Write scrips here
from api.services.clients import ItemClient

client = ItemClient()

test = client.get_items()
print(test)