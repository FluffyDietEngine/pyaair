
from datetime import date, datetime
from enum import StrEnum
from typing import Union, List

from pydantic import BaseModel, Field, ConfigDict

class TripTypes(StrEnum):
    ROUND_TRIP = "Round Trip"
    ONE_WAY_TRIP = "One way Trip"

class TicketClass(StrEnum):
    BASIC_ECONOMY = "Basic Economy class"
    COACH = "Coach class" 
    COACH_FLEXIBLE = "Coach - Flexible class" 
    BUSINESS = "Business class" 
    BUSINESS_FLEXIBLE = "Business - Flexible class" 
    FIRST = "First class" 
    FIRST_FLEXIBLE= "First - Flexible class" 

class PricingGroup(StrEnum):
    MAIN = "Main"
    PREMIUM = "Premium"

class AirportInformation(BaseModel):
    airport: str = Field(serialization_alias="Airport Name", description="Name of the airport", examples=["Albuquerque International Sunport"])
    city_name: str = Field(serialization_alias="City Name", description="City of the airport",examples=["Albuquerque, NM"])
    city_code: str = Field(serialization_alias="City Code", description="Short code for city name", examples=["ABQ"], max_length=3)
    state_code: str = Field(serialization_alias="State code", description="Short code for state name", examples=["NM"], max_length=2)
    country_code: str = Field(serialization_alias="Country code", description="Short code for country name", examples=["US"], max_length=2)
    domestic: bool = Field(serialization_alias="Domestic Airport", description="Is the airport domestic or foreign, with regards to US", default=True)

class SearchMeta(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    search_origin:AirportInformation = Field(description="Origination airport details")
    search_destination: AirportInformation = Field(description="Destination airport details")
    from_date: datetime = Field(serialization_alias="Trip date from")
    to_date: datetime | None = Field(serialization_alias="Trip date end", default=None)
    trip_type: TripTypes = Field(default=TripTypes.ONE_WAY_TRIP.value)

class Flight(BaseModel):
    flight_name: str = Field(description="Flight name", examples=["AA1126"])
    aircraft_type: str = Field(description="Type of the airplane", examples=["Airbus A321"])
    airlines: str = Field(description='Airlines operation', examples=["Americal Airlines"])
    departure: AirportInformation = Field(description="Flight departure airport")
    departure_date: date = Field(description="Departure date of the flight")
    departure_time: datetime = Field(description="Departure time of the flight")
    destination: AirportInformation = Field(description="Flight destination airport")
    arrival_date: date = Field(description="Arrival date of the flight")
    arrival_time: datetime = Field(description="Arrival time of the flight")


class PricingData(BaseModel):
    price: float = Field(alias="Ticket fare from regular pricing", examples=[55.33, 234.12])
    currency: str = Field(alias="Currency of the the price", examples=["USD", "INR"], max_length=3, min_length=3)
    ticket_class: TicketClass = Field(description="Type of pricing class")
    pricing_category: str = Field(description="Category")

class FlightResult(BaseModel):
    flights: Union[Flight, List[Flight]] = Field(description="Information of flight(s)")
    connecting_flight: bool = Field(description="Direct flight or connecting flight", default=False)
    price_data: List[PricingData] = Field(description="List of ticket pricing with seat class")
    cheapest_price: str = Field(alias="Cheapest price", description="Price of cheapest option with currency", examples=["USD 554.33"])
    flight_duration: float = Field(description="Flying duration from origin to arrival")
    
class SearchResults(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    search_information: SearchMeta = Field(description="Meta data of airline search")
    search_results: Union[List[FlightResult], None]
