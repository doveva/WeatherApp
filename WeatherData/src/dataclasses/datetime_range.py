from pydantic import BaseModel, root_validator, ValidationError
from datetime import date


class DateRange(BaseModel):
    start_date: date
    end_date: date

    @root_validator()
    def validate_dates(cls, field_values):
        if field_values['start_date'] < field_values['end_date']:
            raise ValidationError("Start date is smaller than end date")
        return field_values
