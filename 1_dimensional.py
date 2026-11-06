import math
import sys

def GRADIENT_DECENT_in_1D(f, x, h, alpha):

    n = int(input("Enter the number of iterations: "))
    if n <= 0:
        print("Value of n must be greater than zero!!!")
        sys.exit()

    tolerance = float(input("Enter the value of tolerance: "))
    if tolerance <= 0:
        print("Value of tolerance must be greater than zero!!!")
        sys.exit()

    value = f(x)
    converged = False

    print("\n==== GRADIENT DECENT ====")
    print(f"Initial x : {x} ")
    print(f"Initial f(x) : {value} ")

    for i in range(n):
        gradient = (f(x+h) - f(x-h))/(h*2)

        if abs(gradient) < tolerance:
            converged = True
            print("==== Convergence Achieved ====")
            break

        x_new = x - alpha*gradient

        value_new = f(x_new)

        print("\n ==== ITERATION DETAILS ====")
        print(f"Iteration: {i+1}")
        print(f"Current x: {x} ")
        print(f"Gradient: {gradient}")
        print(f"New x: {x_new}")
        print(f"New f(x): {value_new}")

        x = x_new
        value = value_new

    if not converged:
        final_gradient = (f(x + h) - f(x - h)) / (2 * h)

        if abs(final_gradient) < tolerance:
            converged = True

    print("\n========== FINAL RESULT ==========")
    print(f"Minimum point (approx): {x}")
    print(f"Minimum value (approx): {value}")
    print(f"Converged: {converged}")

    print("\n")

    if not converged:
        print("Maximum iterations reached or convergence not achieved.")

    return {
    "minimum_point": x,
    "minimum_value": value,
    "converged": converged
    }


# ===============================================================================================================================================================
# FUNCTION INPUT
# ===============================================================================================================================================================

expression = input("Enter the function f(x): ")

allowed = {
    "x" : None, 
    "sin" : math.sin,
    "cos" : math.cos,
    "tan" : math.tan,
    "sqrt" : math.sqrt,
    "asin" : math.asin,
    "acos" : math.acos,
    "atan" : math.atan,
    "log" : math.log,
    "exp" : math.exp,
    "pi" : math.pi,
    "e" : math.e
}

def f(x):
    values = allowed.copy()
    values["x"] = x

    return eval(expression, {"__builtins__": {}}, values)

x = float(input("Enter the value of x: "))
h = float(input("Enter the value of h: "))
if h <= 0:
    print("Value of h must be greater then zero!!!")
    sys.exit()

alpha = float(input("Enter the learning rate: "))
if alpha <= 0:
    print("Value of learning rate must be greater then zero!!!")
    sys.exit()

result = GRADIENT_DECENT_in_1D(f, x, h, alpha)
print(result)