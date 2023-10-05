import random
import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd

# Create a tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Step 1: Open a file dialog for the user to pick a CSV file
file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

if not file_path:
    print("No file selected. Exiting.")
else:
    # Step 2: Read the CSV into a DataFrame
    df = pd.read_csv(file_path)

    # Step 3: Get the number of rows in the DataFrame
    num_rows = len(df)

    # Step 4: Loop through rows and print a single random value from the entire DataFrame
    for i in range(num_rows):
        random_row = random.randint(0, num_rows - 1)
        random_col = random.choice(df.columns)
        random_value = df.loc[random_row, random_col]
        print(f"Method: Print Random Value from DataFrame - [Row {i + 1}, Random Column '{random_col}']: {random_value}")

    # Step 5: Loop through rows and print a random sample of rows using .sample()
    for i in range(num_rows):
        random_sample = df.sample(n=1)
        random_row = random_sample.iloc[0].to_string(index=False)
        print(f"Method: Print Random Row Sample - [Row {i + 1}, Random Row Sample]: {random_row}")

    # Step 6: Loop through rows and print random values from column 3
    col_name = df.columns[2]  # Assuming column 3 is the third column (index 2)
    for i in range(num_rows):
        random_row = random.randint(0, num_rows - 1)
        random_value = df.iloc[random_row][col_name]
        print(f"Method: Print Random Value from Column 3 - [Row {i + 1}, Column 3]: {random_value}")

    # Step 7: Loop through rows and print random values generated from a normal distribution
    for i in range(num_rows):
        random_value = np.random.normal()  # Generates a random number from a normal distribution
        print(f"Method: Generate Random Value from Normal Distribution - [Row {i + 1}, Normal Distribution]: {random_value}")
