#  def function_name(variable_name):
#       function body

def factorial(n):
    f = 1
    for i in range(n, 0, -1): # range(1, n+1)
        f = f * i
    
    print("Factorial of number:", f)

n1 = int(input("Enter number:"))
n2 = int(input("Enter number:"))
n3 = int(input("Enter number:"))

factorial(n1)
factorial(n2)
factorial(n3)
