n = int(input("Enter number:"))
a = int(input("Enter start:"))
b = int(input("Enter end:"))
# l = [1,2,3,4,5,6,7,8,9,10]

# for i in l:
for i in range(a, b+1):
    print(n,"X", i, "=", n*i)
