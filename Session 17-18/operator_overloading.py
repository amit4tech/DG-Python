class CustomList:

    def __init__(self, arr):
        self.arr = arr

    def __getitem__(self, ix):
        return self.arr[ix]
    
    # def __setitem__(self, ix, val):
    #     self.arr[ix] = val

    def __str__(self):
        return "CustomList: " + "<"+", ".join([str(i) for i in self.arr])+">" 

    # def __iter__(self):
    #     return iter(self.arr)
    
    # def __len__(self):
    #     # return len(self.arr)
    #     return self.arr.__len__()

l = CustomList([10, 20, 30, 40, 50, 60])

# iter(l)
for i in l:
    print(i, end=" ")

# print(l[3])
# print(l[4])
# l[4] = -20
# print(l[4])

# print(l)

# print(len(l))

# class ABC:

#     def __init__(self, val):
#         self.val = val
    
#     def __add__(self, other):
#         val = self.val + other.val
#         return ABC(val)


# a = ABC(10)
# b = ABC(20)

# c = a + b

# print(type(c))
