
import numpy as np

# ============================================================
# Q1. Sensor Readings and Vectorization
# ============================================================

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

# (a) Add +2°C measurement error using vectorization
corrected_temperature = temperature + 2
print("\nQ1(a). Corrected Temperatures:", corrected_temperature)

# (b) Convert Celsius to Fahrenheit
fahrenheit = (9 / 5) * temperature + 32
print("Q1(b). Temperatures in Fahrenheit:", fahrenheit)

# (c) Identify readings greater than 32°C
readings_above_32 = temperature[temperature > 32]
print("Q1(c). Readings above 32°C:", readings_above_32)

# (d) Count readings exceeding 32°C
count = np.sum(temperature > 32)
print("Q1(d). Count above 32°C:", count)

# (e) Explanation:
# Vectorization performs operations on entire arrays without
# explicit Python loops. Boolean indexing selects elements
# satisfying a condition efficiently.


# ============================================================
# Q2. Daily Steps Matrix
# ============================================================

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

# (a) Total steps recorded
print("\nQ2(a). Total Steps:", np.sum(steps))

# (b) Mean number of steps
print("Q2(b). Mean Steps:", np.mean(steps))

# (c) Maximum and minimum
print("Q2(c). Maximum Steps:", np.max(steps))
print("Q2(c). Minimum Steps:", np.min(steps))

# (d) Total steps for each day (axis=0)
print("Q2(d). Total Steps per Day:", np.sum(steps, axis=0))

# (e) Total steps for each user (axis=1)
print("Q2(e). Total Steps per User:", np.sum(steps, axis=1))

# (f) Position of maximum using argmax()
max_index = np.argmax(steps)
position = np.unravel_index(max_index, steps.shape)

print("Q2(f). Maximum Value Position (row, column):", position)
print("Maximum Steps:", steps[position])


# ============================================================
# Q3. Slicing, Copying, Reshaping, Flattening and Raveling
# ============================================================

# (a) Create original array
original = np.array([1, 2, 3, 4, 5, 6])

# (b) Slice from index 1 to 4 (index 4 excluded)
subset = original[1:4]

# (c) Modify subset
subset[0] = 999
print("\nQ3(c). Original after modifying subset:", original)
print("Subset:", subset)

# (d) Create an independent copy and modify it
copied_array = original[1:4].copy()
copied_array[0] = 500

print("Q3(d). Original after modifying copy:", original)
print("Copied Array:", copied_array)

# (e) Create numbers 1 to 12 and reshape into 3x4 matrix
matrix = np.arange(1, 13).reshape(3, 4)
print("\nQ3(e). 3x4 Matrix:\n", matrix)

# (f) Indexing and slicing
print("Q3(f). First Row:", matrix[0, :])
print("Last Row:", matrix[-1, :])
print("Second Column:", matrix[:, 1])
print("Rows 1-2, Columns 2-3:\n", matrix[1:3, 2:4])

# (g) Flatten using flatten() and ravel()
flat_array = matrix.flatten()
ravel_array = matrix.ravel()

print("Q3(g). Flatten:", flat_array)
print("Ravel:", ravel_array)

# (h) Modify ravel output
ravel_array[0] = 100
print("Q3(h). Matrix after modifying ravel:\n", matrix)
print("Ravel Array:", ravel_array)

# (i) Modify flatten output
flat_array[1] = 200
print("Q3(i). Matrix after modifying flatten:\n", matrix)
print("Flatten Array:", flat_array)

# (j) Matrix properties
print("Q3(j). Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Total Elements:", matrix.size)
print("Data Type:", matrix.dtype)


# ============================================================
# Q4. Cognitive-Assistive System: Ordinary Least Squares
# ============================================================

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

# (a) Shape and dimensions
print("\nQ4(a). Shape of X:", X.shape)
print("Dimensions of X:", X.ndim)

# (b) Transpose
print("Q4(b). X Transpose:\n", X.T)

# (c) Matrix product X.T @ X
XtX = X.T @ X
print("Q4(c). X.T @ X:\n", XtX)

# (d) Inverse of X.T @ X
inverse = np.linalg.inv(XtX)
print("Q4(d). Inverse of X.T @ X:\n", inverse)

# (e) Ordinary Least Squares:
# beta = (X.T @ X)^(-1) @ X.T @ y
beta = inverse @ X.T @ y
print("Q4(e). Regression Coefficients:", beta)

# (f) Explanation:
# beta[0] = coefficient for sleep hours
# beta[1] = coefficient for activity level
# beta[2] = coefficient for stress level
# Each coefficient estimates the change in predicted score
# per unit increase in that feature, holding others constant.

# (g) Predict score for a new user
new_user = np.array([5, 40, 7])
predicted_score = new_user @ beta

print("Q4(g). Predicted Assistance Score:", predicted_score)

