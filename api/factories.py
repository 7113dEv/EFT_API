from api.data.models import Item
import random
import uuid

class ItemFactory():
    
    @staticmethod
    def create_iten(self, id: int = None, request_id: str = None, name: str = None) -> Item:
        return Item(
            id=random.randrange(1, 99999), 
            request_id=str(uuid.uuid4),
            name="Test Item"
        )
    