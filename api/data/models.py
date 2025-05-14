from api.extensions import db

# TODO: Update Item object to reflect API data
class Item(db.Model):
    """
    Item Object:
    
    {
        itemsByName(name: "colt m4a1") {
            name
            types
            avg24hPrice
            basePrice
            width
            height
            changeLast48hPercent
            iconLink
            link
            sellFor {
            price
            source
            }
        }
    }
    """

    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    types =  db.Column()
    avg24hPrice =  db.Column()
    basePrice =  db.Column()
    width = db.Column()
    height = db.Column()
    changeLast48hPercent = db.Column()
    iconLink = db.Column()
    link = db.Column()
    sellFor_price = db.Column()
    sellFor_source = db.Column() 
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    
