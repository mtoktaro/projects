from start_container import StartContainer
import requests
from flights import Flights


def main():
    # Start PostgreSQL container
    container = StartContainer().start_postgres_container()
    
    flights = Flights()
    flights_df = flights.get_flights_data()
    # print(flights_df.head())
    
    if container:
        container.stop()
        container.remove()
        print("Container stopped and removed")


if __name__ == '__main__':
    main()