if __name__ == "factorial":
    raise ImportError("Cannot import this module")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input("Enter number n:"))
    print("Factorial of n:", factorial(n))
