
while True:

    v = input("Enter n or exit: ")

    if v == "exit": 
        break
    else:
        try:
            print("Reciprocal of v:", 1/int(v))
        except ValueError:
            print("Invalid input, please enter a valid number or 'exit'.")
        except ZeroDivisionError:
            print("Division with zero is not possible.")

print("Exiting...")



# def func(x):
    # return x+10

# gen = map(func, [10, 20, 30, 40])
# results = list(gen)
# iterator = iter(gen)
# results = []
# for i in range(4):
#     results.append(next(iterator))

# results = list(map(func, [10, 20, 30, 40]))
# print(results)


# func([10, 20]) # [20, 30]

# results = []

# for i in [10, 20, 30, 40]:
    # r = func(i)
    # results.append(r)

# print(results)











# v = list(map(int, input().split(" ")))
# print(v)

# for i in range(len(v)):
#     v[i] = int(v[i])

# print(v)
# while True:
#     n = input()

#     if n == "exit":
#         break
#     else:
#         a, b = int(input().split(""))