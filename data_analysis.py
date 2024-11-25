import pandas as pd
import numpy as np

# Load a CSV file
file_path = input("Enter the path to your CSV file: ")
try:
    data = pd.read_csv(file_path)
    print("CSV Data loaded successfully!")
    print(data.head())  # Display the first few rows to ensure it's read correctly
except Exception as e:
    print(f"Error reading the file: {e}")

# Perform basic analysis
print("Basic Statistics:")
print(data.describe())

print("\nMean of each column:")
print(data.mean())

print("\nMedian of each column:")
print(data.median())

print("\nMode of each column:")
print(data.mode().iloc[0])

# Save a summary to a new file
output_path = "summary.csv"  # This is where the summary will be saved
data.describe().to_csv(output_path)  # Saving the summary as CSV
print(f"\nSummary saved to {output_path}")


