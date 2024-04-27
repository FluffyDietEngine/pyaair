
from datetime import datetime
from pydantic import BaseModel, Field

class AirportInformation(BaseModel):
    airport: str = Field(alias="Airport Name", description="Name of the airport", examples=["Albuquerque International Sunport"])
    city_name: str = Field(alias="City Name", description="City of the airport",examples=["Albuquerque, NM"])
    city_code: str = Field(alias="City Code", description="Short code for city name", examples=["ABQ"], max_length=3)
    state_code: str = Field(alias="State code", description="Short code for state name", examples=["NM"], max_length=2)
    country_code: str = Field(alias="Country code", description="Short code for country name", examples=["US"], max_length=2)
    domestic: bool = Field(alias="Domestic Airport", description="Is the airport domestic or foreign, with regards to US", default=True)

class SearchInformation(BaseModel):
    search_origin:AirportInformation = Field(description="Origination airport details")
    search_destination: AirportInformation = Field(description="Destination airport details")
    from_date: datetime = Field(alias="Trip date from")
    to_date: datetime | None = Field(alias="Trip date end")
    trip_type: str

class FlightsInformation(BaseModel):
    ...    