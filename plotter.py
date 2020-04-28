import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from mpl_toolkits.mplot3d import axes3d, Axes3D

class Plot:
    def __init__(self):
        self.x_data = [] # create all x points
        self.y_data = [] # Create all y points
        self.z_data = [] # Create all z points
        fig = plt.figure()
        self.ax = Axes3D(fig)
        plt.axis([-40, 40, -40, 40])
        anim = animation.FuncAnimation(fig, self.animate_frame, interval=100)
        plt.show()

    def animate_frame(self, r, theta, phi):
        x, y, z = self._sphere_to_cart_(r, theta, phi)
        self.x_data.append(x)
        self.y_data.append(y)
        self.z_data.append(z)
        self.ax.clear()
        self.ax.plot(x, y, z)

    def _sphere_to_cart_(self, r, theta, phi):
        x = r*math.sin(theta)*math.cos(phi)  # get x
        y = r*math.sin(theta)*math.sin(phi)  # get y
        z = r*math.cos(theta)  # get z
        return [x, y, z]  # return coord for point in cart


