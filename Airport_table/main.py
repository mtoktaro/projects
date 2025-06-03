from container import Container
import requests
from flights import Flights
from sqlalchemy import create_engine
from sql_operations import execute_query


def main():
    # Start PostgreSQL container
    container = Container().start_postgres_container()
    
    flights = Flights()
    flights_df = flights.get_flights_data()
    
    flights_cleaned_df = flights.clean_flights_data(flights_df)

    Container().write_to_postgres(flights_cleaned_df, 'flight_departures')
    
    engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')

    airline_name = 'United Airlines'
    result_1 = execute_query(f"SELECT * FROM flight_departures WHERE airline = '{airline_name}'", engine)
    
    for row in result_1:
        print(row)
    
    if container:
        container.stop()
        container.remove()
        print("Container stopped and removed")


if __name__ == '__main__':
    main()