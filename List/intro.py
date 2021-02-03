n = int(input("Enter the total number of digits:"))
i = 1
my_digits = []

while i<=n:
    print("Enter", i, "th number:")
    digit = int(input())
    # print("Digit entered by you:", digit)
    my_digits.append(digit)
    i = i + 1

print("The values that you provided:", my_digits)
