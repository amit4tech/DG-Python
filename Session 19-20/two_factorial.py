# try:
#     from factorial import factorial
# except ImportError:
#     print("Error received")

from factorial import factorial

a, b  = list(map(int, input("Enter space separated integers:").split(" ")))

print("Factorial of both numbers:\n", "a:",factorial(a), "b:", factorial(b))