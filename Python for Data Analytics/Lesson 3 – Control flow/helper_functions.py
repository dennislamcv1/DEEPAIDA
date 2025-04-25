import pandas as pd
import matplotlib.pyplot as plt

def create_line_chart(years, incomes):
    plt.figure(figsize=(10, 6))  # Set the figure size to be larger for better readability
    plt.plot(years, incomes, marker='o', linestyle='-', color='dodgerblue')  # Plotting the data
    
    # Adding titles and labels
    plt.xlabel('Time')  # X-axis label as 'Time'
    plt.ylabel('')  # Y-axis label left blank as per your request
    
    # Style customizations
    plt.grid(True)  # Adding a grid for better readability of plotted data
    plt.tight_layout()  # Adjust layout to make room for label rotation
    
    # Display the plot
    plt.show()

def get_list(column_name):
    # Path to the CSV file
    csv_path = 'library_data.csv'
    
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

def get_restaurant_list(column_name):
    # Path to the CSV file
    csv_path = 'restaurant_data.csv'
    
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
