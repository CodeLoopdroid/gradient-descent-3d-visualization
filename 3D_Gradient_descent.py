import numpy as np
import matplotlib.pyplot as plt

def z_function(x, y):
    return np.sin(x * 5) * np.cos(5 * y) / 5

def derivative(x, y):
    dz_dx = np.cos(x * 5) * np.cos(5 * y) * 5
    dz_dy = -np.sin(x * 5) * np.sin(5 * y) * 5
    return dz_dx, dz_dy

x_vals = np.arange(-1, 1, 0.05)
y_vals = np.arange(-1, 1, 0.05)
x, y = np.meshgrid(x_vals, y_vals)
z = z_function(x, y)

current_pos1 = (0.7, 0.4, z_function(0.7, 0.4))
current_pos2 = (0.5, 0.9, z_function(0.5, 0.9))
current_pos3 = (0.1, -1.0, z_function(0.1, -1.0))

learning_rate = 0.01
iterations = 500

fig = plt.figure()
ax = fig.add_subplot(projection="3d", computed_zorder=False)

for _ in range(iterations):
    dx1, dy1 = derivative(current_pos1[0], current_pos1[1])
    new_x1 = current_pos1[0] - learning_rate * dx1
    new_y1 = current_pos1[1] - learning_rate * dy1
    current_pos1 = (new_x1, new_y1, z_function(new_x1, new_y1))

    dx2, dy2 = derivative(current_pos2[0], current_pos2[1])
    new_x2 = current_pos2[0] - learning_rate * dx2
    new_y2 = current_pos2[1] - learning_rate * dy2
    current_pos2 = (new_x2, new_y2, z_function(new_x2, new_y2))

    dx3, dy3 = derivative(current_pos3[0], current_pos3[1])
    new_x3 = current_pos3[0] - learning_rate * dx3
    new_y3 = current_pos3[1] - learning_rate * dy3
    current_pos3 = (new_x3, new_y3, z_function(new_x3, new_y3))

    ax.plot_surface(x, y, z, cmap="viridis", zorder=0, alpha=0.7)
    ax.scatter(current_pos1[0], current_pos1[1], current_pos1[2], color="red", zorder=1)
    ax.scatter(current_pos2[0], current_pos2[1], current_pos2[2], color="yellow", zorder=1)
    ax.scatter(current_pos3[0], current_pos3[1], current_pos3[2], color="orange", zorder=1)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.pause(0.001)
    ax.clear()