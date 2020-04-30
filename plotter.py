import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D
import json
import numpy as np


class Plot:
    """
    Clas for plotting using matplotlib, however, open3d is desirable as gpu rendering is much faster
    """
    def __init__(self):
        self.x_data = [] # create all x points
        self.y_data = [] # Create all y points
        self.z_data = [] # Create all z points
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)
        self.ax.set_xlabel("X AXIS")
        self.ax.set_ylabel("Y AXIS")
        self.ax.set_zlabel("Z AXIS")
        self.open_data() # Grab data from json
        # Convert to numpy array
        self.x_data = np.array(self.x_data)
        self.y_data = np.array(self.y_data)
        self.z_data = np.array(self.z_data)
        # Plot all data
        self.ax.scatter(self.x_data, self.y_data, self.z_data, s=1)
        # Show the final cloud
        plt.show()

    def open_data(self):
        """
        Retrieve data from json file
        """
        file_name = "scan_data/scan.json"
        with open(file_name, mode='r') as coords_json:
            data = json.load(coords_json)
            for point in data.keys():
                if int(point)%2==0:
                    coord = data.get(point)
                    self.x_data.append(coord[0])
                    self.y_data.append(coord[1])
                    self.z_data.append(coord[2])

