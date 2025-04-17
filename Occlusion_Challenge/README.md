# Occlusion Challenge: Visualizing and Evaluating Vehicle-Pedestrian Data

## Objective
The goal of this challenge is to visualize the positions of vehicles and pedestrians in a 2D bird's eye view format, based on real-time data extracted from Ditto. You will be tasked with representing car locations, pedestrian positions, and their dimensions (length, width) on a simple 2D plot. You will then assess whether these objects are too close to each other, making sure the system accounts for safety and spatial relationships.

# Table of Contents

  - [Objective](#objective)
  - [Setup](#setup)
  - [Challenge](#challenge)
  - [Submission Requirements](#submission-requirements)
  - [Evaluation Criteria](#evaluation-criteria)
  - [Challenges You Will Learn](#challenges-you-will-learn)


## Setup
1. **Start the Kuksa Databroker with the Occlusion Config File**
   - Open a terminal and run the code.
     ```bash 
     cd ~/kuksa-databroker
     docker run --rm -it -p 55555:55555 -v "$(pwd)/occlusion_data_config.json:/occlusion_data_config.json" ghcr.io/eclipse-kuksa/kuksa-databroker:main --insecure --vss /occlusion_data_config.json
     ```

2. **Send Data from the Labels.csv file to Kuksa**
   - Open a new terminal and run the code.
     ```bash 
     cd ~/kuksa-databroker/Occlusion_Challenge
     source ../kuksa-ditto/venv/bin/activate
     python3 send_occlusion_data_to_kuksa.py
     ```
     
3. **Create Thing and Policy**
   - Open the `send_data_to_ditto.py` file.
   - Open a new terminal and run the Step 1 and Step 2 code as specifed before. Make sure to comment the main function call.
     ```bash 
     cd ~/kuksa-databroker/Occlusion_Challenge
     source ../kuksa-ditto/venv/bin/activate
     python3 send_data_to_ditto.py
     ```
     
4. **Retreive Data from the Kuksa and Send it to Ditto**
   - Run the same file from step 3 with the Step 1 and Step 2 code commented, and the main function uncommented.
     ```bash 
     python3 send_data_to_ditto.py
     ```
     ![image](https://github.com/user-attachments/assets/c40f57cc-d069-4da9-8a2b-9a8f99b970a0)

5. **Open Ditto**
    - In Ditto, you will see the values being updated in real-time.
      ![image](https://github.com/user-attachments/assets/7568e53f-642d-4b65-9ca5-2433c680b12f)

6. **Retreive the data from Ditto and save it to a local CSV file**
   - Open a new terminal and run the code.
     ```bash 
     cd ~/kuksa-databroker/Occlusion_Challenge
     source ../kuksa-ditto/venv/bin/activate
     python3 store_ditto_data_into_database.py
     ```   

## Challenge

### Steps:

1. **Data Retrieval**:
   - Write a script to **retrieve real-time data** from the **new CSV file** (acting as a database). The data includes:
     - **Timestamps**
     - **Car 1 and Car 2 locations (X, Y)**
     - **Pedestrian location (X, Y)**
     - **Car dimensions (Length, Width)**
     - **Pedestrian dimensions (Length, Width)**

2. **Bird's Eye View Visualization**:
   - Once the data is retrieved, you will **visualize** it on a **2D plot** using **Matplotlib**, **Plotly**, or any other visualization tool or library you prefer.
   - Each **vehicle** (Car 1, Car 2) will be represented as a **rectangle**, sized based on the **vehicle's length and width**. Make Car 1 the color red, and Car 2 the color green.
   - The **pedestrian** will be represented as a **rectangle** or **circle**, sized based on the **pedestrian's length and width**. Make it the color blue.
   - **Axis labels**: Add **"X Coordinate"** and **"Y Coordinate"** labels, and a **title** for the plot.

Here is an example of what the plot should look like once the data is visualized. 
![image](https://github.com/user-attachments/assets/aebdf6b9-5805-4068-85ad-9bcb0db15a5d)

3. **Danger Zone Calculation**:
   - Calculate the **danger zone** around each vehicle based on a **threshold distance** (e.g., 1.5 times the vehicle's width).
   - **Determine whether a pedestrian is inside the danger zone**. If the pedestrian is within this range, the vehicle should take action (e.g., stop or alert).
   - The danger zone for each vehicle should be visualized, with a **color-coded** representation (e.g., red for danger zone and green for safe zone).

4. **Vehicle Behavior Simulation and Output System**:
   - **Green Vehicle**: This vehicle should continue **driving** if no pedestrian is detected within its danger zone. Simulate this by printing **"Green vehicle: driving..."** in the console, repeating every second or so, until a pedestrian is detected.
   - **Red Vehicle**: This vehicle should stop immediately when a pedestrian is detected within its danger zone. Simulate this by printing **"Red vehicle: danger detected, stopping."** when the pedestrian enters its danger zone.
   - **Green Vehicle Communication with Red Vehicle**: If the green vehicle detects a pedestrian in its danger zone, it should communicate with the red vehicle to signal it to stop as well. Simulate this by printing **"Green vehicle: stop"** in the console. The red vehicle will print **"Red vehicle: stop"** in response, simulating communication between the vehicles.

   The vehicles' movement is not represented on the plot. The primary focus is on **simulating the decision-making** and **communication** between the vehicles based on the pedestrian's proximity, with the status displayed in the **console output**. The behavior is updated dynamically as new data is retrieved.

   ### Example console output:
   - **Green vehicle**: "Driving..." (repeated every 1-2 seconds as it continues driving).
   - **Red vehicle**: "Driving..." (repeated until a pedestrian is detected).
   - When a pedestrian enters the danger zone:
     - **Red vehicle**: "Danger detected, stopping."
     - **Green vehicle**: "Stop."

5. **Visualization**:
   - The 2D plot should visualize the **vehicle** and **pedestrian** locations and their corresponding sizes.
   - The primary vehicle behavior and interactions are **displayed in the console logs**. The plot should remain focused on visualizing the current data (e.g., locations and dimensions of vehicles and pedestrians), without showing vehicle interaction messages.
   - The status of the vehicles (e.g., "driving", "danger detected", "stop") should be printed in the console to reflect their current behavior in response to pedestrian detection.

6. **Dynamic Updates**:
   - Implement a **button** (or similar mechanism) to **retrieve new data** and update the plot automatically. This will simulate **real-time updates** of the vehicle and pedestrian movements. The plot should show **vehicle and pedestrian positions** along with their **dimensions**, and the danger zone visualization should update accordingly as new data is retrieved.
---

### Submission Requirements:
- **Python Script** to retrieve data from the **CSV file** and implement vehicle and pedestrian logic.
- **Visualization** of car and pedestrian positions with dynamic updates (e.g., using **Matplotlib**, **Plotly**, or another visualization tool).
- **Danger Zone Detection**: Include the calculation of the danger zone around vehicles and a color-coded system indicating danger (e.g., red for danger zone).
- **Vehicle Behavior Simulation**: Include the logic for how the **green vehicle** and **red vehicle** respond to pedestrian proximity.
- **Outputs**: Print the vehicle statuses (e.g., "Green vehicle detected no danger and continues driving").

---

### Evaluation Criteria:

1. **Visualization**:
   - **Clarity** and **accuracy** of the 2D plot, including proper scaling of vehicles and pedestrians.
   - The **dynamic updating** of vehicle positions and danger zones.
   - **Labels**, **titles**, and **legend** inclusion for clarity.

2. **Danger Zone Calculation**:
   - The correctness of the **danger zone calculation** and its **visualization**.
   - Clear representation of the **danger zone** for each vehicle.

3. **Vehicle Logic**:
   - The accuracy of the **vehicle behavior simulation**:
     - Green vehicle continues driving when no pedestrian is nearby.
     - Red vehicle stops when a pedestrian is detected in its danger zone.
     - Green vehicle communicates with the red vehicle to stop when needed.

4. **Code Quality**:
   - The clarity and **organization** of the code. Proper **modularization** and clean coding practices.
---

### Challenges You Will Learn:
- **Data extraction** from a **CSV file**.
- **Real-time data visualization** with tools like **Matplotlib** or **Plotly**.
- **Spatial reasoning** and **safety analysis**.
- **Vehicle behavior simulation** in response to pedestrian danger zones.
- Basic principles of **collision avoidance** and **communication between vehicles** in autonomous systems.
