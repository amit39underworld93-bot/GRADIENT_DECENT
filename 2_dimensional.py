import math
import sys

def GRADIENT_DECENT_in_2D(f, x, y, h, alpha):

    n = int(input("Enter the number of iterations: "))
    if n <= 0:
        print("Value of n must be greater than zero!!!")
        sys.exit()

    tolerance_x = float(input("Enter the value of tolerance of x: "))
    if tolerance_x <= 0:
        print("Value of tolerance must be greater than zero!!!")
        sys.exit()

    tolerance_y = float(input("Enter the value of tolerance of y: "))
    if tolerance_y <= 0:
        print("Value of tolerance must be greater than zero!!!")
        sys.exit()

    value = f(x, y)
    converged = False

    print("\n==== GRADIENT DECENT ====")
    print(f"Initial x : {x} ")
    print(f"Initial y : {y} ")
    print(f"Initial f(x, y) : {value} ")

    for i in range(n):
        gradient_x = (f(x+h, y) - f(x-h, y))/(2*h)
        gradient_y = (f(x, y+h) - f(x, y-h))/(2*h)

        if abs(gradient_x) < tolerance_x and abs(gradient_y) < tolerance_y:
            converged = True
            print("==== Convergence Achieved ====")
            break

        x_new = x - alpha*gradient_x
        y_new = y - alpha*gradient_y    

        value_new = f(x_new, y_new)

        print("\n ==== ITERATION DETAILS ====")
        print(f"Iteration: {i+1}")
        print(f"Current x: {x} ")
        print(f"Current y: {y} " )
        print(f"Gradient w.r.t x: {gradient_x}")
        print(f"Gradient w.r.t y: {gradient_y}")
        print(f"New x: {x_new}")
        print(f"New y: {y_new}")
        print(f"New f(x, y): {value_new}")

        x = x_new
        y = y_new
        value = value_new

    if not converged:
        final_gradient_x = (f(x+h, y) - f(x-h, y))/(2*h)
        final_gradient_y = (f(x, y+h) - f(x, y-h))/(2*h)

        if abs(final_gradient_x) < tolerance_x and abs(final_gradient_y) < tolerance_y:
            converged = True

    print("\n========== FINAL RESULT ==========")
    print(f"Approximate final point: ({x}, {y})")
    print(f"Function value at final point: {value}")
    print(f"Converged: {converged}")

    print("\n")

    if not converged:
        print("Maximum iterations reached or convergence not achieved.")

    return {
    "minimum_point": (x, y),
    "minimum_value": value,
    "converged": converged
    }


# ===============================================================================================================================================================
# FUNCTION INPUT
# ===============================================================================================================================================================

expression = input("Enter the function f(x, y): ")

allowed = {
    "x" : None, 
    "y" : None, 
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

def f(x ,y):
    values = allowed.copy()
    values["x"] = x
    values["y"] = y

    return eval(expression, {"__builtins__": {}}, values)

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
h = float(input("Enter the value of h: "))
if h <= 0:
    print("Value of h must be greater then zero!!!")
    sys.exit()

alpha = float(input("Enter the learning rate: "))
if alpha <= 0:
    print("Value of learning rate must be greater then zero!!!")
    sys.exit()

result = GRADIENT_DECENT_in_2D(f, x, y, h, alpha)
print(result)