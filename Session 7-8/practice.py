# if -1:
#     print("True hai bhai")
# else:
#     print("False hai bhai")

l = list(map(int, open("./Session 7-8/array.txt").read().split(" ")))
s = set(map(int, open("./Session 7-8/array.txt").read().split(" ")))

import time

start_time = time.time()

if 10000000-1 in l:
    print("Time taken in list:", time.time() - start_time)

start_time = time.time()
if 10000000-1 in s:
    print("Time taken in set:", time.time() - start_time)