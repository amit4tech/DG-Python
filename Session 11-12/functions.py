def func(**vars):

    a = WWvars.get("a", 0)
    b = vars.get("b", 0)
    # for item in vars.items():
        # print("Key is:", item[0], "Value is:", item[1])

    return a + b
    # return a + b

# print(func(a="abc", b="def", c=33, manu=25, kuchbhi=100, aurkuch=239701))
print(func(a=10, b=2, manu=25, kuchbhi=100, aurkuch=239701))





# d = {"Manu":1231, "Rahul":2313, "Mohini":297, "Bhavya":23901, "Ghevra":97021}

# d = {}

# for i in d.items(): # list of tuples

    # print(i[0], "->", i[1])



# for key in d.keys():
    # print(key, end= " ")

# for val in d.values():
#     print(val, end=" ")
