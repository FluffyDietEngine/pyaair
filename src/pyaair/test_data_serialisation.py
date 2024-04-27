from datetime import datetime
from json import load

from data_model import ( #type: ignore
    AirportInformation,
    SearchMeta, Flight,
    PricingData, FlightResult,
    SearchResults, TripTypes
) 


data = None

with open("aa_data.json", "r") as _file:
    data = load(_file)

search_meta_json_data = data.get("responseMetadata")

search_meta_data = SearchMeta(
    search_origin=AirportInformation(
        airport=search_meta_json_data.get("origin").get("name"),
        city_name=search_meta_json_data.get("origin").get("cityName"),
        city_code=search_meta_json_data.get("origin").get("city"),
        state_code=search_meta_json_data.get("origin").get("stateCode"),
        country_code=search_meta_json_data.get("origin").get("countryCode"),
        domestic=search_meta_json_data.get("origin").get("domestic")
    ),
    search_destination=AirportInformation(
        airport=search_meta_json_data.get("destination").get("name"),
        city_name=search_meta_json_data.get("destination").get("cityName"),
        city_code=search_meta_json_data.get("destination").get("city"),
        state_code=search_meta_json_data.get("destination").get("stateCode"),
        country_code=search_meta_json_data.get("destination").get("countryCode"),
        domestic=search_meta_json_data.get("destination").get("domestic")
    ),
    from_date= datetime.strptime(search_meta_json_data.get("departureDate"), "%Y-%m-%d"),
    trip_type= TripTypes.ROUND_TRIP if search_meta_json_data.get("roundTrip") else TripTypes.ONE_WAY_TRIP
)

search_results_json_data = data.get("slices")

for search_result_json in search_results_json_data:
    search_result = FlightResult()
    


search_result = SearchResults(
    search_information=search_meta_data,
    search_results=None
)

print(search_result)