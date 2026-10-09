
import numpy as np

# ==================== Q1 ====================
# Basic operations on a 1D array

arr1 = np.array([10, 20, 30, 40, 50])

print("\nQ1. Basic Array Operations")
print("Original Array:", arr1)
print("Addition of 2:", arr1 + 2)
print("Multiplication by 3:", arr1 * 3)
print("Division by 2:", arr1 / 2)


# ==================== Q2(a) ====================
# Reverse a NumPy array

arr2 = np.array([1, 2, 3, 6, 4, 5])

print("\nQ2(a). Reverse Array")
print("Original Array:", arr2)
print("Reversed Array:", arr2[::-1])


# ==================== Q2(b)(i) ====================
# Most frequent value and its indices in x

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

values, counts = np.unique(x, return_counts=True)
max_count = np.max(counts)
most_frequent = values[counts == max_count]

print("\nQ2(b)(i). Most Frequent Value in x")
print("Most frequent value(s):", most_frequent)
print("Frequency:", max_count)

for value in most_frequent:
    print("Indices of", value, ":", np.where(x == value)[0])


# ==================== Q2(b)(ii) ====================
# Most frequent value and its indices in y

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

values, counts = np.unique(y, return_counts=True)
max_count = np.max(counts)
most_frequent = values[counts == max_count]

print("\nQ2(b)(ii). Most Frequent Value in y")
print("Most frequent value(s):", most_frequent)
print("Frequency:", max_count)

for value in most_frequent:
    print("Indices of", value, ":", np.where(y == value)[0])


# ==================== Q3 ====================
# Access elements using row and column indices

arr3 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nQ3. Accessing 2D Array Elements")
print("First row, second column:", arr3[0, 1])
print("Third row, first column:", arr3[2, 0])


# ==================== Q4 ====================
# Create 25 evenly spaced numbers from 10 to 100

Riddhi_Jain = np.linspace(10, 100, 25)

print("\nQ4. Linspace Array")
print("Array:", Riddhi_Jain)
print("Dimensions:", Riddhi_Jain.ndim)
print("Shape:", Riddhi_Jain.shape)
print("Total elements:", Riddhi_Jain.size)
print("Data type:", Riddhi_Jain.dtype)
print("Total bytes consumed:", Riddhi_Jain.nbytes)

# Transpose using reshape()
print("Transpose using reshape():\n",
      Riddhi_Jain.reshape(25, 1))

# Transpose using T attribute
print("Transpose using T:\n", Riddhi_Jain.T)


# ==================== Q5 ====================
# Create a 2D array with 3 rows and 4 columns

ucs420_Riddhi_Jain = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("\nQ5. Original Array")
print(ucs420_Riddhi_Jain)

# Statistical operations
print("Mean:", np.mean(ucs420_Riddhi_Jain))
print("Median:", np.median(ucs420_Riddhi_Jain))
print("Maximum:", np.max(ucs420_Riddhi_Jain))
print("Minimum:", np.min(ucs420_Riddhi_Jain))
print("Unique elements:", np.unique(ucs420_Riddhi_Jain))

# Reshape into 4 rows and 3 columns
reshaped_ucs420_Riddhi_Jain = ucs420_Riddhi_Jain.reshape(4, 3)

print("Reshaped Array (4 x 3):\n",
      reshaped_ucs420_Riddhi_Jain)

# Resize into 2 rows and 3 columns
resized_ucs420_Riddhi_Jain = np.resize(
    ucs420_Riddhi_Jain, (2, 3)
)

print("Resized Array (2 x 3):\n",
      resized_ucs420_Riddhi_Jain)

