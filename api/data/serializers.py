from typing import List
from pydantic import BaseModel, Field, ValidationError

class IconSerializer(BaseModel):
    backgroundColor: str
    iconLink: str
    gridImageLink: str
    baseImageLink: str
    inspectImageLink: str
    image512pxLink: str
    image8xLink: str


class ItemSerializer(BaseModel):
    uid: str
    name: str
    basePrice: str
    width: int
    height: int
    imageData: IconSerializer
    wikiLink: str
    types: List[str]
    # This is in the API but I can't find an example for now
    # properties: ItemProperties
    

class ItemMarketDataSerializer(BaseModel):
    avg24hPrice: int
    lastLowPrice: int
    changeLast48h: float
    changeLast48thPercent: float
    low24hPrice: int
    high24hPrice: int
    lastOfferCount: int
    