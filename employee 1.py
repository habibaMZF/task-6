import numpy as np

# Create Arrays
A = np.array([10, 20, 30, 40, 50])          # Ages
B = np.array([5, 4, 3, 2, 1])  # Salaries

# Perform Operations
print("A + B =", A + B)
print("A - B =", A - B)
print("A * B =", A * B)
print("A / B =", A / B)

# NumPy Functions
print("Mean of A =", np.mean(A))
print("Max of A =", np.max(A))
print("Min of A =", np.min(A))

# Dot Product
print("Dot Product of A and B =", np.dot(A, B))

# Reshape A to 5x1
A_reshaped = A.reshape(5, 1)
print("Reshaped A:")
print(A_reshaped)