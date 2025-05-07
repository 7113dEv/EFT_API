from abc import ABC
from api import db

class Item():
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_id = db.Column(db.String(255))
    name = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    