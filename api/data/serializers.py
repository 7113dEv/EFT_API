from typing import List
from pydantic import BaseModel, HttpUrl, field_validator

class IconSerializer(BaseModel):
    background_color: str
    icon_link: HttpUrl
    grid_image_link: HttpUrl
    base_image_link: HttpUrl
    inspect_image_link: HttpUrl
    image_512_px_link: HttpUrl
    image_8x_link: HttpUrl

    @field_validator("background_color", mode="before")
    def validate_background_color(self, v):
        # Add validation logic here
        return v

    @field_validator(
            "icon_link", 
            "grid_image_link", 
            "base_image_link", 
            "inspect_image_link", 
            "image_512_px_link", 
            "image_8x_link", 
            mode="before"
        )
    def validate_urls(self, v):
        # Add validation logic for URLs here
        return v

class ItemMarketDataSerializer(BaseModel):
    avg_24h_price: int
    last_low_price: int
    change_last_48h: float
    change_last_48th_percent: float
    low_24h_price: int
    high_24h_price: int
    last_offer_count: int

    @field_validator("avg_24h_price", "last_low_price", "low_24h_price", "high_24h_price", "last_offer_count", mode="before")
    def validate_prices(self, v):
        # Example: ensure prices are not negative
        return v

    @field_validator("change_last_48h", "change_last_48th_percent", mode="before")
    def validate_changes(self, v):
        # Add float value validations if needed
        return v

class ItemSerializer(BaseModel):
    uid: str
    name: str
    base_price: str
    width: int
    height: int
    image_data: IconSerializer
    wiki_link: str
    types: List[str]
    market_data: ItemMarketDataSerializer
    image_data: IconSerializer

    @field_validator("uid", mode="before")
    def validate_uid(cls, v):
        # Check UUID format or custom ID pattern
        return v

    @field_validator("name", mode="before")
    def validate_name(cls, v):
        # Strip and check for length or invalid chars
        return v

    @field_validator("base_price", mode="before")
    def validate_base_price(cls, v):
        # Example: make sure it's numeric string
        return v

    @field_validator("width", "height", mode="before")
    def validate_dimensions(cls, v):
        # Ensure dimensions are positive
        return v

    @field_validator("wiki_link", mode="before")
    def validate_wiki_link(cls, v):
        # Optional: validate URL format if not using HttpUrl
        return v

    @field_validator("types", mode="before")
    def validate_types(cls, v):
        # Ensure list is not empty, all items are strings
        return v
    