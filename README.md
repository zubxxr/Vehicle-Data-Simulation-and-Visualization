# sq_6


## Module 1: The Software Defined Vehicle (SDV) World
This module explores Software Defined Vehicles (SDVs), focusing on real-time vehicle data collection and the construction of an SDV stack from scratch. It covers the basics of SDVs, including their architecture, advantages like dynamic feature access, advanced onboard safety, and seamless connectivity, as well as challenges such as exponential software growth, industry competition, and cybersecurity risks. Participants will learn about SDV components like user applications, instrumentation, embedded OS, and hardware, and how tools like Kuksa.VAL simplify data integration for SDVs. The course will also delve into hands-on experiments to help students develop skills in SDV architecture and testing.

## Experiment 1: Setting Up The Workspace
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

## Experiment 2: Creating the Python Script
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

