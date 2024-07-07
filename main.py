#importing custom functions
from helpers import get_client, get_postgres_engine
from extract import fetch_data
from load import load_csv_to_postgres
import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text



query = '''
        select pickup_date, vendor_id, passenger_count, trip_distance, payment_type, fare_amount, tip_amount 
        from tripdata
        where year(pickup_date) = 2015 and month(pickup_date) = 1 and day(pickup_date) = 3
     '''

# call the functions to get the client and engine 
client = get_client()
engine = get_postgres_engine()

def main():
    '''
    main function to run the data pipeline modules

    parameters: none

    return : none
    '''
    #extract the data
    fetch_data(client=client, query=query)

    #load the data
    load_csv_to_postgres('tripdata.csv', 'tripdata', engine, 'STG')



    ## excecute stored procedure
    session = sessionmaker(bind=engine)
    session = session()
    session.execute(text('CALL "STG".agg_tripdata()'))
    session.commit()

    print('stored procedure executed')
    

    print('pipeline executed successfully')

if __name__ == '__main__':
    main()
