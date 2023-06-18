########################################################CALCULATOR########################################################
from art import logo
#Add
def add(n1,n2):
    return n1+n2

#Subtract
def subtract(n1,n2):
    return n1-n2


#Multiuply
def multiuply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiuply,
    "/":divide,
}
def calculator():
  print(logo)
  num1 =int(input("What's the first number?: "))

  for symbol in operations:
      print(symbol)
  should_continue = True

  while should_continue:

    operations_symbol= input("picka an operation from the line above: ")
    num2 =int(input("What's the next number?: "))
    calculation_fucntion= operations[operations_symbol]
    answer=calculation_fucntion(num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculation with {answer}, or Type 'n' to start new calculation.: ")=="y":
        num1 = answer
    else:
        should_continue = False
        calculator()

calculator()