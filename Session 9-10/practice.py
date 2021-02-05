var1 = 10

def func():
    global var1, var2
    var1 = 20
    var2 = 100
    print(var1)

func()
print(var1)
print(var2)