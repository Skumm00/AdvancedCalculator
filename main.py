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

def modulus(x, y):
  #calculates the remainder of x divided by y
  return x % y

def absolute_value(x):
  #calculates the absolute value of x
  return abs(x)

def greatest_common_divisor(x, y):
  #calculates the greatest common divisor of x and y
  while y:
    x, y = y, x % y
  return x

def least_common_multiple(x, y):
  #calculates the least common multiple of x and y
  return (x * y) // greatest_common_divisor(x, y)

def convert_to_radians(x):
  #converts degrees to radians
  return math.radians(x)

def convert_to_degrees(x):
  #converts radians to degrees
  return math.degrees(x)

while True:
  print("Choose operation:")
  print("Add:1")
  print("Subtract:2")
  print("Multiply:3")
  print("Divide:4")
  print("Factorial:5")
  print("Power:6")
  print("Square Root:7")
  print("Logarithm:8")
  print("Sine:9")
  print("Cosine:10")
  print("Tangent:11")
  print("Modulus:12")
  print("Absolute Value:13")
  print("Greatest Common Divisor:14")
  print("Least Common Multiple:15")
  print("Convert to Radians:16")
  print("Convert to Degrees:17")
  print("Exit:18")

  choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18): ")

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
    try:
      num1 = float(input("Enter number 1: "))
      num2 = float(input("Enter number 2: "))
      print(modulus(num1, num2))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '13':
    try:
      num1 = float(input("Enter number for absolute value: "))
      print(absolute_value(num1))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '14':
    try:
      num1 = int(input("Enter number 1: "))
      num2 = int(input("Enter number 2: "))
      print(greatest_common_divisor(num1, num2))
    except ValueError:
      print("Invalid! Please only enter integers.")
      continue

  elif choice == '15':
    try:
      num1 = int(input("Enter number 1: "))
      num2 = int(input("Enter number 2: "))
      print(least_common_multiple(num1, num2))
    except ValueError:
      print("Invalid! Please only enter integers.")
      continue

  elif choice == '16':
    try:
      num1 = float(input("Enter angle in degrees to convert to radians: "))
      print(convert_to_radians(num1))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

  elif choice == '17':
    try:
      num1 = float(input("Enter angle in radians to convert to degrees: "))
      print(convert_to_degrees(num1))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue
      
  # Add a new option to find the least common multiple of two numbers
  elif choice == '19':
    try:
      num1 = int(input("Enter number 1: "))
      num2 = int(input("Enter number 2: "))
      print(least_common_multiple(num1, num2))
    except ValueError:
      print("Invalid! Please only enter integers.")
      continue

  # Add a new option to find the greatest common divisor of two numbers
  elif choice == '20':
    try:
      num1 = int(input("Enter number 1: "))
      num2 = int(input("Enter number 2: "))
      print(greatest_common_divisor(num1, num2))
    except ValueError:
      print("Invalid! Please only enter integers.")
      continue

  # Add a new option to find the sum of the digits of a number
  elif choice == '21':
    try:
      num = int(input("Enter a number: "))
      print(sum_of_digits(num))
    except ValueError:
      print("Invalid! Please only enter integers.")
      continue

  # Add a new option to find the reverse of a number
  elif choice == '22':
    try:
      num = int(input("Enter a number: "))
      print(reverse_number(num))
    except ValueError:
      print("Invalid! Please only enter integers.")
      continue
  elif choice == '18':
      print("Leaving, Sad to see you go")
      break

  else:
    print("Invalid input. Please enter a number between 1 and 18.")
  
  # Add a prompt to ask the user if they want to perform another calculation
  another_calculation = input("Do you want to perform another calculation? (y/n): ")
  if another_calculation.lower() != 'y':
    break
  
  # Reset the choice variable to allow the user to choose another operation
  choice = None
  
  # Add a delay before asking for the next operation
  import time
  time.sleep(1)
  print("\n")

