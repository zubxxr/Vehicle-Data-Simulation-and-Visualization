import asyncio
from kuksa_client.grpc.aio import VSSClient
import json
import requests
import time

thingsURL = "http://localhost:8080/api/2/things/"
policiesURL = "http://localhost:8080/api/2/policies/"
auth = ("ditto", "ditto")

def get_thing(thingID):
    url = thingsURL + thingID
    response = requests.get(url, auth=auth)
    if response.status_code == 404:
        return None
    else:
        return response.json()

def put_thing(thingID, ThingData):
    thing = get_thing(thingID)
    url = thingsURL + thingID
    if thing is None:
        headers = {"Content-Type": "Application/json"}
        response = requests.put(url, json=ThingData, headers=headers, auth=auth)
        return response
    else:
        print("There is a thing already created with the same thingID")
        print("Do you want to overwrite it (y/n)?")
        answer = input()
        if answer.lower() == 'y':
            headers = {"Content-Type": "Application/json"}
            response = requests.put(url, json=ThingData, headers=headers, auth=auth)
            return response

def patch_thing(thingID, ThingData):
    url = thingsURL + thingID
    headers = {"Content-Type": "Application/merge-patch+json"}
    response = requests.patch(url, json=ThingData, headers=headers, auth=auth)
    return response

def delete_thing(thingID):
    url = thingsURL + thingID
    response = requests.delete(url, auth=auth)
    return response


def put_policy(policyID, PolicyData):
    url = policiesURL + policyID
    headers = {"Content-Type": "Application/json"}
    response = requests.put(url, json=PolicyData, headers=headers, auth=auth)
    return response.json()

def delete_policy(policyID):
    url = policiesURL + policyID
    response = requests.delete(url, auth=auth)
    if response.status_code == 204:
        print(f"Policy '{policyID}' successfully deleted.")
    else:
        print(f"Failed to delete policy '{policyID}'. Status code: {response.status_code}, Response: {response.text}")
    return response

def get_feature_value(thingID, feature):
    url = thingsURL + thingID + "/features/" + feature + "/properties/value"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        value = float(response.json())
        return value
    else:
        return response

def put_feature_value(thingID, feature, value):
    url = thingsURL + thingID + "/features/" + feature + "/properties"
    headers = {"Content-Type": "Application/json"}
    data = {
        "value": value
    }
    response = requests.put(url, json=data, headers=headers, auth=auth)
    return response

# Function to construct the raw GitHub URL for each image
def get_github_image_url(image_filename):
    return image_filename


