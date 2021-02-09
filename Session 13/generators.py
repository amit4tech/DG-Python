

def func():

    yield "First"
    print("Before return")
    yield "Hello"
    print("After return")
    yield "World"



val = func()

print("First next call:")
print(next(val))
print("Second next call:")
print(next(val))

print(next(val))