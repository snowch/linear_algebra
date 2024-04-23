### Pivots

---


#### Finding solutions to linear systems.

Gaussian elimination - reduced row echelon form (RREF)

<details>
  <summary>Sympy Example</summary>

```python
from sympy import Matrix

# Define the augmented matrix
augmented_matrix = Matrix([[1, 2, -3, 4],
                           [2, 4, -6, 8],
                           [3, 6, -9, 12]])

# Perform Gaussian elimination
reduced_row_echelon_form = augmented_matrix.rref()

# Print the reduced row echelon form
print("Reduced Row Echelon Form:")
print(reduced_row_echelon_form[0])

# Reduced Row Echelon Form:
# Matrix([[1, 2, -3, 4], [0, 0, 0, 0], [0, 0, 0, 0]])
```
</details>

---


#### Augmented, Coefficient and Constant Matrices

<details>
  <summary>Sympy Example</summary>

```python
from sympy import Matrix

# Define the augmented matrix
augmented_matrix = Matrix([[1, 2, -3, 4],
                           [2, 4, -6, 8],
                           [3, 6, -9, 12]])

# Coefficient Matrix
coefficient_matrix = augmented_matrix[:, :-1]

# Constant Matrix
constant_matrix = augmented_matrix[:, -1:]

# Print the reduced row echelon form
print("Coefficient Matrix:", coefficient_matrix)
print("Constant Matrix:", constant_matrix)

# Coefficient Matrix: Matrix([[1, 2, -3], [2, 4, -6], [3, 6, -9]])
# Constant Matrix: Matrix([[4], [8], [12]])
```
</details>

---

