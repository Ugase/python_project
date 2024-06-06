import sympy as sp

def algebra_solver(equation, variables):
    """
    Solves an algebraic equation for a given list of variables.

    Parameters:
    equation (str): The algebraic equation as a string (e.g., "x**2 + 3*y - 4 = 0")
    variables (list): A list of variables to solve for (e.g., ["x", "y"])

    Returns:
    solution (dict): A dictionary of solutions for each variable
    """
    # Define the variables as symbolic variables
    var_dict = {var: sp.symbols(var) for var in variables}

    # Parse the equation using SymPy
    try:
        lhs, rhs = equation.split("=")
        lhs = sp.sympify(lhs, locals=var_dict)
        rhs = sp.sympify(rhs, locals=var_dict)
        eq = sp.Eq(lhs, rhs)
    except Exception as e:
        print(f"Error parsing equation: {e}")
        return {}

    # Solve the equation
    solution = {}
    for var in variables:
        try:
            sol = sp.solve(eq, var_dict[var])
            solution[var] = sol
        except Exception as e:
            print(f"Error solving for variable {var}: {e}")
            solution[var] = None

    return solution

# Example usage:
equation = "x**2 + 3*y - 4 = 0"
variables = ["x", "y"]

solution = algebra_solver(equation, variables)
print(f"Solutions for {variables}:")
for var, sol in solution.items():
    if sol is not None:
        print(f"{var}: {', '.join(str(s) for s in sol)}")
    else:
        print(f"{var}: No solution found")3