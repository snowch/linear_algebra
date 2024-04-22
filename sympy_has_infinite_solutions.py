from sympy import symbols, Eq, Matrix

def has_infinite_solutions(equations):
    """
    Determines if a linear system has infinitely many solutions.

    Args:
      equations: A list of symbolic equations representing the linear system.

    Returns:
      True if the system has infinitely many solutions, False otherwise.
    """
    # Extract variables
    variables = list(equations[0].free_symbols)
    
    # Construct coefficient matrix and constant vector
    A = Matrix([[eq.lhs.coeff(v) for v in variables] for eq in equations])
    b = Matrix([-eq.rhs for eq in equations])
    Ab = A.row_join(b)
    
    # Find the reduced row echelon form
    rref_Ab, pivot_columns = Ab.rref()
    
    # Count the number of pivots in the coefficient matrix
    num_pivots_A = sum(1 for i in pivot_columns if i < A.shape[1] - 1)
    
    # Compare the number of variables with the number of pivots
    num_variables = len(variables)
    return num_pivots_A < num_variables

from sympy import symbols, Eq, Matrix

def has_unique_solution(equations):
    """
    Determines if a linear system has a unique solution.

    Args:
      equations: A list of symbolic equations representing the linear system.

    Returns:
      True if the system has a unique solution, False otherwise.
    """
    # Extract variables
    variables = list(equations[0].free_symbols)
    
    # Construct coefficient matrix and constant vector
    A = Matrix([[eq.lhs.coeff(v) for v in variables] for eq in equations])
    b = Matrix([-eq.rhs for eq in equations])
    Ab = A.row_join(b)
    
    # Find the reduced row echelon form
    rref_Ab, pivot_columns = Ab.rref()
    
    # Count the number of pivots in the coefficient matrix
    num_pivots_A = sum(1 for i in pivot_columns if i < A.shape[1] - 1)
    
    # Compare the number of variables with the number of pivots
    num_variables = len(variables)
    return num_pivots_A == num_variables


# Example usage
x, y, z = symbols('x y z')
eq1 = Eq(x + y, 3)
eq2 = Eq(y - z, 2)
eq3 = Eq(2*x + y + z, 4)
system1 = [eq1, eq2, eq3]

print("System 1 has infinitely many solutions:", has_infinite_solutions(system1))
print("System 1 has unique solutions:", has_unique_solution(system1))

