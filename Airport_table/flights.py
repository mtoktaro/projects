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
            'dep_iata': 'DEN'
        }
        response = requests.get(self.API_URL, params=params)
        data = response.json()

        print(data)

        return data
