import matplotlib.pyplot as plt

# Define the number of circles
num_circles = 5

# Create a new figure
fig, ax = plt.subplots()

# Draw each circle
for i in range(num_circles, 0, -1):
    circle = plt.Circle((0.5, 0.5), i*0.1, fill=False)
    ax.add_artist(circle)

# Set limits and aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Display the plot
plt.show()
