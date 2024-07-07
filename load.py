import pandas as pd

def load_csv_to_postgres(csv_file_path, table_name, engine, schema):
    '''
    load data from a csv file to datatframe to postgres database table

    parameters:
    - csv_file_path (str): path to the csv file
    - table_name(str): postgres database table
    _ engine(sqlalchemy.engine): sqlalchemy engine object
    _ schema(str): a postgress DB schema
    '''

    #read csv to pandas and to sql
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, schema=schema)

    print(f'{len(df)}rows loaded to staging successfully')