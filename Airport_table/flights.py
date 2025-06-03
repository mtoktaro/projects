import requests
import pandas as pd

class Flights:
    def __init__(self):
        self.API_KEY = '8cc84bb968d58e11c127814350d963e7'  
        self.API_URL = 'http://api.aviationstack.com/v1/flights'
        # self.data = self. fetch_flight_data()
        
    def get_flights_data(self):
        params = {
            'access_key': self.API_KEY,
            'limit': 10,
            'dep_iata': 'DEN',
            'status': 'active'
        }
        response = requests.get(self.API_URL, params=params)
        data = response.json()

        # print(data)
        data = data.get("data")
        
        return data


    def clean_flights_data(self, data):
        
        records = []
        for row in data:
            record = {
                "departure_airport":row.get("departure").get("iata"),
                "flight_number": row.get("flight").get("number"),
                "departure_gate":row.get("departure").get("gate"),
                "airline":row.get("airline").get("name"),
                "arrival_airport":row.get("arrival").get("iata"),
                "departure_time":row.get("departure").get("scheduled")
            }
            records.append(record)
            print(record)
        
        return pd.DataFrame(records)
        



