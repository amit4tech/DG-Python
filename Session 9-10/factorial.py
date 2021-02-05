n1 = int(input("Enter number:"))
n2 = int(input("Enter number:"))
n3 = int(input("Enter number:"))

for n in [n1, n2, n3]:
    factorial = 1
    for i in range(n, 0, -1): # range(1, n+1)
        factorial = factorial * i
    
    print("Factorial of number:", factorial)
