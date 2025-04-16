# Vehicle Data Simulation and Setup Instructions

This module will teach you the following: how to simulate on-board diagnostics (OBD) to generate real-time vehicle data, how to integrate this data with the Kuksa Vehicle Abstraction Layer (VAL), and how to send it to the Eclipse Ditto IoT platform to create a digital twin. You will learn to generate random OBD data using Python, transmit and retrieve it through Kuksa, and configure Ditto to facilitate seamless data exchange between physical devices and external systems. Additionally, you will experiment with launching Eclipse Ditto, setting up its user interface, and configuring URLs and authentication variables to enable real-time vehicle data simulation.

### Task 0: Setting Up The Workspace

1. **Clone the Kuksa Databroker repository to your home directory**  
   ```bash
   git clone https://github.com/eclipse-kuksa/kuksa-databroker ~/  
   cd ~/kuksa-databroker
   ```
    
2. **Download the OBD file and place it inside the `kuksa-databroker` folder.**  
   - [OBD.json](https://github.com/zubxxr/sq_6/blob/main/OBD.json)

3. **Create a new folder called `kuksa-ditto` inside the `kuksa-databroker` folder.**  
   ```bash
   cd ~/kuksa-databroker
   mkdir kuksa-ditto
   ```
    
5. Download the `VSS_Ditto` and `Policy` Files` and place them inside the ‘kuksa-ditto’ folder. 
    - [policy.json](https://github.com/zubxxr/sq_6/blob/main/policy.json)
    - [VSS_Ditto.json](https://github.com/zubxxr/sq_6/blob/main/VSS_Ditto.json)
      
## 1. Simulating On-Board Diagnostics (OBD)
This task focuses on simulating on-board diagnostics (OBD) to generate real-time vehicle data, mimicking data typically provided by a vehicle's OBD system, such as engine parameters and fuel consumption. Through a simple Python script, you will learn how to generate random OBD data, laying the foundation for developing a digital twin. 

### Task 1: Creating the Python Script
1. Download and Open the File
    - Download the [generate_random_obd_data.py](https://github.com/zubxxr/sq_6/blob/main/kuksa-ditto/generate_random_obd_data.py) and place it in the `kuksa-ditto` folder.

2. Import Required Modules
    - Add these imports at the top of the file.
      ```bash
      import random
      import time
      ```
      
3. Generate Random Values for Features
    - Use the random library to generate random values for each feature within the specified ranges:
      ```
      Vehicle Speed: Generate random integers between 0 and 255.
      Engine Speed: Generate random integers between 0 and 1000. 
      Throttle Position: Generate random integers between 0 and 200.
      Coolant Temperature: Generate random integers between 0 and 500.
      ```

4. Print Each Feature Value
    - Display the generated values for each feature.
      
5. Pause and Repeat
    - Use the time library to pause the script for 1 second.

6. Execute the Script
   ![image](https://github.com/user-attachments/assets/0ee41e34-fc20-48e3-a959-d2416041e7ca)

## 2. Intro to Eclipse Kuksa.VAL and Data Orchestration
This section covers integrating simulated OBD data with the Kuksa Vehicle Abstraction Layer (VAL) platform. You will learn how to send OBD data to Kuksa and retrieve that data.

### Task 2: Powering up Kuksa.VAL 

1. Launch the Kuksa Databroker in a Docker Container
	```bash
	cd ~/kuksa-databroker
	docker run --rm -it -p 55555:55555 -v "$(pwd)/OBD.json:/OBD.json" ghcr.io/eclipse-kuksa/kuksa-databroker:main --insecure --vss /OBD.json
	```
	![image](https://github.com/user-attachments/assets/ce0ae01e-d119-4b4b-86b6-e13addc58d94)


### Task 3: Sending OBD Data to Kuksa Databroker

1. Download and Open the File
    - Download the [send_obd_data_to_kuksa.py](https://github.com/zubxxr/sq_6/blob/main/kuksa-ditto/send_obd_data_to_kuksa.py) and place it in the `kuksa-ditto` folder.
    - This is the same file created earlier with a few extra changes. The changes include:
        ```
        Lines 4 and 5 include new imports.
        Line 8 requires an update to the main function.
        Line 11 creates a connection to the Kuksa Databroker.
        Lines 23 to 28 involve sending the generated OBD data to the Databroker.
        ```

2. Complete the Code
   - There are comments in the code to guide you.

3. Create a Virtual Environment
    - Create a virtual environment `(Command is for Linux)` in the same directory as the created files. 
        ```bash
        cd ~/kuksa-databroker/kuksa-ditto
        python3 -m venv venv
        source venv/bin/activate
        pip install kuksa-client
        ```
4. Install the packages inside the Virtual Environment
     - Run the following commands:
	```bash
	pip install kuksa-client
	pip install requests
	```
   
6. Execute The File
    - Execute the code file in the activated virtual environment. It will immediately start outputting random values each second. Launch the Databroker first, then the script.
      
      ![image](https://github.com/user-attachments/assets/f19bbc03-4bbe-4572-805f-220b78f74a5f)

### Task 4: Receiving OBD Data from Kuksa Databroker
1. Create File
    - Create a file in the ‘kuksa-ditto’ folder named `retrieve_obd_data_from_kuksa.py`.
2. Copy This Code into the File
    - This file appears similar to the `send_obd_data_to_kuksa.py` file, but is focused on retrieving the data from the Databroker. 
3. Complete the Code
4. Activate the Virtual Environment
    - Open a new terminal and activate the previously created virtual environment.
5. Execute The Script
    - Launch the Databroker first, then the `send_obd_data_to_kuksa.py` script, and lastly the `retrieve_obd_data_from_kuksa.py` script.

      ![image](https://github.com/user-attachments/assets/c16f22b3-0864-4c84-9a4e-5c9595babf84)

      


## 3. Eclipse Ditto
Eclipse Ditto is an IoT backend solution that uses digital twins to create cloud-based virtual representations of real-world objects or devices. It serves as IoT middleware, facilitating communication between physical devices and external systems. Through APIs, Ditto enables seamless integration of data, allowing the exchange of information, modification, or retrieval of data. You will learn how to engage in an experiment where you will launch Eclipse Ditto and its user interface.

### Task 5: Launching Eclipse Ditto
1. Clone Repository
    - Open a terminal and enter the following commands.
        ```bash
        git clone https://github.com/eclipse-ditto/ditto ~/
        cd ~/ditto
        ```
2. Install Docker Compose

- #### Linux:
	```bash
	sudo apt-get update
	sudo apt-get install docker-compose-plugin
 	docker compose version
	```
- #### Windows:
	- TO DO

3. Start Ditto
    - Navigate to the repository and enter these commands in the terminal.
        ```bash
        cd ~/ditto/deployment/docker/
        docker compose up -d
        ```
    
4. Open URL
    - Open this url in your browser: http://localhost:8080
      
5. Open the User Interface
    - Click the first bullet point `visit the Eclipse Ditto™ explorer UI to get started with your first digital twins`.

## 4. Integration of Kuksa with Ditto
This section involves integrating Kuksa with the Ditto IoT platform to send real-time vehicle data, such as OBD information, to Ditto for simulating a digital twin. It will walk you through the necessary steps for configuring URLs and authentication variables to interact with the Ditto platform.

### URLs and Authentication Variables
The updates start with defining the URLs for the Things and Policies. These URLs are routed to list all the Things and Policies created on your device. Feel free to try entering the thingURL inside your web browser. The login and password will both be “ditto”, which was also defined in the last line as “auth”. However, the policyURL does not work.
```python
thingsURL = "http://localhost:8080/api/2/things/"
policiesURL = "http://localhost:8080/api/2/policies/"
auth = ("ditto" , "ditto")
```

### Function 1: get_thing(thingID)
This function retrieves the details of a specific "thing" using its thingID. If the thing exists, it returns its details in JSON format. If the thing is not found, it returns None.
```python
def get_thing(thingID):
    url = thingsURL + thingID
    response = requests.get(url, auth=auth)
    if response.status_code == 404:
        return None
    else:
        return response.json()
```

### Function 2: put_thing(thingID, ThingData)
This function creates a new "thing" with the given thingID and ThingData. If a thing with the same ID already exists, it asks the user if they want to overwrite it. If the user agrees, it updates the existing thing with the new data.
```python
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
```

### Function 3: patch_thing(thingID, ThingData)
This function partially updates an existing "thing" with the provided ThingData. It only modifies the fields specified in the ThingData, leaving other fields unchanged.
```python
def patch_thing(thingID, ThingData):
    url = thingsURL + thingID
    headers = {"Content-Type": "Application/merge-patch+json"}
    response = requests.patch(url, json=ThingData, headers=headers, auth=auth)
    return response
```

### Function 4: delete_thing(thingID)
This function deletes a specific "thing" identified by thingID from the system.
```python
def delete_thing(thingID):
    url = thingsURL + thingID
    response = requests.delete(url, auth=auth)
    return response
```

### Function 5: put_policy(policyID, PolicyData)
This function creates or updates a policy with the specified policyID and PolicyData. It ensures that the policy is stored with the provided details.
```python
def put_policy(policyID, PolicyData):
    url = policiesURL + policyID
    headers = {"Content-Type": "Application/json"}
    response = requests.put(url, json=PolicyData, headers=headers, auth=auth)
    return response.json()
```

### Function 6: delete_policy(policyID)
This function deletes a specific "policy" identified by policyID from the system.
```python
def delete_policy(policyID):
    url = policiesURL + policyID
    response = requests.delete(url, auth=auth)
    if response.status_code == 204:
        print(f"Policy '{policyID}' successfully deleted.")
    else:
        print(f"Failed to delete policy '{policyID}'. Status code: {response.status_code}, Response: {response.text}")
    return response
```

### Function 7: get_feature_value(thingID, feature)
This function retrieves the value of a specific feature of a "thing" identified by thingID. It returns the value as a floating-point number if successful.
```python
def get_feature_value(thingID, feature):
    url = thingsURL + thingID + "/features/" + feature + "/properties/value"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        value = float(response.json())
        return value
    else:
        return response
```

### Function 8: put_feature_value(thingID, feature, value)
This function sets or updates the value of a specific feature for a "thing" identified by thingID. The new value is provided in the value parameter.
```python
def put_feature_value(thingID, feature, value):
    url = thingsURL + thingID + "/features/" + feature + "/properties"
    headers = {"Content-Type": "Application/json"}
    data = {
        "value": value
    }
    response = requests.put(url, json=data, headers=headers, auth=auth)
    return response
```

### Task 6: Sending OBD Data to Eclipse Ditto

1. Copy File
    - Create a copy of your completed `retrieve_obd_data_from_kuksa.py` file, rename it to `send_recieved_obd_data_to_ditto.py` and place it inside the `kuksa-ditto` folder.
  
2. Add These Imports 
    - Add the following imports under the existing imports.
        ```python
        import json
        import requests
        ```

3. Add The Following Code
    - The code for each bullet point is provided at the start of this module. Add them to the top of the `send_recieved_obd_data_to_ditto.py` file under the imports but above the main function. 
        ```
        - URLs and Authentication Variables
        - Function 1: get_thing(thingID)
        - Function 2: put_thing(thingID, ThingData)
        - Function 3: patch_thing(thingID, ThingData)
        - Function 4: delete_thing(thingID)
        - Function 5: put_policy(policyID, PolicyData)
        - Function 6: delete_policy(policyID)
        - Function 7: get_feature_value(thingID, feature)
        - Function 8: put_feature_value(thingID, feature, value)
        ```

4. Use The Following Function To Receive a Response
    - At the bottom of the file where the print statements are, put each line under their respective print statement:
        ```python
        response = put_feature_value('org.vehicle:my-device' , 'VehicleSpeed' , VehicleSpeed)
        response = put_feature_value('org.vehicle:my-device' , 'EngineSpeed' , EngineSpeed)
        response = put_feature_value('org.vehicle:my-device' , 'ThrottlePosition' , ThrottlePosition)
        response = put_feature_value('org.vehicle:my-device' , 'CoolantTemperature' , CoolantTemperature)
        ```

5. Print The Response
    - For each function call in step 4, the response variable will store the result of the `put_feature_value` function. Under each response assignment, print the response.
      
6. Copy The Following Code
    - Copy this code and paste it after the main function but above the `asyncio.run(main())` line. It will be outside the main function.
		```python
		# STEP 1
		# with open("_______", "r") as dittoFile:
		# 	data = json.load(dittoFile)
		
		# response = put_policy("org.ovin:my-policy", data)
		# print(response)
		
		# STEP 2
		# with open("_______", "r") as dittoFile:
		# 	data = json.load(dittoFile)
		
		# response = put_thing("org.ovin:my-vehicle", data)
		# print(response)
		```

7. Uncomment Step 1 Code
    - Uncomment the code under Step 1 and also comment the final line: `asyncio.run(main())`. It will look like this:
      
      ![image](https://github.com/user-attachments/assets/7a1fb92d-c27e-4f6e-836d-396d13378e2d)


8. Open Policy File
    - Open the `policy.json` file inside the current folder. This file helps grant our Thing the correct policies such as read and write abilities. 

9. Go Back to Current File
    - Go back to the Step 1 code and fill in the blank.

10. Execute the File
    - Make sure your virtual environment is activated and execute the file. You will receive a message exactly the same as this after execution.
      
      ![image](https://github.com/user-attachments/assets/344fe372-6627-4a5f-946f-b2d075e999a3)


11. Uncomment Step 2 Code
    - Next, go back to the file, comment the Step 1 code, and uncomment the Step 2 code. It will look like this:

      ![image](https://github.com/user-attachments/assets/3947c3a6-0db9-48c4-ac23-3473a3f4dea0)

12. Open File
    - Open the `VSS_Ditto.json` file already created inside the current folder. This file helps link our Thing with the created policy and also defines the features of our Thing.
      
13. Go Back to Current File
    - Go back to the Step 2 code and fill in the blank.
      
14. Execute the File
    - Make sure your virtual environment is activated and execute the file. You will receive a message exactly the same as this after execution. If you get any other response number, then it did not work.
      
      ![image](https://github.com/user-attachments/assets/93b3647b-75dc-469f-9184-626e52d74d0c)

15. Open Ditto
    - Open http://localhost:8080/ in your browser
    - Open the User Interface
    - You should see a Thing ID created with the name `org.ovin:my-vehicle`
    - You can also click on each feature to see the default values written in the VSS_Ditto.json file
      
      ![image](https://github.com/user-attachments/assets/431a5b24-f649-465a-9de3-b9f9bf5e450d)

16. Uncomment the Main Function Call
    - Now, comment the Step 2 code, and uncomment the main function call.
      
16. Execute the File
    - Make sure your virtual environment is activated.
    - Run the Kuksa Databroker.
    - Run the `send_obd_data_to_kuksa.py` file.
    - Then run the `send_recieved_obd_data_to_ditto.py` file.
    - After executing the file, you should see the received messages appear in the terminal, along with the response number being 204. This means that the messages are being successfully sent to Ditto. If you get any other response number, then there is something wrong.
    - Open Ditto, and you will see the values being updated in real-time.
      
      ![image](https://github.com/user-attachments/assets/45aa70d0-453c-421b-b55b-b00885a4ebd2)

