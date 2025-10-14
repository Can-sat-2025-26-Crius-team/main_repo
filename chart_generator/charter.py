import time
import matplotlib.pyplot as plt
import numpy as np

# Time points (in minutes)
time = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 335])

# Energy usage (in mAh) for three stages
energy = np.array([20, 20, 20, 20, 20, 20, 150, 150, 150, 150, 150, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

# Plotting the energy usage line    
plt.plot(time, energy, marker='o', linestyle='-', color='red', label='Energy Usage')

# Shade the zones
plt.fill_between([0, 75], 0, 150, color='lightblue', alpha=0.3, label='Pre-Launch')
plt.fill_between([75, 165], 0, 150, color="#ff8800", alpha=0.3, label='Launch')
plt.fill_between([165, 320], 0, 150, color='lightgreen', alpha=0.3, label='Post-Launch')

# Add vertical lines for section boundaries
plt.axvline(x=75, color='blue', linestyle='--')
plt.axvline(x=165, color='blue', linestyle='--')
# plt.axvline(x=225, color='blue', linestyle='--')

# Labels and title
plt.xlabel('Time (min)')
plt.ylabel('Energy Usage (mAh)')
plt.title('Mission Energy Usage')
plt.grid(True)
plt.legend()

# Display
plt.show()