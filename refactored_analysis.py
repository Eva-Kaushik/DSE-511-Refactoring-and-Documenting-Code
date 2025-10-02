# refactored_analysis.py
# Author: Eva Kaushik
# Date: 10/01/2025
# This script is my cleaned-up solution for Homework #5.
# Originally, the code was messy, so I broke it down into simple, bite-sized functions that anyone (including future me) can easily understand and work.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import logging
import unittest


# Step 1 & 2: Functions and Documentation 
# Broke down bad_python.py into modular functions for clarity and reusability alongwith I added clear docstrings for all functions defining purpose, inputs, outputs, and exceptions

# Setting up logging so I can track what script does without getting too much of print statements.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_average(numbers):
    """
    This function figures out the average of whatever numbers we give it.
    I use NumPy here because it handles all kinds of numeric inputs smoothly and quickly.

    Args:
        numbers (list, pd.Series, or np.ndarray): The numbers to average.

    Returns:
        float: The average value.


    Raises:
        ValueError: If we provide no input to work on.
        TypeError: If we provide an input which isn't a number.
    """
    if len(numbers) == 0:
        raise ValueError("Can't average an empty list!")
    
    numeric_array = np.array(numbers)
    if not np.issubdtype(numeric_array.dtype, np.number):
        raise TypeError("All values must be numeric, no strings or alphanumeric values allowed.")
    
    return np.mean(numeric_array)


def compute_std_dev(numbers, mean_value):
    """
    This one calculates how spread out our numbers are, using the population standard deviation formula.
    It needs the average first, which we already get from compute_average.

    Args:
        numbers (list, pd.Series, or np.ndarray): The numbers to check.
        mean_value (float): The average we've calculated beforehand.


    Returns:
        float: The standard deviation, showing how much variation exists.
    """
    if len(numbers) == 0:
        raise ValueError("Can't work with an empty list!")


    numeric_array = np.array(numbers)
    if not np.issubdtype(numeric_array.dtype, np.number):
        raise TypeError("All values must be numbers.")


    return np.sqrt(np.mean((numeric_array - mean_value) ** 2))



def sample_rows(dataframe, column_name, num_samples=5):
    """
    It attains a handful of random, unique values from one column so we can parse through our data quickly.

    Args:
        dataframe (pd.DataFrame): Our whole dataset.
        column_name (str): Which column we want to sample from.
        num_samples (int): How many random picks we want.


    Returns:
        list: The sampled values.
    """
    if column_name not in dataframe.columns:
        raise KeyError(f"Oops! No column named '{column_name}' here.")
    if len(dataframe) < num_samples:
        raise ValueError(f"Can't get {num_samples} samples; only {len(dataframe)} rows available.")


    random_indices = random.sample(range(len(dataframe)), num_samples)
    return [dataframe.iloc[i][column_name] for i in random_indices]



def plot_histogram(data_values, bins=10):
    """
    Shows a quick histogram so we can see how the numbers are spread out.

    Args:
        data_values (list, pd.Series, or np.ndarray): Numbers to plot.
        bins (int): Number of bars you want in your histogram.
    """
    plt.figure(figsize=(7, 4))
    plt.hist(data_values, bins=bins, color='skyblue', edgecolor='black')
    plt.title("Value distribution")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def run_analysis_pipeline(filename, sample_size=5, num_bins=10):
    """
    This is the main control function. It loads our data, computes averages and spread,
    makes a plot, and finally samples some random points so we can check-on the data a bit.

    Args:
        filename (str): Where our CSV file is located
        sample_size (int): How many random rows we want to check
        num_bins (int): How many bars for the histogram.

    Returns:
        dict: A summary with the average and standard deviation.
    """
    try:
        logging.info(f"Starting analysis for '{filename}'")
        source_df = pd.read_csv(filename)
    except FileNotFoundError:
        logging.error(f"Can't find the file '{filename}'. Check the path!")
        return None


    if "value" not in source_df.columns:
        raise KeyError("Our CSV needs a 'value' column for this to work.")


    values = source_df["value"].dropna()


    logging.info("Calculating average")
    mean_val = compute_average(values)
    logging.info(f"Average = {mean_val:.2f}")


    logging.info("Calculating standard deviation")
    std_dev_val = compute_std_dev(values, mean_val)
    logging.info(f"Std Dev = {std_dev_val:.2f}")


    logging.info("Plotting histogram")
    plot_histogram(values, bins=num_bins)


    logging.info(f"Sampling {sample_size} random values for a quick peek...")
    sampled_values = sample_rows(source_df, "value", sample_size)
    logging.info(f"Sampled values: {sampled_values}")


    logging.info("All done!")


    return {"average": mean_val, "std_deviation": std_dev_val}


#   Step 3 : Testing 
#  Added unittest.TestCase with multiple test cases for each function and Tests cover normal and edge cases, and type validation. This ensures robustness and easier debugging or future modifications


class TestMyAnalysisFunctions(unittest.TestCase):
    """
    I wrote these tests to double-check that my functions works well.
    I’m testing normal cases, edge cases (like empty lists),
    and incorrect input types to catch common failure checks.
    """

    def test_compute_average(self):
        self.assertAlmostEqual(compute_average([10, 20, 30]), 20.0)
        with self.assertRaises(ValueError):
            compute_average([])
        with self.assertRaises(TypeError):
            compute_average([1, "oops", 3])


    def test_compute_std_dev(self):
        self.assertAlmostEqual(compute_std_dev([1, 2, 3], 2.0), np.sqrt(np.mean((np.array([1, 2, 3]) - 2.0) ** 2)))
        with self.assertRaises(ValueError):
            compute_std_dev([], 0)
        with self.assertRaises(TypeError):
            compute_std_dev([1, "oops"], 1.5)


    def test_sample_rows(self):
        test_df = pd.DataFrame({"value": [10, 20, 30, 40, 50]})
        self.assertEqual(len(sample_rows(test_df, "value", 3)), 3)
        with self.assertRaises(KeyError):
            sample_rows(test_df, "wrong_column", 2)
        with self.assertRaises(ValueError):
            sample_rows(test_df, "value", 10)


# Step 4:
# Used logging for cleaner output management, avoided code duplication with helper functions, explicit error handling and meaningful exceptions


if __name__ == "__main__":
    relative_path_to_file = "./data.csv"
    results = run_analysis_pipeline(relative_path_to_file, sample_size=5, num_bins=12)

    if results:
        print("\n Analysis Summary")
        print(f"Average: {results['average']:.2f}")
        print(f"Standard Deviation: {results['std_deviation']:.2f}")


    print("\n Running Tests")
    unittest.main(argv=["first-arg-is-ignored"], exit=False)


"""
# Brief Steps: Homework 5  

# This refactored script successfully meets all the assignment goals:

# Step 1 and 2 (Functions and Documentation):
#   The original messy code was broken down into several focused functions like `compute_average`, `plot_histogram`, etc. Each one is now equipped 
#   with a clear docstring explaining its purpose, what it needs (Args), and what it gives back (Returns).

# Step 3 (Adding Tests):
#   I built a test suite using the `unittest` library. These tests check for correct outputs, proper error handling with empty lists, and how the
#   functions react to incorrect data types. This makes the code much more reliable.

# Step 4:
#   The complete working for this assignment is provided in a separate README.md file, which explains the "before and after" and the benefits of this new,
#   cleaner structure.
"""