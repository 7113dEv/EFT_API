from typing import List, Optional
from pydantic import BaseModel, HttpUrl, ValidationError, field_validator

from api.data.validation_helpers import (
    is_negative, 
    validate_asset_url_string, 
    validate_name_string, 
    validate_uid_string, 
    validate_wiki_url_string
    )

class BaseSerializer:
    # class Config:
    #     orm_mode = True

    model_config = {
      "from_attributes": True,
      "json_encoders": { HttpUrl: lambda u: str(u) }
    }

class IconSerializer(BaseModel, BaseSerializer):
    background_color: Optional[str] = None
    icon_link: Optional[HttpUrl] = None
    grid_image_link: Optional[HttpUrl] = None
    base_image_link: Optional[HttpUrl] = None
    inspect_image_link: Optional[HttpUrl] = None
    image_512_px_link: Optional[HttpUrl] = None
    image_8x_link: Optional[HttpUrl] = None


    @field_validator("background_color", mode="before")
    def validate_background_color(cls, field_value):
        if field_value:
            valid_string = validate_name_string(field_value)
            if not valid_string:
                # raise ValueError(f"String {field_value} does not match regex pattern.")
                return None
        
        return field_value

    @field_validator(
            "icon_link", 
            "grid_image_link", 
            "base_image_link", 
            "inspect_image_link", 
            "image_512_px_link", 
            "image_8x_link", 
            mode="before"
        )
    def validate_urls(cls, field_value):
        if field_value:
            valid_string = validate_asset_url_string(field_value)
            if not valid_string:
                # raise ValueError(f"{field_value} does not match regex pattern.")
                return None
        
        return field_value

class ItemMarketDataSerializer(BaseModel, BaseSerializer):
    avg_24h_price: Optional[int] = None
    last_low_price: Optional[int] = None
    change_last_48h: Optional[float] = None
    change_last_48th_percent: Optional[float] = None
    low_24h_price: Optional[int] = None
    high_24h_price: Optional[int] = None
    last_offer_count: Optional[int] = None

    @field_validator(
            "avg_24h_price", 
            "last_low_price",
            "low_24h_price", 
            "high_24h_price", 
            "last_offer_count", 
            mode="before"
        )
    def validate_prices(cls, field_value):
        if field_value:
            if is_negative(field_value):
                # raise ValueError(f"Improper number value used: {field_value}.")
                return None
        
        return field_value
    
    @field_validator("change_last_48th_percent", mode="after")
    def ensure_two_decimals(cls, field_value):
        rounded_value = round(field_value, 2) if field_value else None

        return rounded_value

class ItemSerializer(BaseModel, BaseSerializer):
    bsgid: Optional[str] = None
    name: Optional[str] = None
    normalized_name: Optional[str] = None
    base_price: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    wiki_link: Optional[str] = None
    types: Optional[List[str]] = None
    market_data: ItemMarketDataSerializer
    image_data: IconSerializer

    @field_validator("uid", mode="before")
    def validate_uid(cls, field_value):
        if field_value:
            valid_string = validate_uid_string(field_value)
            if not valid_string:
                # raise ValueError(f"{field_value} does not match regex pattern.")
                return None
        
        return field_value
    
    @field_validator("name", "normalized_name", mode="before")
    def validate_name(cls, field_value):
        if field_value:
            valid_string = validate_name_string(field_value)
            if not valid_string:
                # raise ValueError(f"String {field_value} does not match regex pattern.")
                return None
        
        return field_value
    
    @field_validator("normalized_name", mode="after")
    def tranform_string(cls, field_value):
        transformed_str = field_value.replace("-", "_") if field_value else None

        return transformed_str

    @field_validator("base_price", mode="before")
    def validate_base_price(cls, field_value):
        if field_value:
            if is_negative(field_value):
                # raise ValueError(f"Improper number value used: {field_value}.")
                return None
        
        return field_value

    @field_validator("width", "height", mode="before")
    def validate_dimensions(cls, field_value):
        if field_value:
            if is_negative(field_value):
                # raise ValueError(f"Improper number value used: {field_value}.")
                return None
        
        return field_value

    @field_validator("wiki_link", mode="before")
    def validate_wiki_link(cls, field_value):
        if field_value:
            valid_string = validate_wiki_url_string(field_value)
            if not valid_string:
                # raise ValueError(f"{field_value} does not match regex pattern.")
                return None
                
        
        return field_value

    @field_validator("types", mode="before")
    def validate_types(cls, field_value):
        if field_value:
            if len(field_value) < 1:
                # raise ValueError(f"Item types are not a list or the list is empty.")
                return None
            
        return field_value
    