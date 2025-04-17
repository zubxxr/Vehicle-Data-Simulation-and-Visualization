# Occlusion Challenge: Visualizing and Evaluating Vehicle-Pedestrian Data

## Objective
The goal of this challenge is to visualize the positions of vehicles and pedestrians in a 2D bird's eye view format, based on real-time data extracted from Ditto. You will be tasked with representing car locations, pedestrian positions, and their dimensions (length, width) on a simple 2D plot. You will then assess whether these objects are too close to each other, making sure the system accounts for safety and spatial relationships.

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

3. **Retreive Data from the Kuksa and Send it to Ditto**
   - Open a new terminal and run the code.
     ```bash 
     cd ~/kuksa-databroker/Occlusion_Challenge
     source ../kuksa-ditto/venv/bin/activate
     python3 send_data_to_ditto.py
     ```
     ![image](https://github.com/user-attachments/assets/c40f57cc-d069-4da9-8a2b-9a8f99b970a0)

4. **Open Ditto**
    - In Ditto, you will see the values being updated in real-time.
      ![image](https://github.com/user-attachments/assets/7568e53f-642d-4b65-9ca5-2433c680b12f)

5. **Retreive the data from Ditto and save it to a local CSV file**
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
   - Each **vehicle** (Car 1, Car 2) will be represented as a **rectangle**, sized based on the **vehicle's length and width**.
   - The **pedestrian** will be represented as a **rectangle** or **circle**, sized based on the **pedestrian's length and width**.
   - The plot should include a `next` button, which will go to the next record in the database.
   - **Axis labels**: Add **"X Coordinate"** and **"Y Coordinate"** labels, and a **title** for the plot.

3. **Danger Zone Calculation**:
   - Calculate the **danger zone** around each vehicle based on a **threshold distance** (e.g., 1.5 times the vehicle's width).
   - **Determine whether a pedestrian is inside the danger zone**. If the pedestrian is within this range, the vehicle should take action (e.g., stop or alert).
   - The danger zone for each vehicle should be visualized, with a **color-coded** representation (e.g., red for danger zone and green for safe zone).

4. **Vehicle Behavior Simulation**:
   - **Green Vehicle**: This vehicle should continue driving if no pedestrian is detected within the danger zone.
   - **Red Vehicle**: This vehicle should **stop immediately** when a pedestrian is detected within its danger zone.
   - **Green Vehicle Communication with Red Vehicle**: If the green vehicle detects a pedestrian in its danger zone, it should **communicate** with the red vehicle to signal it to stop as well. This can be simulated by changing the red vehicle's state to stopped when the green vehicle detects the pedestrian.

5. **Output and Alert System**:
   - Display or print the **status** of the vehicles based on the detection of pedestrians and danger zones. For example:
     - **Green vehicle**: "No pedestrian detected, continuing driving."
     - **Red vehicle**: "Pedestrian detected, stopping."
     - **Green vehicle communication**: "Green vehicle detects pedestrian, red vehicle stops."
   - Output this status to the console or display in the visualization for clarity.

6. **Dynamic Updates**:
   - Implement a **button** (or similar mechanism) to **retrieve new data** and update the plot automatically. This will simulate **real-time updates** of the vehicle and pedestrian movements, with the status and danger zones being updated.
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

3. **Danger Zone Calculation**:
   - The correctness of the **danger zone calculation** and its **visualization**.
   - Clear representation of the **danger zone** for each vehicle.

4. **Vehicle Logic**:
   - The accuracy of the **vehicle behavior simulation**:
     - Green vehicle continues driving when no pedestrian is nearby.
     - Red vehicle stops when a pedestrian is detected in its danger zone.
     - Green vehicle communicates with the red vehicle to stop when needed.

5. **Interactivity** (Bonus):
   - How well the plot **updates dynamically** with new data.
   - The user interface's responsiveness and intuitiveness (e.g., button or automated updates).

6. **Code Quality**:
   - The clarity and **organization** of the code. Proper **modularization** and clean coding practices.

7. **Creativity** (Bonus):
   - Additional features such as **alerts**, **animations**, or **improving the user interface**.
   - Any **extra logic** to handle more complex scenarios (e.g., multiple pedestrians, multiple vehicles).

---

### Challenges You Will Learn:
- **Data extraction** from a **CSV file**.
- **Real-time data visualization** with tools like **Matplotlib** or **Plotly**.
- **Spatial reasoning** and **safety analysis**.
- **Vehicle behavior simulation** in response to pedestrian danger zones.
- Basic principles of **collision avoidance** and **communication between vehicles** in autonomous systems.
