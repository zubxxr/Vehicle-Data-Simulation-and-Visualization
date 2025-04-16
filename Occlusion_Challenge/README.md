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
     ![image](https://github.com/user-attachments/assets/142801e5-a8d0-4d7f-97f8-b61c277c34ba)

 4. **Open Ditto**
    - In Ditto, you will see the values being updated in real-time.
      ![image](https://github.com/user-attachments/assets/7891203e-e545-46cc-a353-c2ed6ed17922)

## Challenge

### Steps:

1. **Data Retrieval**:
   - Write a script to **retrieve real-time data** from **Ditto** using the provided Python script.
   - The data includes:
     - **Car 1 and Car 2 locations (X, Y)**
     - **Pedestrian location (X, Y)**
     - **Car dimensions (Length, Width)**
     - **Pedestrian dimensions (Length, Width)**
     - **Image URLs (OccludedImage, OccludingCar, GroundTruthView)**

2. **Bird's Eye View Visualization**:
   - Once the data is retrieved, you will **visualize** it on a **2D plot** using **Matplotlib** or **Plotly**.
   - Each **vehicle** (Car 1, Car 2) will be represented as a **rectangle**, sized based on the **vehicle's length and width**.
   - The **pedestrian** will be represented as a **rectangle**, sized based on the **pedestrian's length and width**.
   - The plot will be updated dynamically with each new data set, simulating vehicle and pedestrian movement.
   - **Axis labels**: Add **"X Coordinate"** and **"Y Coordinate"** labels, and **title** for the plot.

3. **Safety Evaluation (Optional)**:
   - Once you visualize the data, you can **evaluate the safety** of pedestrian placement. Ensure the pedestrian is not too close to any vehicle by calculating the **distance** between the pedestrian and the vehicles. You can implement a simple check:
     - If the pedestrian's position is within a certain **threshold distance** (e.g., 1.5 times the vehicle's width), mark the pedestrian as in a **danger zone**.
   - If necessary, you could write a function to **alert** when a pedestrian is in the danger zone or implement a color-coded system where:
     - **Green** indicates safe, and
     - **Red** indicates danger.

4. **Next Steps**:
   - **Dynamic Updates**: Once you have successfully visualized the data, implement a **button** (or similar mechanism) to retrieve **new data** and update the plot automatically. This will simulate **real-time updates** of the vehicle and pedestrian movements.
   - **Optimize Placement** (Optional): Based on the vehicle and pedestrian placements, try to **rearrange** the vehicles or pedestrians for **optimal safety** and **distance management**. Adjust positions to ensure that no collisions or safety breaches happen.

### Submission Requirements:
- **Script** to retrieve data from **Ditto**.
- **Visualization** of car and pedestrian positions. Students are free to use any visualization tool or library they prefer, such as **Matplotlib**, **Plotly**, **Pygame**, or even other interactive tools. The key is to dynamically display the data with proper scaling and labels.
- (Optional) **Safety analysis** and color-coded alerts indicating danger zones.
- (Optional) **Code for optimizing placement** or making adjustments based on safety rules.

### Evaluation Criteria:
1. **Data Handling**:
   - How well students handle **retrieving** and **processing** the data from **Ditto**.
2. **Visualization**:
   - The clarity and **accuracy** of the 2D plot, including proper scaling of vehicle and pedestrian dimensions.
   - The inclusion of **axis labels**, **title**, and **legend**.
3. **Safety Evaluation (Optional)**:
   - The logic used to determine whether a pedestrian is in a **danger zone** and how it is visualized on the plot.
4. **Interactivity** (Bonus):
   - How well the plot **updates dynamically** with new data and how intuitive the user interface is.
5. **Optimization** (Bonus):
   - How well the vehicles and pedestrians are rearranged to maximize safety or **optimize placement**.

### Challenges You Will Learn:
- **Data extraction** from a **digital twin** (Ditto).
- **Real-time data visualization** with tools like **Matplotlib** or **Plotly**.
- **Spatial reasoning** and **safety analysis**.
- Basic principles of **collision avoidance** in a simulated environment.
- **Optimizing placement** for safety in dynamic simulations.
