

# Add
def add(n1,n2):
  return n1+n2
# Subtract
def subs(n1,n2):
  return n1-n2
# Multiply
def multi(n1,n2):
  return n1*n2
# Divide 
def divide (n1,n2):
  return n1/n2

operations = {
  "+" : add,
  "-": subs,
  "*": multi,
  "/": divide
}
def calculator():
  num1 = float(input ("Enter the first number: "))
  
  
  for symbol in operations:
    print (symbol)
    
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input ("Enter the second number: "))
    Operation = operations[operation_symbol]
    answer = Operation (num1,num2)
    
    print (f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculation with the {answer}: ,or type 'n' to start a new calculation.: ") == "y":
      num1 = answer
    else:
      should_continue= False
      calculator()

calculator()      
      

  

