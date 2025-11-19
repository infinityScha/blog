# step 1: definition of the space

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import qmc

# Set the random seed for reproducibility
np.random.seed(42)

# Define the grid size
N, M = 500, 50

# Generate uniformly distributed points using Poisson Disk Sampling
sampler = qmc.PoissonDisk(d=2, radius=0.05, seed=42)
points = sampler.fill_space()
X, Y = points[:, 0], points[:, 1]
X = (X * N).astype(int)
Y = (Y * M).astype(int)

# Define 4 periodic lines
y = np.linspace(0, M-1, M)
disp = np.arange(-N/100, N/100)

def wave(y, A, B, C):
    return np.array(A * np.sin(2*np.pi*(y + B)/M) + C, dtype=int)

line1 = (wave(y, N/25, 0.0, N/10) + np.random.choice(disp, size=M)) % N
line2 = (wave(y, N/20, 0.2*M, N/4) + np.random.choice(disp, size=M)) % N
line3 = (wave(y, N/15, 0.7*M, N/2) + np.random.choice(disp, size=M)) % N
line4 = (wave(y, N/10, 0.5*M, N/1.2) + np.random.choice(disp, size=M)) % N

# check that none of the points overlap with the lines, if a point does overlap, remove it
for i in range(len(X)):
    if X[i] in [line1[Y[i]], line2[Y[i]], line3[Y[i]], line4[Y[i]]]:
        X[i] = -1

# remove the marked points
Y = Y[X != -1]
X = X[X != -1]

# Plot the grid and the periodic lines using scatter
plt.figure(figsize=(5, 3))
plt.scatter(X, Y, label='Random Points', color='black', s=30, edgecolors='black', linewidth=0.5)
plt.scatter(line1, y, label='Line 1', color='tab:red', s=30, edgecolors='black', linewidth=0.5)
plt.scatter(line2, y, label='Line 2', color='tab:blue', s=15, edgecolors='black', linewidth=0.5)
plt.scatter(line3, y, label='Line 3', color='tab:green', s=15, edgecolors='black', linewidth=0.5)
plt.scatter(line4, y, label='Line 4', color='tab:orange', s=15, edgecolors='black', linewidth=0.5)

# Customize the x and y limits
plt.xlim(0, N-1)
plt.ylim(0, M-1)

# Set the title and labels
plt.xlabel('X', fontsize=14, fontweight='bold')
plt.ylabel('Y', fontsize=14, fontweight='bold')

# Customize the grid and ticks
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the figure with improved layout
plt.tight_layout()
plt.savefig('test_scatter_profeat.png', dpi=300)

plt.close()

# step 2: painting the zebra based on parity 
from sympy.combinatorics import Permutation

def find_parity(X,Y,*lines):
    # make the required permutations
    temp = np.vstack([X,np.vstack([line[Y] for line in lines])]).T

    # argsort each row to get the permutation
    permutations = np.argsort(temp, axis=1)

    # find the parity of each permutation
    parities = np.array([Permutation(p).parity() for p in permutations])

    return parities

parities = find_parity(X,Y,line1,line2,line3,line4)

# color the points based on the parity
plt.figure(figsize=(5, 3))

plt.scatter(X[parities == 0], Y[parities == 0], label='Even Parity', color='blue', s=30, edgecolors='black', linewidth=0.5)
plt.scatter(X[parities == 1], Y[parities == 1], label='Odd Parity', color='red', s=30, edgecolors='black', linewidth=0.5)
plt.scatter(line1, y, label='Line 1', color='tab:red', s=15, edgecolors='black', linewidth=0.5)
plt.scatter(line2, y, label='Line 2', color='tab:blue', s=15, edgecolors='black', linewidth=0.5)
plt.scatter(line3, y, label='Line 3', color='tab:green', s=15, edgecolors='black', linewidth=0.5)
plt.scatter(line4, y, label='Line 4', color='tab:orange', s=15, edgecolors='black', linewidth=0.5)

# Set the title and labels
plt.xlabel('X', fontsize=14, fontweight='bold')
plt.ylabel('Y', fontsize=14, fontweight='bold')

# Customize the x and y limits
plt.xlim(0, N-1)
plt.ylim(0, M-1)

# Customize the grid and ticks
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the figure with improved layout
plt.tight_layout()
plt.savefig('test_scatter_profeat_2.png', dpi=300)

plt.close()

# step 3: show at it works under shift through the periodic boundary

# Define the shift
shifts = np.array([N//4, N//2, 3*N//4])

for shift in shifts:
    # Shift the points and lines
    X_shifted = (X + shift) % N
    line1_shifted = (line1 + shift) % N
    line2_shifted = (line2 + shift) % N
    line3_shifted = (line3 + shift) % N
    line4_shifted = (line4 + shift) % N
    # Find the parity of the shifted points
    parities_shifted = find_parity(X_shifted, Y, line1_shifted, line2_shifted, line3_shifted, line4_shifted)
    # Plot the shifted points and lines
    plt.figure(figsize=(5, 3))
    plt.scatter(X_shifted[parities_shifted == 0], Y[parities_shifted == 0], label='Even Parity', color='blue', s=30, edgecolors='black', linewidth=0.5)
    plt.scatter(X_shifted[parities_shifted == 1], Y[parities_shifted == 1], label='Odd Parity', color='red', s=30, edgecolors='black', linewidth=0.5)
    plt.scatter(line1_shifted, y, label='Line 1', color='tab:red', s=15, edgecolors='black', linewidth=0.5)
    plt.scatter(line2_shifted, y, label='Line 2', color='tab:blue', s=15, edgecolors='black', linewidth=0.5)
    plt.scatter(line3_shifted, y, label='Line 3', color='tab:green', s=15, edgecolors='black', linewidth=0.5)
    plt.scatter(line4_shifted, y, label='Line 4', color='tab:orange', s=15, edgecolors='black', linewidth=0.5)
    # Set the title and labels
    plt.title(f'Shifted X by {shift}', fontsize=16, fontweight='bold')
    plt.xlabel('X', fontsize=14, fontweight='bold')
    plt.ylabel('Y', fontsize=14, fontweight='bold')
    # Customize the x and y limits
    plt.xlim(0, N-1)
    plt.ylim(0, M-1)
    # Customize the grid and ticks
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    # Save the figure with improved layout
    plt.tight_layout()
    plt.savefig(f'test_scatter_profeat_shifted_{shift}.png', dpi=300)
    plt.close()