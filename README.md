# Gradient Descent Engine 📉

A custom, pure Python Command-Line Interface (CLI) toolkit designed to iteratively compute the global or local minima of continuous mathematical functions. 
This engine implements the Gradient Descent optimization algorithm from scratch across 1D, 2D, and 3D vector spaces using Central Difference approximations.

## 🚀 Key Features

- **Multi-Dimensional Optimization:** Evaluates and optimizes 1D $f(x)$, 2D $f(x,y)$, and 3D $f(x,y,z)$ functions dynamically parsed from user input.

- **Pure Python Implementation:** Built entirely without external optimization libraries (like SciPy) to demonstrate a deep understanding of core algorithmic mechanics and numerical calculus.

- **Dynamic Parsing:** Uses Python's eval() safely with a restricted local namespace to parse and compute complex string expressions including trigonometric and logarithmic functions.

- **Granular Hyperparameter Control:** Allows users to manually set the initial starting coordinates, learning rate ($\alpha$), maximum iterations, tolerance thresholds for convergence, and finite-difference step size ($h$).

- **Step-by-Step Tracing:** Prints real-time iteration details, tracing the current coordinates, computed gradient vector, and cost function value at each step until convergence is achieved.

## 🛠️ Tech Stack

- **Language:** Python 3

- **Core Logic:** Built-in math module (for function evaluation) and numerical calculus concepts (Central Difference Theorem).

## 💻 How to Run (Installation & Execution)

*This is a pure Python script with no external dependencies required.*

1. ### Clone the repository:

   git clone https://github.com/amit39underworld93-bot/GRADIENT_DECENT.git cd GRADIENT_DECENT

2. ### Install dependencies:
     *This project requires specific libraries for arrays, plotting, and 3D rendering.*
   
     `pip install numpy matplotlib`

3. ### Execute the script:

   `python3 gradient_decent.py`

## 📸 Usage Overview

*Upon running the script, you will be prompted to select the dimensionality and define the function along with its hyperparameters:*

Enter the dimension between 1 and 3: 2

Enter the function f(x, y): x**2 + y**2

Enter the number of iterations: 1000

Enter the value of tolerance of x: 0.0001

Enter the value of tolerance of y: 0.0001

Enter the value of x: 10

Enter the value of y: 10

Enter the value of h: 0.001

Enter the learning rate: 0.1

*The engine will then output the convergence status and the approximated minimum point:*

========== FINAL RESULT ==========

Approximate final point: (0.000123, 0.000123)

Function value at final point: 3.02e-08

Converged: True
