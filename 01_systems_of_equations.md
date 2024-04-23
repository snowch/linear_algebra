

### Pivots

> **Definition 1.4.1**.  A pivot position in a matrix $A$ is the position of a leading entry in the reduced row echelon matrix of $A$.

**Sympy**
```
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
