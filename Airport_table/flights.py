import requests

class Flights:
    def __init__(self):
        API_KEY = '8cc84bb968d58e11c127814350d963e7'  
        API_URL = 'http://api.aviationstack.com/v1/flights'
        params = {
            'access_key': API_KEY,
            'limit': 100,
            'dep_iata': 'DEN'
        }
        response = requests.get(API_URL, params=params)
        data = response.json()

        print(data.columns)

        return data
