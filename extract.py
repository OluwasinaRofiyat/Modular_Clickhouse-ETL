import pandas as pd

#function to get data
def fetch_data(client, query):
    '''
    fetches query from a clickhouse database and write to a csv file

    parameters:
    - client(clickhouse_connect.client)
    - query(A sql select query)

    returns: none
    '''
    #execute the query
    output = client.query(query)
    rows = output.result_rows
    cols = output.column_names

    #close client
    client.close()

    #write to pandas df and csv file
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv('tripdata.csv', index=False)

    print(f'{len(df)} rows successfully extracted')

