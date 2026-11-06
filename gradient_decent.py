import math
import sys

try:
    dimension = int(input("Enter the dimension between 1 and 3: "))
except Exception:
    print("INVALID INPUT! Please enter a valid numeric value.")
    sys.exit()

if dimension < 1 or dimension > 3:
    print("Please enter a valid dimension between 1 to 3!!!")
    sys.exit()

if dimension == 1:
    expression = input("Enter the function f(x): ")

elif dimension == 2:
    expression = input("Enter the function f(x, y): ")

else:
    expression = input("Enter the function f(x, y, z): ")

allowed = {
    "x" : None, 
    "y" : None, 
    "z" : None,
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


# ==============================================================================================================================================================
if dimension == 1:
# ==============================================================================================================================================================

    def GRADIENT_DESCENT_in_1D(f, x, h, alpha):

        try:
            n = int(input("Enter the number of iterations: "))
            if n <= 0:
                print("Value of n must be greater than zero!!!")
                sys.exit()

            tolerance = float(input("Enter the value of tolerance: "))
            if tolerance <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()
        except Exception:
            print("INVALID INPUT! Please enter a valid numeric value.")
            sys.exit()

        value = f(x)
        converged = False

        print("\n==== GRADIENT DESCENT ====")
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

    def f(x):
        try:
            values = allowed.copy()
            values["x"] = x

            return eval(expression, {"__builtins__": {}}, values)
        except Exception:
            print("INVALID FUNCTION! Please enter a valid function.")
            sys.exit()  

    try:
        x = float(input("Enter the value of x: "))
        h = float(input("Enter the value of h: "))
    except Exception:
        print("INVALID INPUT! Please enter a valid numeric value.")
        sys.exit()

    if h <= 0:
        print("Value of h must be greater than zero!!!")
        sys.exit()

    try:
        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()
    except Exception:
        print("INVALID INPUT! Please enter a valid numeric value.")
        sys.exit()

    result = GRADIENT_DESCENT_in_1D(f, x, h, alpha)
    print(result)

# ==============================================================================================================================================================
elif dimension == 2:
# ==============================================================================================================================================================

    def GRADIENT_DESCENT_in_2D(f, x, y, h, alpha):

        try:
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
        except Exception:
            print("INVALID INPUT! Please enter a valid numeric value.")
            sys.exit()

        value = f(x, y)
        converged = False

        print("\n==== GRADIENT DESCENT ====")
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

    def f(x ,y):
        try:
            values = allowed.copy()
            values["x"] = x
            values["y"] = y

            return eval(expression, {"__builtins__": {}}, values)
        except Exception:
            print("INVALID FUNCTION! Please enter a valid function.")
            sys.exit()  

    try:
        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))
        h = float(input("Enter the value of h: "))
    except Exception:
        print("INVALID INPUT! Please enter a valid numeric value.")
        sys.exit()

    if h <= 0:
        print("Value of h must be greater than zero!!!")
        sys.exit()

    try:
        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()
    except Exception:
        print("INVALID INPUT! Please enter a valid numeric value.")
        sys.exit()

    result = GRADIENT_DESCENT_in_2D(f, x, y, h, alpha)
    print(result)

# ==============================================================================================================================================================
else: 
# ==============================================================================================================================================================

    def GRADIENT_DESCENT_in_3D(f, x, y, z, h, alpha):

        try:
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

            tolerance_z = float(input("Enter the value of tolerance of z: "))
            if tolerance_z <= 0:
                print("Value of tolerance must be greater than zero!!!")
                sys.exit()
        except Exception:
            print("INVALID INPUT! Please enter a valid numeric value.")
            sys.exit()

        value = f(x, y, z)
        converged = False

        print("\n==== GRADIENT DESCENT ====")
        print(f"Initial x : {x} ")
        print(f"Initial y : {y} ")
        print(f"Initial z : {z} ")
        print(f"Initial f(x, y, z) : {value} ")

        for i in range(n):
            gradient_x = (f(x+h, y, z) - f(x-h, y, z))/(2*h)
            gradient_y = (f(x, y+h, z) - f(x, y-h, z))/(2*h)
            gradient_z = (f(x, y, z+h) - f(x, y, z-h))/(2*h)

            if abs(gradient_x) < tolerance_x and abs(gradient_y) < tolerance_y and abs(gradient_z) < tolerance_z:
                converged = True
                print("==== Convergence Achieved ====")
                break

            x_new = x - alpha*gradient_x
            y_new = y - alpha*gradient_y    
            z_new = z - alpha*gradient_z

            value_new = f(x_new, y_new, z_new)

            print("\n ==== ITERATION DETAILS ====")
            print(f"Iteration: {i+1}")
            print(f"Current x: {x} ")
            print(f"Current y: {y} ")
            print(f"Current z: {z} ")
            print(f"Gradient w.r.t x: {gradient_x}")
            print(f"Gradient w.r.t y: {gradient_y}")
            print(f"Gradient w.r.t z: {gradient_z}")
            print(f"New x: {x_new}")
            print(f"New y: {y_new}")
            print(f"New z: {z_new}")
            print(f"New f(x, y, z): {value_new}")

            x = x_new
            y = y_new
            z = z_new
            value = value_new

        if not converged:
            final_gradient_x = (f(x+h, y, z) - f(x-h, y, z))/(2*h)
            final_gradient_y = (f(x, y+h, z) - f(x, y-h, z))/(2*h)
            final_gradient_z = (f(x, y, z+h) - f(x, y, z-h))/(2*h)

            if abs(final_gradient_x) < tolerance_x and abs(final_gradient_y) < tolerance_y and abs(final_gradient_z) < tolerance_z:
                converged = True

        print("\n========== FINAL RESULT ==========")
        print(f"Approximate final point: ({x}, {y}, {z})")
        print(f"Function value at final point: {value}")
        print(f"Converged: {converged}")

        print("\n")

        if not converged:
            print("Maximum iterations reached or convergence not achieved.")

        return {
        "minimum_point": (x, y, z),
        "minimum_value": value,
        "converged": converged
        }

    def f(x ,y, z):
        try:
            values = allowed.copy()
            values["x"] = x
            values["y"] = y
            values["z"] = z

            return eval(expression, {"__builtins__": {}}, values)
        except Exception:
            print("INVALID FUNCTION! Please enter a valid function.")
            sys.exit()  

    try:
        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))
        z = float(input("Enter the value of z: "))
        h = float(input("Enter the value of h: "))
    except Exception: 
        print("INVALID INPUT! Please enter a valid numeric value.")
        sys.exit()

    if h <= 0:
        print("Value of h must be greater than zero!!!")
        sys.exit()

    try:
        alpha = float(input("Enter the learning rate: "))
        if alpha <= 0:
            print("Value of learning rate must be greater than zero!!!")
            sys.exit()
    except Exception:
        print("INVALID INPUT! Please enter a valid numeric value.")
        sys.exit()

    result = GRADIENT_DESCENT_in_3D(f, x, y, z, h, alpha)
    print(result)

