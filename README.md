# Study Notes for "Understanding Linear Algebra by David Austin"

----

My notes for: https://understandinglinearalgebra.org/ula.html

----

### Sage Math utility

<details>
 <summary>Sage Code</summary>

```python
def my_solve(augmented_matrix):

    A = augmented_matrix[:, :-1]
    Y = augmented_matrix[:, -1]

    m, n = A.dimensions()
    p, q = Y.dimensions()

    if m!=p:
        raise RuntimeError("The matrices have different numbers of rows")
    X = vector([var("x_{}".format(i)) for i in [0..n-1]])

    # don't include the free variables in solve
    X_pivots = vector([var("x_{}".format(i)) for i in [0..n-1] if i in A.pivots()])

    sols = []
    for j in range(q):
        system = [A[i]*X==Y[i,j] for i in range(m)]
        sols += solve(system, *X_pivots)
    return sols



def solution_details(augmented_matrix):
    '''
    - If every column of the coefficient matrix contains a pivot position, 
      then the system has a unique solution
    - If the constant column contains a pivot then there is no solution
    - If there is a column in the coefficient matrix that contains no pivot position, 
      then the system has infinitely many solutions.
    - Columns that contain a pivot position correspond to basic variables
      Columns that do not contain a pivot position correspond to free variables.
    '''
    
    try:
        num_coeff_cols = augmented_matrix.subdivisions()[1][0]
        if not num_coeff_cols > 0:
            raise ValueError("Subdivided augmented matrix required1.")
    except (AttributeError, IndexError):
        raise ValueError("Subdivided augmented matrix required.")
        
    pivots = augmented_matrix.pivots()
    const_col = num_coeff_cols + 1
    
    print("##############################", end="\n\n")
    print(augmented_matrix, end="\n\n")
    print(augmented_matrix.rref(), end="\n\n")
    # print("pivots: ", pivots, end="\n\n")
    
    # zero base const col
    if (const_col - 1) in pivots:
        print('No Solution (Inconsistent - const col has pivot)')
    else:
        if (len(pivots)) == num_coeff_cols:
            print("Unique Solution (pivot position in each col)")
        elif len(pivots) < num_coeff_cols:
            print('Infinitely Many Solutions (>= 1 coeff col with no pivots)')

    
    solution = my_solve(augmented_matrix)
    if solution:
        # flatten solution list
        import operator
        solution = reduce(operator.concat, solution)
    
    print("Columns that:")
    print(" - contain a pivot position correspond to basic variables")
    print(" - do not contain a pivot position correspond to free variables")
    print("Solution: ")
    [ print(f'  {s}') for s in solution if len(solution) ]
    print()
    
# Examples

M = matrix(QQ, 3, [1,2,3,0,1,2,0,0,1])
v = vector(QQ, [4,3,2])
Maug = M.augment(v, subdivide=True)
solution_details(Maug)


M = matrix(QQ, 2, [1,1,2,2])
v = vector(QQ, [4,8])
Maug = M.augment(v, subdivide=True)
solution_details(Maug)


M = matrix(QQ, 3, [1,2,3,0,1,2,0,0,0])
v = vector(QQ, [4,3,1])
Maug = M.augment(v, subdivide=True)
solution_details(Maug)


##############################

[1 2 3|4]
[0 1 2|3]
[0 0 1|2]

[ 1  0  0| 0]
[ 0  1  0|-1]
[ 0  0  1| 2]

Unique Solution (pivot position in each col)
Columns that:
 - contain a pivot position correspond to basic variables
 - do not contain a pivot position correspond to free variables
Solution:  [[x_0 == 0, x_1 == -1, x_2 == 2]]

##############################

[1 1|4]
[2 2|8]

[1 1|4]
[0 0|0]

Infinitely Many Solutions (>= 1 coeff col with no pivots)
Columns that:
 - contain a pivot position correspond to basic variables
 - do not contain a pivot position correspond to free variables
Solution:  [[x_0 == -x_1 + 4]]

##############################

[1 2 3|4]
[0 1 2|3]
[0 0 0|1]

[ 1  0 -1| 0]
[ 0  1  2| 0]
[ 0  0  0| 1]

No Solution (Inconsistent - const col has pivot)
Columns that:
 - contain a pivot position correspond to basic variables
 - do not contain a pivot position correspond to free variables
Solution:  []

##############################
```

</details>

----

### Symp utility

<details>
 <summary>Sympy Code</summary>

