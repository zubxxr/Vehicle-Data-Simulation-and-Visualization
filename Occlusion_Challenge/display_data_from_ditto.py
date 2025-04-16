import requests
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Ditto URL and authentication
thingsURL = "http://localhost:8080/api/2/things/"
auth = ("ditto", "ditto")
thingID = 'org.otu:occlusion-data'  # Ensure the Thing ID is correct

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

# Function to update the plot with coordinates and sizes
def update_plot():
    # Fetch coordinates (accessing the nested data)
    car1_location = get_feature_value_from_ditto(thingID, "Car1_Location") or {'X': 0, 'Y': 0}
    car2_location = get_feature_value_from_ditto(thingID, "Car2_Location") or {'X': 0, 'Y': 0}
    pedestrian_location = get_feature_value_from_ditto(thingID, "Pedestrian_Location") or {'X': 0, 'Y': 0}

    # Extract the X, Y coordinates from the nested data
    car1_x = car1_location.get('X', 0)
    car1_y = car1_location.get('Y', 0)

    car2_x = car2_location.get('X', 0)
    car2_y = car2_location.get('Y', 0)

    pedestrian_x = pedestrian_location.get('X', 0)
    pedestrian_y = pedestrian_location.get('Y', 0)

    # Fetch the dimensions (Length, Width) from Ditto
    car1_length = get_feature_value_from_ditto(thingID, "Car1_Length") or 4.5  # Default values if not found
    car1_width = get_feature_value_from_ditto(thingID, "Car1_Width") or 2.0

    car2_length = get_feature_value_from_ditto(thingID, "Car2_Length") or 4.7
    car2_width = get_feature_value_from_ditto(thingID, "Car2_Width") or 2.2

    pedestrian_length = get_feature_value_from_ditto(thingID, "Pedestrian_Length") or 1.2
    pedestrian_width = get_feature_value_from_ditto(thingID, "Pedestrian_Width") or 0.5

    print(f"Car1 Location: ({car1_x}, {car1_y})")
    print(f"Car2 Location: ({car2_x}, {car2_y})")
    print(f"Pedestrian Location: ({pedestrian_x}, {pedestrian_y})")
    print(f"Car1 Size: Length={car1_length}, Width={car1_width}")
    print(f"Car2 Size: Length={car2_length}, Width={car2_width}")
    print(f"Pedestrian Size: Length={pedestrian_length}, Width={pedestrian_width}")

    # Clear the previous plot
    ax.clear()
    
    # Plot new data
    ax.plot(car1_x, car1_y, 'ro', label='Car 1 Location')
    ax.plot(car2_x, car2_y, 'go', label='Car 2 Location')
    ax.plot(pedestrian_x, pedestrian_y, 'bs', label='Pedestrian Location')

    # Plot solid rectangles for Car1, Car2, and Pedestrian using the length and width
    ax.add_patch(plt.Rectangle((car1_x - car1_width / 2, car1_y - car1_length / 2), car1_width, car1_length, linewidth=1, edgecolor='r', facecolor='red', label='Car 1 Size'))
    ax.add_patch(plt.Rectangle((car2_x - car2_width / 2, car2_y - car2_length / 2), car2_width, car2_length, linewidth=1, edgecolor='g', facecolor='green', label='Car 2 Size'))
    ax.add_patch(plt.Rectangle((pedestrian_x - pedestrian_width / 2, pedestrian_y - pedestrian_length / 2), pedestrian_width, pedestrian_length, linewidth=1, edgecolor='b', facecolor='blue', label='Pedestrian Size'))

    # Set labels and title
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Bird\'s Eye View: Car and Pedestrian Locations')
    ax.legend()
    ax.grid(True)

    # Set axis limits with padding
    padding = 10
    x_min = min(car1_x, car2_x, pedestrian_x) - padding
    x_max = max(car1_x, car2_x, pedestrian_x) + padding
    y_min = min(car1_y, car2_y, pedestrian_y) - padding
    y_max = max(car1_y, car2_y, pedestrian_y) + padding

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # Redraw the canvas
    canvas.draw()

# Tkinter window setup
window = tk.Tk()
window.title("Vehicle and Pedestrian Location Viewer")

# Create the matplotlib figure and axes
fig, ax = plt.subplots(figsize=(6, 6))

# Create a canvas widget to display the plot in Tkinter
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

# Add a "Next" button to navigate to the next set of locations
next_button = tk.Button(window, text="Next", command=update_plot)
next_button.pack()

# Initialize the plot with the first data set
update_plot()

# Run the Tkinter event loop
window.mainloop()