# Asynchronous main function to connect to KUKSA Databroker and send data from CSV
async def main():
    async with VSSClient('127.0.0.1', 55555) as client:
        while True:
            # Get image data and coordinates from KUKSA
            values = await client.get_current_values([
                'Vehicle.Images.OccludedImage', 'Vehicle.Images.OccludingCar', 'Vehicle.Images.GroundTruthView',
                'Vehicle.Coordinates.Car1_Location.X', 'Vehicle.Coordinates.Car1_Location.Y',
                'Vehicle.Coordinates.Car2_Location.X', 'Vehicle.Coordinates.Car2_Location.Y',
                'Vehicle.Coordinates.Pedestrian_Location.X', 'Vehicle.Coordinates.Pedestrian_Location.Y',
                'Vehicle.Timestamp',
                'Vehicle.Coordinates.Car1_Length', 'Vehicle.Coordinates.Car1_Width',
                'Vehicle.Coordinates.Car2_Length', 'Vehicle.Coordinates.Car2_Width',
                'Vehicle.Coordinates.Pedestrian_Length', 'Vehicle.Coordinates.Pedestrian_Width'
            ])

            # Fetch the image filenames from KUKSA
            OccludedImage = values['Vehicle.Images.OccludedImage'].value
            OccludingCar = values['Vehicle.Images.OccludingCar'].value
            GroundTruthView = values['Vehicle.Images.GroundTruthView'].value

            # Fetch the car and pedestrian coordinates from KUKSA
            car1_x = values['Vehicle.Coordinates.Car1_Location.X'].value
            car1_y = values['Vehicle.Coordinates.Car1_Location.Y'].value

            car2_x = values['Vehicle.Coordinates.Car2_Location.X'].value
            car2_y = values['Vehicle.Coordinates.Car2_Location.Y'].value

            pedestrian_x = values['Vehicle.Coordinates.Pedestrian_Location.X'].value
            pedestrian_y = values['Vehicle.Coordinates.Pedestrian_Location.Y'].value

            # Fetch the vehicle and pedestrian dimensions from KUKSA
            car1_length = values['Vehicle.Coordinates.Car1_Length'].value
            car1_width = values['Vehicle.Coordinates.Car1_Width'].value

            car2_length = values['Vehicle.Coordinates.Car2_Length'].value
            car2_width = values['Vehicle.Coordinates.Car2_Width'].value

            pedestrian_length = values['Vehicle.Coordinates.Pedestrian_Length'].value
            pedestrian_width = values['Vehicle.Coordinates.Pedestrian_Width'].value

            timestamp = values['Vehicle.Timestamp'].value

            # Construct the GitHub URLs for the images
            occluded_image_url = get_github_image_url(OccludedImage)
            occluding_car_url = get_github_image_url(OccludingCar)
            ground_truth_url = get_github_image_url(GroundTruthView)

            # Send the image URLs to Ditto
            print('occluded_image_url =', occluded_image_url)
            response = send_image_url_to_ditto('org.otu:occlusion-data', 'OccludedImage', occluded_image_url)
            print(response)

            print('occluding_car_url =', occluding_car_url)
            response = send_image_url_to_ditto('org.otu:occlusion-data', 'OccludingCar', occluding_car_url)
            print(response)

            print('ground_truth_url =', ground_truth_url)
            response = send_image_url_to_ditto('org.otu:occlusion-data', 'GroundTruthView', ground_truth_url)
            print(response)

            # Send the car coordinates to Ditto as objects
            car1_location = {'X': car1_x, 'Y': car1_y}
            print(f"Sending Car1 Location: {car1_location}")
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Car1_Location', car1_location)
            print(response)

            car2_location = {'X': car2_x, 'Y': car2_y}
            print(f"Sending Car2 Location: {car2_location}")
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Car2_Location', car2_location)
            print(response)

            # Send the pedestrian location to Ditto as objects
            pedestrian_location = {'X': pedestrian_x, 'Y': pedestrian_y}
            print(f"Sending Pedestrian Location: {pedestrian_location}")
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Pedestrian_Location', pedestrian_location)
            print(response)

            # Send the dimensions to Ditto
            print(f"Sending Car1 Length: {car1_length}, Car1 Width: {car1_width}")
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Car1_Length', car1_length)
            print(response)
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Car1_Width', car1_width)
            print(response)

            print(f"Sending Car2 Length: {car2_length}, Car2 Width: {car2_width}")
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Car2_Length', car2_length)
            print(response)
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Car2_Width', car2_width)
            print(response)

            print(f"Sending Pedestrian Length: {pedestrian_length}, Pedestrian Width: {pedestrian_width}")
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Pedestrian_Length', pedestrian_length)
            print(response)
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Pedestrian_Width', pedestrian_width)
            print(response)

            # Send the timestamp to Ditto
            print(f"Sending Timestamp: {timestamp}")
            response = send_feature_to_ditto('org.otu:occlusion-data', 'Timestamp', timestamp)
            print(response)

            time.sleep(1)
            print('-----------------------------')

# Function to send the image URL to Ditto
def send_image_url_to_ditto(thingID, feature, image_url):
    url = thingsURL + thingID + "/features/" + feature + "/properties"
    headers = {"Content-Type": "Application/json"}
    data = {
        "value": image_url
    }
    response = requests.put(url, json=data, headers=headers, auth=auth)
    return response

# Function to send feature value to Ditto
def send_feature_to_ditto(thingID, feature, value):
    url = thingsURL + thingID + "/features/" + feature + "/properties"
    headers = {"Content-Type": "Application/json"}
    data = {
        "value": value
    }
    response = requests.put(url, json=data, headers=headers, auth=auth)
    return response

# STEP 1
# with open("policy.json", "r") as dittoFile:
#     data = json.load(dittoFile)

# response = put_policy("org.otu:occlusion-policy", data)
# print(response)

# # STEP 2
# with open("Occlusion_Ditto.json", "r") as dittoFile:
#     data = json.load(dittoFile)
#     print(data)

# response = put_thing("org.otu:occlusion-data", data)
# print(response)

asyncio.run(main())

# response = delete_policy("org.otu:occlusion-policy")
# print(response)
# response = delete_thing("org.otu:occlusion-data")
# print(response)





