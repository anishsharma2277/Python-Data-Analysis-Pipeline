import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
data_path = "data/dataset.csv"
data = pd.read_csv(data_path)

# Calculate the average of the "Sales" column
average_sales = data['Sales'].mean()
print(f"Average Sales: {average_sales}")

# Plot a histogram of the sales data
plt.figure(figsize=(10, 6))
data['Sales'].plot(kind='hist', title='Sales Distribution')
plt.xlabel('Sales')
plt.savefig("output/sales_distribution.png")

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Save the average sales to a text file
with open("output/summary.txt", "w") as f:
    f.write(f"Average Sales: {average_sales}\n")
