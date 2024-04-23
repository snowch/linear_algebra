

### Pivots

#### Two Fundamental Questions.

When we encounter a linear system, we often ask:

- **Existence**: Is there a solution to the linear system? If so, we say that the system is consistent; if not, we say it is inconsistent.
- **Uniqueness**: If the linear system is consistent, is the solution unique or are there infinitely many solutions?

> **Definition 1.4.1**.  A pivot position in a matrix $A$ is the position of a leading entry in the reduced row echelon matrix of $A$.

**Sympy** [docs](https://docs.sympy.org/latest/modules/matrices/matrices.html)
```python
from sympy import Matrix
from sympy.abc import x
m = Matrix([[1, 2], [x, 1 - 1/x]])

rref_matrix, rref_pivots = m.rref()

rref_matrix
# Matrix([
# [1, 0],
# [0, 1]])

rref_pivots
# (0, 1) # tuple of pivot columns
```

#### The existence of solutions

> **Proposition 1.4.3.**  A linear system is inconsistent if and only if there is a pivot position in the rightmost column of the corresponding augmented matrix.

```python
from sympy import Matrix

def is_consistent_augmented(augmented_matrix):
    # Convert the augmented matrix to row echelon form (REF)
    rref_matrix, pivot_columns = augmented_matrix.rref()
    
    # Check if there is a pivot position in the rightmost column
    num_rows, num_cols = rref_matrix.shape
    for row in range(num_rows):
        if all(rref_matrix[row, col] == 0 for col in range(num_cols - 1)) and rref_matrix[row, num_cols - 1] != 0:
            # Pivot in the rightmost column found, matrix is inconsistent
            return False
    
    # No pivot in the rightmost column found, matrix is consistent
    return True

# Test augmented matrices
A_augmented = Matrix([
    [1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 0, 1, 2]
])

B_augmented = Matrix([
    [1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 0, 0, 1]
])

# Test the function
print("Augmented matrix A is consistent:", is_consistent_augmented(A_augmented))
print(A_augmented.rref())
print()
print("Augmented matrix B is consistent:", is_consistent_augmented(B_augmented))
print(B_augmented.rref())

# Augmented matrix A is consistent: True
# (Matrix([
# [1, 0, 0,  0],
# [0, 1, 0, -1],
# [0, 0, 1,  2]]), (0, 1, 2))
# 
# Augmented matrix B is consistent: False
# (Matrix([
# [1, 0, -1, 0],
# [0, 1,  2, 0],
# [0, 0,  0, 1]]), (0, 1, 3))
```

> **Proposition 1.4.4.** If every row of the coefficient matrix has a pivot position, then the corresponding system of linear equations is consistent.

```python
from sympy import Matrix

def is_consistent(matrix):
    coeff_matrix = matrix[:, :-1]  # Extracting only the coefficient matrix
    rref_matrix = coeff_matrix.rref()[0]
    num_cols = rref_matrix.shape[1]
    num_pivots = sum(1 for row in rref_matrix.tolist() if any(row))
    return num_pivots == coeff_matrix.shape[0]

# Test matrices
A = Matrix([
    [1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 0, 1, 2]
])

B = Matrix([
    [1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 0, 0, 1]
])

print("Matrix A is consistent:", is_consistent(A))
print(A.rref())
print()
print("Matrix B is consistent:", is_consistent(B))
print(B.rref())

# Matrix A is consistent: True
# (Matrix([
# [1, 0, 0,  0],
# [0, 1, 0, -1],
# [0, 0, 1,  2]]), (0, 1, 2))
# 
# Matrix B is consistent: False
# (Matrix([
# [1, 0, -1, 0],
# [0, 1,  2, 0],
# [0, 0,  0, 1]]), (0, 1, 3))
```

#### The uniqueness of solutions

> **Principle 1.4.5.**  Suppose that we consider a consistent linear system.
> - If every column of the coefficient matrix contains a pivot position, then the system has a unique solution.
> - If there is a column in the coefficient matrix that contains no pivot position, then the system has infinitely many solutions.
> - Columns that contain a pivot position correspond to basic variables while columns that do not correspond to free variables.
