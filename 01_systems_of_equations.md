

### Pivots

#### Two Fundamental Questions.

When we encounter a linear system, we often ask:

- **Existence**: Is there a solution to the linear system? If so, we say that the system is consistent; if not, we say it is inconsistent.
- **Uniqueness**: If the linear system is consistent, is the solution unique or are there infinitely many solutions?

> **Definition 1.4.1**.  A pivot position in a matrix $A$ is the position of a leading entry in the reduced row echelon matrix of $A$.

[**Sympy**](https://docs.sympy.org/latest/modules/matrices/matrices.html)
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

#### The existence of solutions

> **Proposition 1.4.3.**  A linear system is inconsistent if and only if there is a pivot position in the rightmost column of the corresponding augmented matrix.
> **Proposition 1.4.4.** If every row of the coefficient matrix has a pivot position, then the corresponding system of linear equations is consistent.

#### The uniqueness of solutions

> **Principle 1.4.5.**  Suppose that we consider a consistent linear system.
> - If every column of the coefficient matrix contains a pivot position, then the system has a unique solution.
> - If there is a column in the coefficient matrix that contains no pivot position, then the system has infinitely many solutions.
> - Columns that contain a pivot position correspond to basic variables while columns that do not correspond to free variables.
