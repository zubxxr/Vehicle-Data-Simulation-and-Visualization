import pandas as pd
import asyncio
import time
from kuksa_client.grpc.aio import VSSClient
from kuksa_client.grpc import Datapoint
from PIL import Image
from io import BytesIO
import os

# Function to read CSV file and return the data
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Ensure that all numeric values are treated as floats
def ensure_float(value):
    try:
        return float(value)
    except ValueError:
        return None  # If the value can't be converted to float, return None

# Asynchronous main function to connect to KUKSA Databroker and send data from CSV
async def main():
    # Load CSV data
    csv_data = read_csv('Labels.csv')
    
    # Establish an asynchronous connection to the KUKSA Databroker at the IP: 127.0.0.1 and port 55555
    async with VSSClient('127.0.0.1', 55555) as client:
        # Iterate through each row in the CSV
        for index, row in csv_data.iterrows():

            # Extract the vehicle coordinates and pedestrian data from the CSV
            car1_x = ensure_float(row['Car1_Location_X'])
            car1_y = ensure_float(row['Car1_Location_Y'])
            
            car2_x = ensure_float(row['Car2_Location_X'])
            car2_y = ensure_float(row['Car2_Location_Y'])
            
            pedestrian_x = ensure_float(row['Pedestrian_Location_X'])
            pedestrian_y = ensure_float(row['Pedestrian_Location_Y'])

            # Extract the vehicle and pedestrian dimensions from the CSV
            car1_length = ensure_float(row['Car1_Length'])
            car1_width = ensure_float(row['Car1_Width'])
            
            car2_length = ensure_float(row['Car2_Length'])
            car2_width = ensure_float(row['Car2_Width'])
            
            pedestrian_length = ensure_float(row['Pedestrian_Length'])
            pedestrian_width = ensure_float(row['Pedestrian_Width'])

            timestamp = str(row['Timestamp'])  # Ensure timestamp is a string
            
            # Prepare the vehicle data to send to KUKSA
            vehicle_data = {
                'Vehicle.Coordinates.Car1_Location.X': Datapoint(car1_x),
                'Vehicle.Coordinates.Car1_Location.Y': Datapoint(car1_y),
                'Vehicle.Coordinates.Car2_Location.X': Datapoint(car2_x),
                'Vehicle.Coordinates.Car2_Location.Y': Datapoint(car2_y),
                'Vehicle.Coordinates.Pedestrian_Location.X': Datapoint(pedestrian_x),
                'Vehicle.Coordinates.Pedestrian_Location.Y': Datapoint(pedestrian_y),
                'Vehicle.Timestamp': Datapoint(timestamp),
                'Vehicle.Coordinates.Car1_Length': Datapoint(car1_length),
                'Vehicle.Coordinates.Car1_Width': Datapoint(car1_width),
                'Vehicle.Coordinates.Car2_Length': Datapoint(car2_length),
                'Vehicle.Coordinates.Car2_Width': Datapoint(car2_width),
                'Vehicle.Coordinates.Pedestrian_Length': Datapoint(pedestrian_length),
                'Vehicle.Coordinates.Pedestrian_Width': Datapoint(pedestrian_width)
            }
        
            # Send the data to the KUKSA Databroker
            values = await client.set_current_values(vehicle_data)
        
            # Print the values for debugging
            print(f"Sending data for record {index + 1}:")
            print(f"Car1 Location = ({car1_x}, {car1_y})")
            print(f"Car2 Location = ({car2_x}, {car2_y})")
            print(f"Pedestrian Location  = ({pedestrian_x}, {pedestrian_y})")
            print(f"Timestamp = {timestamp}")
            print(f"Car1 Length = {car1_length}, Car1 Width = {car1_width}")
            print(f"Car2 Length = {car2_length}, Car2 Width = {car2_width}")
            print(f"Pedestrian Length = {pedestrian_length}, Pedestrian Width = {pedestrian_width}")
            print('-----------------------------')

            # Wait before sending the next data (adjust this based on your needs)
            time.sleep(3)

# Run the asynchronous main function
asyncio.run(main())
