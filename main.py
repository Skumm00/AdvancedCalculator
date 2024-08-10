import math

def add(x, y):
  #gets two numbers together
  return x + y

def subtract(x, y):
  #removes 2 numbers from each other
  return x - y

def multiply(x, y):
  #multiplies the two numbers
  return x * y

def divide(x, y):
  #divide the two numbers
  if y == 0:
    return "Error: Cannot divide by zero"
  else:
    return x / y

def factorial(n):
  #factorial finder
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def power(x, y):
  #calculates x raised to the power of y
  return x ** y

def square_root(x):
  #calculates the square root of x
  if x < 0:
    return "Error: Cannot find square root of a negative number"
  else:
    return x ** 0.5

def log(x, base=10):
  #calculates the logarithm of x to the given base
  if x <= 0:
    return "Error: Cannot find logarithm of a non-positive number"
  else:
    return math.log(x, base)

def sin(x):
  #calculates the sine of x in radians
  return math.sin(x)

def cos(x):
  #calculates the cosine of x in radians
  return math.cos(x)

def tan(x):
  #calculates the tangent of x in radians
  return math.tan(x)

while True:
  print("Choose operation:")
  print("Add:1")
  print("Substract:2")
  print("Multiply:3")
  print("Divide:4")
  print("Factorial:5")
  print("Power:6")
  print("Square Root:7")
  print("Logarithm:8")
  print("Sine:9")
  print("Cosine:10")
  print("Tangent:11")
  print("Exit:12")

  choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12): ")

  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter number 1: "))
      num2 = float(input("Enter number 2: "))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

    if choice == '1':
      print(add(num1, num2))

    if choice == '2':
      print(subtract(num1, num2))

    if choice == '3':
      print(multiply(num1, num2))

    if choice == '4':
      print(divide(num1, num2))

  elif choice == '5':
    try:
      num1 = int(input("Enter a non-negative integer for factorial: "))
      if num1 < 0:
        print("Error: Factorial is not defined for negative numbers")
      else:
        print(factorial(num1))
    except ValueError:
      print("Invalid! Please enter a non-negative integer.")
      continue

  elif choice == '6':
    try:
      num1 = float(input("Enter base: "))
      num2 = float(input("Enter exponent: "))
      print(power(num1, num2))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '7':
    try:
      num1 = float(input("Enter number for square root: "))
      print(square_root(num1))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '8':
    try:
      num1 = float(input("Enter number for logarithm: "))
      base = float(input("Enter base (default is 10): "))
      print(log(num1, base))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '9':
    try:
      num1 = float(input("Enter angle in radians for sine: "))
      print(sin(num1))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '10':
    try:
      num1 = float(input("Enter angle in radians for cosine: "))
      print(cos(num1))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '11':
    try:
      num1 = float(input("Enter angle in radians for tangent: "))
      print(tan(num1))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '12':
      print("Exiting")
      break

  else:
    print("Invalid input. Please enter a number between 1 and 12.")