n = int(input("Enter n:"))

# l = []
# for i in range(n):
#     l.append(i*i) # l.append(i**2)
#     l.append((i,i))
def square(x):
    return x*x

# l = [i**2 for i in range(n)]
# l = [i*i for i in range(n)]
# l = [square(i) for i in range(n)]
l = [(i,i) for i in range(n)]

print(l)