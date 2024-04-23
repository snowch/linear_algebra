

### Pivots

#### Two Fundamental Questions.

When we encounter a linear system, we often ask:

- **Existence**: Is there a solution to the linear system? If so, we say that the system is consistent; if not, we say it is inconsistent.
- **Uniqueness**: If the linear system is consistent, is the solution unique or are there infinitely many solutions?

> **Definition 1.4.1**.  A pivot position in a matrix $A$ is the position of a leading entry in the reduced row echelon matrix of $A$.

<details>
<summary>Sympy Example</summary>

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
</details>

#### The existence of solutions

> **Proposition 1.4.3.**  A linear system is inconsistent if and only if there is a pivot position in the rightmost column of the corresponding augmented matrix.

<details>
<summary>Sympy Example</summary>
    
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

</details>

> **Proposition 1.4.4.** If every row of the coefficient matrix has a pivot position, then the corresponding system of linear equations is consistent.

<details>
<summary>Sympy Example</summary>

```python
from sympy import Matrix

def is_consistent(matrix):
    coeff_matrix = matrix[:, :-1]  # Extracting only the coefficient matrix
    pivot_columns = coeff_matrix.rref()[1]
    return len(pivot_columns) == coeff_matrix.shape[0]

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

</details>

#### The uniqueness of solutions

> **Principle 1.4.5.**  Suppose that we consider a consistent linear system.
> - If every column of the coefficient matrix contains a pivot position, then the system has a unique solution.
> - If there is a column in the coefficient matrix that contains no pivot position, then the system has infinitely many solutions.
> - Columns that contain a pivot position correspond to basic variables while columns that do not correspond to free variables.

<details>
<summary>Sympy Example</summary>
    
```python
from sympy import symbols, Eq, solve, Matrix

x, y, z = symbols('x y z')

def has_solution(augmented_matrix):
    
    # Extract coefficients and constants from the augmented matrix
    coefficients = augmented_matrix[:, :-1]
    constants = augmented_matrix[:, -1]

    # Create equations from the coefficients and constants
    equations = []
    for i in range(len(constants)):
        equation = Eq(coefficients[i, 0]*x + coefficients[i, 1]*y + coefficients[i, 2]*z, constants[i])
        equations.append(equation)

    solution = solve((equations[0], equations[1], equations[2]), (x, y, z))
    return solution

def solution_details(augmented_matrix):
    '''
    - If every column of the coefficient matrix contains a pivot position, 
      then the system has a unique solution.
    - If there is a column in the coefficient matrix that contains no pivot position, 
      then the system has infinitely many solutions.
    - Columns that contain a pivot position correspond to basic variables
      Columns that do not contain a pivot position correspond to free variables.
    '''
    
    coeff_matrix = augmented_matrix[:, :-1]  # Extracting only the coefficient matrix
    pivot_columns = coeff_matrix.rref()[1]
    coeff_num_cols = coeff_matrix.shape[0]
    
    # columns with a pivot
    basic_variable_columns = list(pivot_columns)
    
    # columns without a pivot
    free_variable_columns = list(set(range(coeff_num_cols)) - set(pivot_columns))
 
    solution = has_solution(augmented_matrix)
    
    response = ""
    
    if not solution:
        response = 'No Solution.\n'
    elif len(pivot_columns) == coeff_num_cols:
        response = 'Unique Solution (pivot position in each coeff col):\n'
    elif len(pivot_columns) < coeff_num_cols:
        response = 'Infinitely Many Solutions (>= 1 coeff col with no pivots):\n'
    
    return response + (
        f'  Basic Variable Columns {basic_variable_columns} (pivot cols)\n'
        f'  Free Variable Columns: {free_variable_columns} (cols without pivots)\n'
        f'  Solution: {solution}\n'
    )

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

C = Matrix([
    [1, 2, -3, 4],
    [2, 4, -6, 8],
    [3, 6, -9, 12]  # All entries in the last column are 0
])

print("Matrix A:", solution_details(A))
print("Matrix B:", solution_details(B))
print("Matrix C:", solution_details(C))

# Matrix A: Unique Solution (pivot position in each coeff col):
#   Basic Variable Columns [0, 1, 2] (pivot cols)
#   Free Variable Columns: [] (cols without pivots)
#   Solution: {x: 0, y: -1, z: 2}

# Matrix B: No Solution.
#   Basic Variable Columns [0, 1] (pivot cols)
#   Free Variable Columns: [2] (cols without pivots)
#   Solution: []

# Matrix C: Infinitely Many Solutions (>= 1 coeff col with no pivots):
#   Basic Variable Columns [0] (pivot cols)
#   Free Variable Columns: [1, 2] (cols without pivots)
#   Solution: {x: -2*y + 3*z + 4}
```
</details>
