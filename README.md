# sq_6


## Module 1: The Software Defined Vehicle (SDV) World
This module explores Software Defined Vehicles (SDVs), focusing on real-time vehicle data collection and the construction of an SDV stack from scratch. It covers the basics of SDVs, including their architecture, advantages like dynamic feature access, advanced onboard safety, and seamless connectivity, as well as challenges such as exponential software growth, industry competition, and cybersecurity risks. Participants will learn about SDV components like user applications, instrumentation, embedded OS, and hardware, and how tools like Kuksa.VAL simplify data integration for SDVs. The course will also delve into hands-on experiments to help students develop skills in SDV architecture and testing.

### Experiment 1: Setting Up The Workspace

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
    
5. Download the VSS_Ditto and Policy Files and place them inside the ‘kuksa-ditto’ folder. 
    - [policy.json](https://github.com/zubxxr/sq_6/blob/main/policy.json)
    - [VSS_Ditto.json](https://github.com/zubxxr/sq_6/blob/main/VSS_Ditto.json)
      
## Module 2: 
Module 2 focuses on simulating on-board diagnostics (OBD) to generate real-time vehicle data, mimicking data typically provided by a vehicle's OBD system, such as engine parameters and fuel consumption. Through a simple Python script, participants will learn how to generate random OBD data, laying the foundation for developing a digital twin. This module also introduces OBD2, a standardized system used for vehicle diagnostics since 1991, which helps with tasks like vehicle logging, real-time diagnostics, predictive maintenance, and vehicle black box logging.

### Experiment 2: Creating the Python Script
1. Create File
    - Create a file inside the ‘kuksa-ditto’ folder and name it ‘generate_random_obd_data.py’.

2. Import Required Modules
    - Add these imports at the top of the file.
      ```bash
      import random
      import time
      ```

3. Generate Random Values for Features
    - Use the random module to generate random values for each feature within the specified ranges:
      ```
      Vehicle Speed: Generate random integers between 0 and 255.
      Engine Speed: Generate random integers between 0 and 1000. 
      Throttle Position: Generate random integers between 0 and 200.
      Coolant Temperature: Generate random integers between 0 and 500.
      ```
4. Print Each Feature Value
    - Display the generated values for each feature.
5. Pause and Repeat
    - Pause for 1 second, then repeat the process.


## Module 3: Intro to Eclipse Kuksa.VAL and Data Orchestration

Module 3 covers integrating simulated OBD data with the Kuksa Vehicle Abstraction Layer (VAL) platform. Participants will learn about the Kuksa VAL architecture, its components, and how to send OBD data to Kuksa and Ditto. In the experiment, they will run the Kuksa broker, update a script to send OBD data, and set up another script to receive it, enabling real-time integration of vehicle data into Kuksa. The module also explores the Vehicle Signal Specification (VSS), which standardizes vehicle signal definitions and categorizes them into sensors, actuators, and attributes. The Kuksa VAL system architecture, including VSS servers, clients, data providers, and actuation providers, is essential for managing vehicle data efficiently.

### Experiment 4: Powering up Kuksa.VAL 

1. Execute Commands
    - Run these commands to start the Kuksa Databroker. Some of them may take a while.
        ```bash
        cd ~/kuksa-databroker
        docker run --rm -it -p 55555:55555 -v "$(pwd)/OBD.json:/OBD.json" ghcr.io/eclipse-kuksa/kuksa-databroker:main --insecure --vss /OBD.json
        ```

    - Here is the output after executing the final command, which starts the Databroker server.
        ![image](https://github.com/user-attachments/assets/ce0ae01e-d119-4b4b-86b6-e13addc58d94)


### Experiment 5: Sending OBD Data to Kuksa Databroker

1. Create File
    - Make a new file inside the ‘kuksa-ditto’ folder and name it ‘send_obd_data_to_kuksa.py’.
2. Copy This Code into the File
    - This is the same file created earlier with a few extra changes. The changes include:
        ```
        Lines 4 and 5 include new imports.
        Line 8 requires an update to the main function.
        Line 11 creates a connection to the Kuksa Databroker.
        Lines 23 to 28 involve sending the generated OBD data to the Databroker.
        ```
3. Complete the Code

4. Create a Virtual Environment
    - Create the virtual environment in the same directory as the created files. Follow these steps to create and activate it:
        ```
        sudo apt install python3-venv
        python3 -m venv venv
        source venv/bin/activate
        pip install kuksa-client
        ```
5. Execute The File
    - Finally, execute the code file in the activated virtual environment. It will immediately start outputting random values each second. Just make sure that the Kuksa Databroker is also running in another terminal. Here is an example of its output:

### Experiment 6: Receiving OBD Data from Kuksa Databroker
1. Create File
    - Create a file in the ‘kuksa-ditto’ folder named ‘retrieve_obd_data_from_kuksa.py’.
2. Copy This Code into the File
    - This file appears similar to the ‘send_obd_data_to_kuksa.py’ file, but is focused on retrieving the data from the Databroker. 
3. Complete the Code
4. Activate the Virtual Environment
    - Open a new terminal and activate the previously created virtual environment.
5. Execute The File
    - First keep the ‘send_obd_data_to_kuksa.py’ file running in one terminal, and then execute the file just created in the activated virtual environment. It should be receiving the exact same messages being generated from the ‘send_obd_data_to_kuksa.py’ file. Here is an example of the output:

## Module 4: Eclipse Ditto

Module 4 focuses on Eclipse Ditto, explaining its features and how the digital twin concept operates. Participants will learn about key concepts such as Things, Policies, and their interactions. Eclipse Ditto is an IoT backend solution that uses digital twins to create cloud-based virtual representations of real-world objects or devices. It serves as IoT middleware, facilitating communication between physical devices and external systems. Through APIs, Ditto enables seamless integration of data, allowing the exchange of information, modification, or retrieval of data. Participants will also engage in an experiment where they will launch Eclipse Ditto and explore its user interface.

### Experiment 6: Launching Eclipse Ditto
1. Clone Repository
    - Open a terminal and enter the following commands.
        ```bash
        git clone https://github.com/eclipse-ditto/ditto ~/
        cd ~/ditto
        ```
    
2. Start Ditto
    - Navigate to the repository and enter these commands in the terminal.
        ```bash
        cd ~/ditto/deployment/docker/
        docker-compose up -d
        ```
    
3. Open URL
    - Open this url in your browser: http://localhost:8080
      
4. Open the User Interface
    - Click the first bullet point ‘visit the Eclipse Ditto™ explorer UI to get started with your first digital twins’.

## Module 5: Integration of Kuksa with Ditto

Module 5: Integration of Kuksa with Ditto introduces participants to the process of integrating Kuksa with the Ditto IoT platform to send real-time vehicle data, such as OBD information, to Ditto for simulating a digital twin. This module walks through the necessary steps for configuring URLs and authentication variables to interact with the Ditto platform. Participants will also learn about key functions, such as retrieving, updating, and deleting "things" and "policies," as well as managing features within the platform. The module ensures a seamless flow of data from Kuksa to Ditto for real-time monitoring and digital twin creation.

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
	if (thing == None):
    	   headers = {"Content-Type": "Application/json"}
    	   response = requests.put(url, json=ThingData, headers=headers, auth=auth)
    	   return response
	else:
    	   print("There is a thing already created with same thingID")
    	   print("Do you want to overwrite it(y/n)?")
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
	headers = {"Content-Type": "Application/merget-patch+json"}
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
def put_policy (policyID, PolicyData):
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

### Experiment 7: Sending OBD Data to Eclipse Ditto

1. Copy File
    - Create a copy of the retrieve_obd_data_from_kuksa.py file in the ‘kuksa-ditto’ folder and rename it to ‘send_recieved_obd_data_to_ditto.py’.
2. Add These Imports 
	- Add the following imports under the existing imports.
        ```python
        import json
        import requests
        ```


3. Add The Following Code
    - Add the following code at the top of the file under the imports. This code will be above the main function. You will find them at the start of this module under each of the following sections:
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
        ```
        - response = put_feature_value('org.vehicle:my-device' , 'VehicleSpeed' , VehicleSpeed)
        - response = put_feature_value('org.vehicle:my-device' , 'EngineSpeed' , EngineSpeed)
        - response = put_feature_value('org.vehicle:my-device' , 'EngineSpeed' , EngineSpeed)
        - response = put_feature_value('org.vehicle:my-device' , 'CoolantTemperature' , CoolantTemperature)
        ```

5. Print The Response
    - For each function call in step 4, the response variable will store the result of the put_feature_value function. Under each respective print statement, print the response to see the outcome of the function call for each feature.
      
6. Copy The Following Code
    - Copy this code and paste it after the main function but above the ‘asyncio.run(main())’ line. It will be outside the main function.
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
    - Uncomment the code under Step 1 and also comment the final line: ‘asyncio.run(main())’. It will look like this:
      
      ![image](https://github.com/user-attachments/assets/7a1fb92d-c27e-4f6e-836d-396d13378e2d)


8. Open Policy File
    - Open the ‘policy.json’ file already created inside the current folder. This file helps grant our Thing the correct policies such as read and write abilities. 

9. Go Back to Current File
    - Go back to the Step 1 code and fill in the blank.

10. Execute the File
    - Execute the file. You will receive a message exactly the same as this after execution.

11. Uncomment Step 2 Code
    - Next, go back to the file, comment the Step 1 code, and uncomment the Step 2 code. It will look like this:

      ![image](https://github.com/user-attachments/assets/3947c3a6-0db9-48c4-ac23-3473a3f4dea0)


12. Open Thing File
    - Open the ‘VSS_Ditto.json’ file already created inside the current folder. This file helps link our Thing with the created policy and also defines the features of our Thing.
13. Go Back to Current File
    - Go back to the Step 2 code and fill in the blank.
14. Execute the File
    - Execute the file. You will receive a message exactly the same as this after execution. If you get any other response number, then it did not work.
      
      ![image](https://github.com/user-attachments/assets/55c284f4-3897-4549-bf00-811dd92deac4)

15. Uncomment the Main Function Call
    - Now, comment the Step 2 code, and uncomment the main function call. We are now done with creating the Thing and Policy, and can now go back to the main function, which will send the received data to Ditto.
      
16. Execute the File
    - Finally, for the final time, you can execute the file again. However, make sure that the Kuksa Databroker is running, and the ‘send_obd_data_to_kuksa.py’ file is also running. After executing the file, you should see the received messages appear in the terminal, along with the response number being 204. This means that the messages are being successfully sent to Ditto. If you get any other response number, then there is something wrong.
