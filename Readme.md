# Homework 5: Refactoring and Documenting Code

I took a messy Python script (`bad_python.py`) and refactors it into a more modular, maintainable, and testable version. The refactored script read data.csv, computes summary statistics (mean and standard deviation), samples random rows, and visualizes the data in a histogram.

### What all changes I did in bad_python.csv

##### The original script entails:

1. Loaded the CSV directly without error handling.
2. Computed averages and standard deviations manually with loops.
3. Repeated logic (random sampling).
4. Had no functions, no comments, and no testing.

##### The refactored script now entails:

1. Uses modular functions with descriptive names (compute_average, compute_std_dev, sample_rows, plot_histogram, run_analysis).
2. Includes docstrings and inline comments for every function.
3. Adds error handling for empty inputs, wrong column names, and non-numeric data.
4. Uses NumPy for efficient math instead of manual loops.
5. Introduces logging for runtime clarity instead of raw print statements.
6. Adds unit tests with unittest to validate correctness and edge cases.

### How come the changes enhanced my code? 
All the changes make the code cleaner and easier to follow (readability), more reliable with clear error handling and tests, and reusable. Logging and modular design improved professionalism and maintainability, making it closer to standards.

### In what way I created data.csv? 
I generated a random dataset(id,value,category,date) with line 15 (value = 35.0) acting as a mild outlier to test standard deviation with sequential dates (lines 1–15) to keep the dataset analysis easy going.

### What exactly value dist. vs count histogram showcases? 
The histogram displays values from ~18 to 28, with counts reflecting repeated entries. We did automatic axis scaling, which focuses on the main data distribution.

### This submission covers all required steps of assignment completion:

1. Step 1: Chose the messy provided script (bad_python.csv)
2. Step 2: Refactored into modular functions with comments/docstrings.
3. Step 3: Added unit tests for both normal and error cases.
4. Step 4: Added README.md file for documentation and reproducibility.

