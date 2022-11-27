from pydantic import BaseModel, validator, ValidationError


class Place(BaseModel):
    name: str
    longitude: float
    latitude: float

    @validator('longitude', 'latitude')
    def longitude_validation(cls, v):
        if -90 <= v <= 90:
            return v
        raise ValidationError('Value should be between -90 and 90 range')
