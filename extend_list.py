l1 = [1,2,3,4]

l2 = [10,20,30,40,50,60]

i = 0

while i < len(l2):
    l1.append(l2[i])
    i = i + 1

print("l1:", l1)
print("l2:", l2)