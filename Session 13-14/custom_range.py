
import time

def custom_range(start, stop, step):
    # arr = []
    i = start

    while i<stop:
        # arr.append(i)
        yield i
        i += step

    # return arr

s = time.time()
for i in custom_range(0, 10000000, 1):
    # print(i, end= " ")    
    pass
print("Time:", time.time() - s)