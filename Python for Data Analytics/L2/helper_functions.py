#from datetime import datetime
def print_rows_stations(df):
    print("number of rows:", len(df))
    print()
    print("stations in this DataFrame:")
    print(df['station'].unique())
    print()