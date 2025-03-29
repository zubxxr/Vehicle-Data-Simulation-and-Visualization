# sq_6


## Module 1: The Software Defined Vehicle (SDV) World
This module explores Software Defined Vehicles (SDVs), focusing on real-time vehicle data collection and the construction of an SDV stack from scratch. It covers the basics of SDVs, including their architecture, advantages like dynamic feature access, advanced onboard safety, and seamless connectivity, as well as challenges such as exponential software growth, industry competition, and cybersecurity risks. Participants will learn about SDV components like user applications, instrumentation, embedded OS, and hardware, and how tools like Kuksa.VAL simplify data integration for SDVs. The course will also delve into hands-on experiments to help students develop skills in SDV architecture and testing.

### Experiment 1: Setting Up The Workspace
1. Clone the Kuksa Databroker Repository
    ```bash
    git clone https://github.com/eclipse-kuksa/kuksa-databroker ~/
    cd ~/kuksa-databroker
    ```
    
2. Download the OBD file and place it inside the ‘kuksa-databroker’ folder.
    - OBD.json: https://drive.google.com/file/d/1FIUlDSE6YCA7jLLp798unJA9cq2-2TCr/view?usp=sharing
      
3. Create a New Folder called ‘kuksa-ditto’ inside the ‘kuksa-databroker’ folder.
    ```bash
    cd ~/kuksa-databroker
    mkdir kuksa-ditto
    ```
    
4. Download the VSS_Ditto and Policy Files and place them inside the ‘kuksa-ditto’ folder. 
    - Policy.json: https://drive.google.com/file/d/1LfGWvJiX5lDKcYwHK5baw3grXGgXEdY2/view?usp=sharing
    - VSS_Ditto.json: https://drive.google.com/file/d/144SDC-i9sqOTQRbiWMvzpZrCGNOI0FQz/view?usp=drive_link
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
        sudo apt update
        sudo apt install build-essential
        sudo apt install curl
        curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
        echo '. "$HOME/.cargo/env"' >> ~/.bashrc
        source ~/.bashrc
        cargo run --bin databroker -- --vss OBD.json
        ```

    - Here is the output after executing the final command, which starts the Databroker server.
        ![image](https://github.com/user-attachments/assets/b6aa2515-6330-433d-9810-138c7556c5ff)

### Experiment 5: Sending OBD Data to Kuksa Databroker

1. Create File
    - Make a new file inside the ‘kuksa-ditto’ folder and name it ‘send_obd_data_to_kuksa.py’.
2. Copy This Code into the File
    - This is the same file created earlier with a few extra changes. The changes include:
        ```
        Lines 4 and 5 include new imports.
        Line 8 requires an update to the main function.
        Line 11 creates a connection to the Kuksa Databroker.
        Lines 24 to 29 involve sending the generated OBD data to the Databroker.
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

### Experiment 3: Receiving OBD Data from Kuksa Databroker
1. Create File
    - Create a file in the ‘kuksa-ditto’ folder named ‘retrieve_obd_data_from_kuksa.py’.
2. Copy This Code into the File
    - This file appears similar to the ‘send_obd_data_to_kuksa.py’ file, but is focused on retrieving the data from the Databroker. 
3. Complete the Code
4. Activate the Virtual Environment
    - Open a new terminal and activate the previously created virtual environment.
5. Execute The File
    - First keep the ‘send_obd_data_to_kuksa.py’ file running in one terminal, and then execute the file just created in the activated virtual environment. It should be receiving the exact same messages being generated from the ‘send_obd_data_to_kuksa.py’ file. Here is an example of the output:


