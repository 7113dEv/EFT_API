# import app

from api.services.clients import ItemClient


def test():
    # with app.app_context:
    client = ItemClient()

    response = client.get_items()
    print(response)

test()