import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('chart_generator.py')

# Assuming CSV has 'x' and 'y' columns
plt.plot(df['x'], df['y'], marker='o')

# Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple CSV Plot')

# # Display the plot
# plt.grid(True)
# plt.show()