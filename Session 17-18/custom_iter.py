def custom_iter(iterable):
    if "__iter__" not in dir(iterable):
        # if "__getitem__" in dir(iterable) and "__len__" in dir(iterable):
        if "__getitem__" in dir(iterable):
            def custom_iterator(iterable):
                i = 0
                # n = iterable.__len__()
                # while i < n:
                while True:
                    try:
                        ele = iterable.__getitem__(i)
                    except IndexError:
                        raise StopIteration
                    else:
                        yield ele
                        i += 1
                # raise StopIteration
                return
            return custom_iterator(iterable)
        else:
            raise TypeError(iterable.__class__.__name__ + " object is not iterable")
    else:
        return iterable.__iter__()

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

# l = CustomList([10, 20, 30, 40, 50, 60])
l = [1,2,3,4,5,6]

for i in custom_iter(l):
    print(i, end=" ")
