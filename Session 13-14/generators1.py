
def gen():

    while True:
        # print("Before", end=" ")
        val = yield 10 # val = -10
        print("Value Generator recieved:", val)


obj = gen()
val = next(obj)
# print("Value Main recieved:", val)
# print("Value Main recieved:",obj.send(-10))
# print("Value Main recieved:",obj.send(-20))
# print("Value Main recieved:",obj.send(-30))
# print("Value Main recieved:",next(obj))

next(obj.send(10)) #next(10)