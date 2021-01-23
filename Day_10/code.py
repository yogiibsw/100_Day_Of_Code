from os import system
from math import sqrt

def add(n1, n2):
  """Adds 2 numbers"""
  return n1+n2

def substract(n1, n2):
  """Subtracts 2 numbers"""
  return n1-n2

def multiply(n1, n2):
  """Multiplies 2 numbers"""
  return n1*n2

def divide(n1 , n2):
   """Divides 2 numbers"""
   return n1/n2
def square(n1, n2):
  """Squares n1 by n2"""
  return n1**n2
operations = {
  "+": add,
  '-': substract,
  '*': multiply,
  "/": divide,
  "**": square,
}

def calculator():
  """Calculator"""
  
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  print("sqrt")
  operation_symbol = input("Pick an operation from the value above ☝: ")
  if operation_symbol == 'sqrt':
    first_answer = sqrt(num1)
    print(f"√{num1} = {first_answer}")

  else:
    num2 = float(input("What is the second number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  want_to_exit = input("Type 'y' to continue chaining or 'n' to start a new calculation or 'exit' to exit:")
  if want_to_exit == 'y':
    pass
  elif want_to_exit == 'n':
    system('CLS')
    calculator()
  else:
    print("Bye!")
    exit()
  while True:
    operation_symbol = input("Pick another operation: ")
    
    if operation_symbol == 'sqrt':
      second_answer = sqrt(first_answer)
      print(f"√{first_answer} = {second_answer}")

    else:
      num3 = float(input("What is the next number?: "))
      calculation_function = operations[operation_symbol]
      second_answer = calculation_function(first_answer, num3)

      print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

    want_to_exit2 = input("Type 'y' to continue chaining or 'n' to start a new calculation or 'exit' to exit:")
    if want_to_exit2 == 'y':
      first_answer=second_answer
    elif want_to_exit2 == 'n':
      system('CLS')
      calculator()
    else:
      print("Bye!")
      exit()


calculator()