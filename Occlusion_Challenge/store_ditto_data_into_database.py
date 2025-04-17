import requests
import csv
import time
import os

# Ditto URL and authentication
thingsURL = "http://localhost:8080/api/2/things/"
auth = ("ditto", "ditto")
thingID = 'org.otu:occlusion-data'

# Function to get feature value from Ditto (handles nested objects and missing keys)
def get_feature_value_from_ditto(thingID, feature):
    url = thingsURL + thingID + "/features/" + feature + "/properties/value"
    response = requests.get(url, auth=auth)
    
    if response.status_code == 200:
        value = response.json()
        print(f"Fetched data for {feature}: {value}")  # Debugging line to print the data
        return value  # Return the full response
    else:
        print(f"Error fetching {feature} from Ditto. Status code: {response.status_code}")
        return None  # Return None if feature is not found

# Function to save the retrieved data into a CSV file
def save_to_csv(data, filename='retrieved_data.csv', header=None):
    # Check if the file exists, and if not, write the header
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        
        # If file doesn't exist, write header
        if not file_exists and header:
            writer.writerow(header)
        
        writer.writerow(data)  # Write the row of data

# Main function to retrieve data and save it
def retrieve_and_save_data(last_timestamp):

    # Fetch the timestamp
    timestamp = get_feature_value_from_ditto(thingID, "Timestamp") or 'Not Available'\
    
    # Check if the timestamp is the same as the last one
    if timestamp == last_timestamp:
        print("No new data, stopping.")
        return None  # Return None to stop the process
    
    
    # Fetch the data from Ditto for vehicle and pedestrian location and size
    car1_location = get_feature_value_from_ditto(thingID, "Car1_Location") or {'X': 0, 'Y': 0}
    car2_location = get_feature_value_from_ditto(thingID, "Car2_Location") or {'X': 0, 'Y': 0}
    pedestrian_location = get_feature_value_from_ditto(thingID, "Pedestrian_Location") or {'X': 0, 'Y': 0}
    
    # Fetch the dimensions (Length, Width) for vehicles and pedestrians
    car1_length = get_feature_value_from_ditto(thingID, "Car1_Length") or 4.5  # Default values if not found
    car1_width = get_feature_value_from_ditto(thingID, "Car1_Width") or 2.0

    car2_length = get_feature_value_from_ditto(thingID, "Car2_Length") or 4.7
    car2_width = get_feature_value_from_ditto(thingID, "Car2_Width") or 2.2

    pedestrian_length = get_feature_value_from_ditto(thingID, "Pedestrian_Length") or 1.2
    pedestrian_width = get_feature_value_from_ditto(thingID, "Pedestrian_Width") or 0.5

    # Extract the X, Y coordinates from the data
    car1_x = car1_location.get('X', 0)
    car1_y = car1_location.get('Y', 0)

    car2_x = car2_location.get('X', 0)
    car2_y = car2_location.get('Y', 0)

    pedestrian_x = pedestrian_location.get('X', 0)
    pedestrian_y = pedestrian_location.get('Y', 0)

    # Prepare the data to save into CSV (the row to be saved)
    data = [
        timestamp, car1_x, car1_y, car1_length, car1_width,
        car2_x, car2_y, car2_length, car2_width,
        pedestrian_x, pedestrian_y, pedestrian_length, pedestrian_width,
    ]

    # Define the header (column names)
    header = [
        'Timestamp', 'Car1_X', 'Car1_Y', 'Car1_Length', 'Car1_Width',
        'Car2_X', 'Car2_Y', 'Car2_Length', 'Car2_Width',
        'Pedestrian_X', 'Pedestrian_Y', 'Pedestrian_Length', 'Pedestrian_Width',
    ]
    
    # Save the data to a CSV file
    save_to_csv(data, filename='retrieved_data.csv', header=header)
    
    return timestamp

last_timestamp = None

# Continuously fetch and save data every second (adjust the sleep time as needed)
while True:
    last_timestamp = retrieve_and_save_data(last_timestamp)
    if last_timestamp is None:
        break  # Exit the loop when no new data is found
    time.sleep(3.5)  # Fetch data every second