```python
from sympy import symbols, Eq, solve, Matrix, pprint

x, y, z = symbols('x y z')

def has_solution(augmented_matrix):
    # Get the number of variables
    num_variables = augmented_matrix.shape[1] - 1
    
    # Generate symbols for variables
    variables = symbols('x:' + str(num_variables))
    
    # Extract coefficients and constants from the augmented matrix
    coefficients = augmented_matrix[:, :-1]
    constants = augmented_matrix[:, -1]

    # Create equations from the coefficients and constants
    equations = []
    for i in range(len(constants)):
        equation = Eq(sum(coefficients[i, j] * variables[j] for j in range(num_variables)), constants[i])
        equations.append(equation)

    # Solve the equations
    solution = solve(equations, variables, dict=True)
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
    const_matrix = augmented_matrix[:, -1:]
    
    pivot_columns = coeff_matrix.rref()[1]
    coeff_num_cols = coeff_matrix.shape[0]
    
    # useful to check if rightmost col has a pivot
    aug_pivot_columns = augmented_matrix.rref()[1]
    last_column_index = augmented_matrix.shape[1] - 1
    last_column_is_pivot = last_column_index in aug_pivot_columns

    # columns with a pivot
    basic_variable_columns = list(pivot_columns)
    
    # columns without a pivot
    free_variable_columns = list(set(range(coeff_num_cols)) - set(pivot_columns))
 
    solution = has_solution(augmented_matrix)
    
    response = ""
    
    if not solution:
        response = 'No Solution.\n'
    elif len(pivot_columns) == coeff_num_cols:
        response = 'Unique Solution (pivot position in each col):\n'
    elif len(pivot_columns) < coeff_num_cols:
        response = 'Infinitely Many Solutions (>= 1 coeff col with no pivots):\n'
    
    if last_column_is_pivot:
        response += '  Inconsistent - rightmost column has pivot\n'
    
    return response + (
        f'  Basic Variable Columns: {basic_variable_columns} (pivot cols)\n'
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
pprint(A.rref()[0])
print()

print("Matrix B:", solution_details(B))
pprint(B.rref()[0])
print()

print("Matrix C:", solution_details(C))
pprint(C.rref()[0])
print()


# Matrix A: Unique Solution (pivot position in each col):
#   Basic Variable Columns: [0, 1, 2] (pivot cols)
#   Free Variable Columns: [] (cols without pivots)
#   Solution: [{x: 0, y: -1, z: 2}]

# ⎡1  0  0  0 ⎤
# ⎢           ⎥
# ⎢0  1  0  -1⎥
# ⎢           ⎥
# ⎣0  0  1  2 ⎦

# Matrix B: No Solution.
#   Inconsistent - rightmost column has pivot
#   Basic Variable Columns: [0, 1] (pivot cols)
#   Free Variable Columns: [2] (cols without pivots)
#   Solution: []

# ⎡1  0  -1  0⎤
# ⎢           ⎥
# ⎢0  1  2   0⎥
# ⎢           ⎥
# ⎣0  0  0   1⎦

# Matrix C: Infinitely Many Solutions (>= 1 coeff col with no pivots):
#   Basic Variable Columns: [0] (pivot cols)
#   Free Variable Columns: [1, 2] (cols without pivots)
#   Solution: [{x: -2*y + 3*z + 4}]

# ⎡1  2  -3  4⎤
# ⎢           ⎥
# ⎢0  0  0   0⎥
# ⎢           ⎥
# ⎣0  0  0   0⎦
```
</details>

---

#### Systems of Equations
 - [Solutions to Linear Systems](./pages/01_systems_of_equations_solutions_to_linear_systems.md)
 - [Pivots and their influence on solution spaces](./pages/01_systems_of_equations_pivots.md)

#### Vectors, matrices, and linear combinations
 - [Vectors and linear combinations](./pages/2.1_vectors_and_linear_combinations.md)
 - [Matrix multiplication and linear combinations](./pages/2.2_matrix_multiplication_and_linear_combinations.md)
 - [The span of a set of vectors](./pages/2.3_the_span_of_a_set_of_vectors.md)
 - [Linear independence](./pages/2.4_linear_independence.md)
 - [Matrix transformations](./pages/2.5_matrix_transformations.md)
 - [The geometry of matrix transformations - TODO]()

#### Invertibility, bases, and coordinate systems - TODO
 - [Invertibility]()
 - [Bases and coordinate systems]()
 - [Image Compression]()
 - [Determinants]()
 - [Subspaces]()

#### Eigenvalues and eigenvectors - TODO
 - [An introduction to eigenvalues and eigenvectors]()
 - [Finding eigenvalues and eigenvectors]()
 - [Diagonalization, similarity, and powers of a matrix]()
 - [Dynamical systems]()
 - [Markov chains and Google’s PageRank algorithm]()

#### Linear algebra and computing - TODO
 - [Markov chains and Google’s PageRank algorithm]()
 - [Finding eigenvectors numerically]()

#### Orthogonality and Least Squares - TODO
 - The dot product
 - Orthogonal complements and the matrix transpose
 - Orthogonal bases and projections
 - Finding orthogonal bases
 - Orthogonal least squares

#### Singular value decompositions
 - Symmetric matrices and variance
 - Quadratic forms
 - Principal Component Analysis
 - Singular Value Decompositions
 - Using Singular Value Decompositions

---

The material presented in this document is adapted from "Understanding Linear Algebra" by David Austin, a professor of mathematics at Grand Valley State University. The original work is available at understandinglinearalgebra.org.

---

Study Notes for Understanding Linear Algebra © 2024 by Chris Snow is licensed under CC BY 4.0 

---

Thanks to https://latex.codecogs.com/eqneditor/editor.php

---
