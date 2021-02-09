
l1 = [10, 20, 30, 50, 90, 100]
l2 = [1, 2, 5, 6, 8, 9]

iterator_l1 = iter(l1)
i = 0
while i<len(l1):
    val = next(iterator_l1)
    print(val, end=" ")
    i += 1
# for i in l1:
    # print(i, end=" ")

print() 
for i in l2:
    print(i, end=" ")