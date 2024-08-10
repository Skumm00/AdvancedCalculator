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
    return #error because no divison by zero
  else:
    return x / y

def factorial(n):
  #factorial finder
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

while True:
  print("Choose operation:")
  print("Add")
  print("Substract")
  print("Multiply")
  print("Divide")
  print("Factorial")
  print("Exit")

  choice = input("Enter choice(1/2/3/4/5/6): ")

  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter number 1: "))
      num2 = float(input("Enter number 2: "))
    except ValueError:
      print("Invalid! Please only enter real numbers.")
      continue

    if choice == '1':
      add(num1,num2)
      
    if choice == '2':
      add(num1,num2)
      
    if choice == '2':
      add(num1,num2)