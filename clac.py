import sympy as sp

def algebra_solver(equation=None, equations=None, expression=None):
    """
    Algebra solver and simplifier

    Parameters:
    equation (str): a single equation to solve
    equations (list of str): a system of equations to solve
    expression (str): an algebraic expression to simplify

    Returns:
    solution (dict or str): the solution to the equation or system of equations, or the simplified expression
    """
    x, y, z = sp.symbols('x y z')

    if equation:
        # Solve a single equation
        equation = sp.Eq(eval(equation), 0)
        solution = sp.solve(equation, x)
        return solution

    elif equations:
        # Solve a system of equations
        equations = [sp.Eq(eval(eq), 0) for eq in equations]
        solution = sp.solve(equations, (x, y, z))
        return solution

    elif expression:
        # Simplify an algebraic expression
        expression = eval(expression)
        simplified_expression = sp.simplify(expression)
        return simplified_expression

    else:
        raise ValueError("Must provide either an equation, a system of equations, or an expression")

# Example usage
print(algebra_solver(equation="x**2 + 2*x + 1"))  # Solve a single equation
print(algebra_solver(equations=["x + y - 4", "x - y - 2"]))  # Solve a system of equations
print(algebra_solver(expression="x**2 + 2*x + 1"))  # Simplify an expression