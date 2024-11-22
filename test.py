import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Define the grid size
N, M = 20, 10

# Generate random points over the grid
points = np.random.choice([0, 1], size=(N, M))

# Define 4 periodic lines
y = np.linspace(0, M-1, M)
disp = np.arange(-2, 3)
#disp_rand = 
line1 = (N/5 + np., size=(M), seed=seed)) % N
line2 = (N/3 + np.random.choice([-2, -1, 0, 1, 2], size=(M), seed=seed)) % N
line3 = (N/2 + np.random.choice([0, 1, 2], size=(M), seed=seed)) % N
line4 = (N/1.5 + np.random.choice([0, 1, 2], size=(M), seed=seed)) % N

# Plot the grid and the periodic lines
plt.figure(figsize=(8, 8))
plt.imshow(points, cmap='Greys', interpolation='none', extent=[0, N-1, 0, M-1])
plt.plot(line1, y, label='Line 1', color='red')
plt.plot(line2, y, label='Line 2', color='blue')
plt.plot(line3, y, label='Line 3', color='green')
plt.plot(line4, y, label='Line 4', color='purple')
plt.legend()
plt.title('Periodic Lines and Random Points on Grid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.savefig('test.png')