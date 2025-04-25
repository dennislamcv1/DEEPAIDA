import pandas as pd

def get_list(column_name):
    # Path to the CSV file
    csv_path = 'data/retail_sampled.csv'
    
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_path)
        
        # Check if the specified column exists in the DataFrame
        if column_name in df.columns:
            # Return the column data as a list
            return df[column_name].tolist()
        else:
            # If the column does not exist, raise an error
            raise ValueError("Column name not found in the DataFrame")
    except Exception as e:
        # Print any error that occurs during the process
        print(f"An error occurred: {e}")
