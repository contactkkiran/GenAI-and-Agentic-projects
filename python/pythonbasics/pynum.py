import numpy as np

# ============================================================
# TOPIC 1: NumPy 1D Array — Salary Operations
# NumPy applies math to every element at once (vectorized),
# no loop needed. Ideal for large datasets in ML/AI.
# ============================================================
salaries = np.array([10000, 20000, 30000, 40000, 50000])
print("Original salaries:", salaries)
# Give 15% hike
newsalaries = salaries * 1.15
print("New salaries after 15% hike:", newsalaries)
# Calculate the average of the new salaries
print("Average of new salaries:", newsalaries.mean() / len(newsalaries))
# Calulate highest salary
print("Highest salary:", newsalaries.max())
# Calculate the lowest salary
print("Lowest salary:", newsalaries.min())

# ============================================================
# TOPIC 2: Input Validation Before Creating NumPy Array
# Always validate raw data before converting to np.ndarray.
# Prevents silent errors during model training in ML/AI.
# ============================================================

from typing import List, Optional


def validate_all_nonzero(data: List[List[int]]) -> bool:
    """
    Check if all elements in a 2D list are non-zero before NumPy conversion.

    Args:
        data: 2D list of integers to validate

    Returns:
        True if all elements are non-zero, False otherwise
    """
    return all(element != 0 for row in data for element in row)


def safe_create_array(data: List[List[int]]) -> Optional[np.ndarray]:
    """
    Create NumPy array only if all elements are non-zero.

    Args:
        data: 2D list to convert

    Returns:
        np.ndarray if valid, None if zeros found
    """
    if not validate_all_nonzero(data):
        print("Error: Matrix contains zero. Cannot create array.")
        return None

    return np.array(data)


def main_validation() -> None:
    """Validation demo."""
    raw_data = [[1, 2], [3, 4]]  # Change to [[1, 0], [3, 4]] to test the else case

    print(f"Raw data: {raw_data}")

    sample_matrix = safe_create_array(raw_data)

    if sample_matrix is not None:
        print(f"Matrix created successfully:\n{sample_matrix}")
        print(f"Shape: {sample_matrix.shape}")
        print("All elements confirmed non-zero before access")
    else:
        print("Matrix creation aborted due to zeros")


main_validation()

# ============================================================
# TOPIC 3: 2D Array (Matrix) — Shape & Dimensions
# shape → (rows, cols)   ndim → number of dimensions
# Used in ML to verify input tensor sizes before training.
# ============================================================
# Create a 2D Array (Matrix)
A = np.array([[1, 2], [3, 4]])
print("2D Array (Matrix):", A.shape)
print("2D Array (Dimensions):", A.ndim)

# ============================================================
# TOPIC 3: Accessing Elements, Rows & Columns
# A[row][col] — zero-indexed
# A[row]    → full row
# A[:, col] → full column (: = all rows)
# ============================================================
# Access Elements

print("\nAccess Elements:")
print("A[0][0] =", A[0][0])
print("A[0][1] =", A[0][1])
print("A[1][0] =", A[1][0])
print("A[1][1] =", A[1][1])
# Accessing first row
print("First row of the matrix:", A[0])
# Accessing second row
print("Second row of the matrix:", A[1])
# Accessing first column
print("First column of the matrix:", A[:, 0])
# Accessing second column
print("Second column of the matrix:", A[:, 1])

# ============================================================
# TOPIC 4: Aggregate Operations — sum, mean, max, min
# Used in ML for loss calculation, normalization & statistics.
# ============================================================
# Sum of all elements in the matrix
print("Sum of all elements in the matrix:", A.sum())
# Mean (Average)

print("\nMean:")

print(A.mean())

# Maximum Value

print("\nMaximum:")

print(A.max())

# Minimum Value

print("\nMinimum:")

print(A.min())

# ============================================================
# TOPIC 5: Second Matrix B — Access & Stats
# ============================================================
B = np.array([[5, 6], [7, 8]])
print(B)
print(B[0][0])
print(B[1][1])
print(B[:, 0])
print(B.shape)
print(B.mean())

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# ============================================================
# TOPIC 6: Element-wise vs Matrix Multiplication
# A + B  → adds matching elements (element-wise)
# A * B  → multiplies matching elements (element-wise)
# A @ B  → true matrix multiplication (dot product)
#           used in neural network layer computations
# ============================================================
# Element-wise addition and multiplication
print(A + B)
print(A * B)

# Matrix Wise multiplication
print("Matrix Wise multiplication:", A @ B)

# ============================================================
# TOPIC 7: 1D Array — Mean
# ============================================================
arr = np.array([1, 2, 3, 4])

print(arr.mean())


A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# ============================================================
# TOPIC 8: Matrix Multiplication Result Verification
# A @ B = [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]]
#       = [[19, 22], [43, 50]]
# ============================================================
print(A @ B)

