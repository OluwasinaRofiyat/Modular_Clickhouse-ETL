
from sqlalchemy import create_engine
import clickhouse_connect
from dotenv import load_dotenv
import os
import configparser




load_dotenv(override=True)

def get_client():
    '''
    connects to a clickhouse database using parameters from a .env File

    parameters: None

    returns:
    - clickhouse_connect.client: A database client object
    '''

    ## getting credentials
    host = os.getenv('ch_host')
    port = os.getenv('ch_port')
    user = os.getenv('ch_user')
    password = os.getenv('ch_password')

    ##connect to database
    client = clickhouse_connect.get_client(host = host, port = port, username = user, password = password, secure = True)

    return client


def get_postgres_engine():
    '''
    construct a sqlalchemy engine for postgres DB from .env file 

    parameters: none 

    Return: 
    - sqlalchemy engine (sqlalchemy.engine.Engine)
    '''
    engine = create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
                            user = os.getenv('pg_user'),
                            password = os.getenv('pg_password'),
                            host = os.getenv('pg_host'),
                            port = os.getenv('pg_port'),
                            dbname = os.getenv('pg_dbname')
                             )
                         )
    return engine

print(os.getenv('pg_host'))

