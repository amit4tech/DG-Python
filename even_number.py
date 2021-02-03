a = int(input("start:"))
b = int(input("end:"))

print("Even numbers between", a, "and", b)

# Code begins

# for i in range(a, b+1):
#     if i%2 == 0:
#         print(i, end= " ")
# if a % 2 != 0:
    # a = a+1
# a = a + (a % 2)

for i in range(a + (a % 2),b+1,2):
    print(i, end=" ")