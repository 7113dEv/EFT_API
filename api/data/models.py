from api.extensions import db

class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    bsgid = db.Column(db.String(36), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=True)
    normalized_name = db.Column(db.String(255), nullable=True)
    base_price = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    wiki_link = db.Column(db.String(512), nullable=True)
    types = db.Column(db.JSON, nullable=False)  
    market_data = db.relationship("market_data", back_populates="item", cascade="all, delete-orphan")
    icon_data = db.relationship("icon_data", back_populates="item", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "bsgid": self.bsgid,
            "name": self.name,
            "normalized_name": self.normalized_name,
            "types": self.types,
            "basePrice": self.base_price,
            "width": self.width,
            "height": self.height,
            "market_data": self.market_data.to_dict(),
            "icon_data": self.icon_data.to_dict()
        }
    
class MarketData(db.Model):
    __tablename__ = "market_data"

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    item = db.relationship("item", back_populates="market_data")
    avg_24h_price = db.Column(db.Integer, nullable=True)
    last_low_price = db.Column(db.Integer, nullable=True)
    change_last_48h = db.Column(db.Float, nullable=True)
    change_last_48th_percent = db.Column(db.Float, nullable=True)
    low_24h_price = db.Column(db.Integer, nullable=True)
    high_24h_price = db.Column(db.Integer, nullable=True)
    last_offer_count = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            "avg_24h_price": self.avg_24h_price,
            "last_low_price": self.last_low_price,
            "change_last_48h": self.change_last_48h,
            "change_last_48th_percent": self.change_last_48th_percent,
            "low_24h_price": self.low_24h_price,
            "high_24h_price": self.high_24h_price,
            "last_offer_count": self.last_offer_count,
        }
    
class IconData(db.Model):
    __tablename__ = "icon_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.relationship("Item", back_populates="icon_data")
    background_color = db.Column(db.String(32),  nullable=True)
    icon_link = db.Column(db.String(512), nullable=True)
    grid_image_link = db.Column(db.String(512), nullable=True)
    base_image_link = db.Column(db.String(512), nullable=True)
    inspect_image_link = db.Column(db.String(512), nullable=True)
    image_512_px_link = db.Column(db.String(512), nullable=True)
    image_8x_link = db.Column(db.String(512), nullable=True)
    
    def to_dict(self):
        return {
            "background_color":   self.background_color,
            "icon_link":          self.icon_link,
            "grid_image_link":    self.grid_image_link,
            "base_image_link":    self.base_image_link,
            "inspect_image_link": self.inspect_image_link,
            "image_512_px_link":  self.image_512_px_link,
            "image_8x_link":      self.image_8x_link,
        }
