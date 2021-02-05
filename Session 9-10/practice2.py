# def func(*a):
    # print(a)

def my_sum(*values):
    s = 0

    for val in values:
        s = s + val
    
    return s

# func((10, 20, (-1, -2), "Manu"))
# func()

print(my_sum(1,22,3,4))
print(my_sum(10))
print(my_sum())



# def func(a,b=10):
#     return a+b


# # print(func(10, 20))
# print(func(2))