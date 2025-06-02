from start_container import StartContainer
import requests

def main():
    StartContainer().start_postgres_container()

    new_flights_df = Flights()



if __name__ == '__main__':
    main()