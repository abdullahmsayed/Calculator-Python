import math

import mpmath
import numpy as np


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")

if op in ["sin", "cos", "tan", "cosec","sec","cot", "sqrt", "exp", "sq", "cube", "abs", "cube", "log10","log"]:
    if op == "sin":
        print("Sin of " + str(num1) + " is equals to " + str(math.sin(num1)))
    elif op == "cosec":
        print("Cosec of " + str(num1) + " is equals to " + str(mpmath.csc(num1)))
    elif op == "cos":
        print("Cos of " + str(num1) + " is equals to " + str(math.cos(num1)))
    elif op == "sec":
        print("Sec of " + str(num1) + " is equals to " + str(mpmath.sec(num1)))
    elif op == "tan":
        print("Tan of " + str(num1) + " is equals to " + str(math.tan(num1)))
    elif op == "cot":
        print("Cot of " + str(num1) + " is equals to " + str(mpmath.cot(num1)))
    elif op == "sqrt":
        print("Sqrt of " + str(num1) + " is equals to " + str(math.sqrt(num1)))
    elif op == "cube":
        print("Cube Root of " + str(num1) + " is equals to " + str(np.cbrt(num1)))
    elif op == "exp":
        print("Exp of " + str(num1) + " is equals to " + str([math.exp(num1)]))
    elif op == "sq":
        result = num1 ** 2
        print("Square of " + str(num1) + " is equals to " + str(result))
    elif op == "cube":
        result = num1 ** 3
        print("Cube of " + str(num1) + " is equals to " + str(result))
    elif op == "abs":
        print("Absolute of " + str(num1) + " is equals to " + str(abs(num1)))
    elif op == "exp":
        print("Exp of " + str(num1) + " is equals to " + str([math.exp(num1)]))
    elif op == "log10":
        print("Log10 of " + str(num1) + " is equals to " + str([math.log10(num1)]))
    elif op == "log":
        print("Log of " + str(num1) + " is equals to " + str([math.log(num1)]))
    else:
        print("Invalid Input")


else:
    num2 = eval(input("Enter second number: "))
    if op == "+":
        result = num1 + num2
        print("Sum of " + str(num1) + " + " + str(num2) + " is equals to " + str(result))
    elif op == "-":
        result = num1 - num2
        print("Subtraction of " + str(num1) + " - " + str(num2) + " is equals to " + str(result))
    elif op == "*":
        result = num1 * num2
        print("Multiplication of " + str(num1) + " * " + str(num2) + " is equals to " + str(result))
    elif op == "/":
        if num2 == 0:
            print("Infinite")
        else:
            result = num1 / num2
            print("Division of " + str(num1) + " / " + str(num2) + " is equals to " + str(result))
    elif op == "mod":
        print("Modulus of " + str(num1) + " mod " + str(num2) + " is equals to " + str(num1 % num2))
    elif op == "pow":
        result = math.pow(num1, num2)
        print("Power of " + str(num1) + " to the power of " + str(num2) + " is equals to " + str(result))

    else:
        print("Invalid Input")
