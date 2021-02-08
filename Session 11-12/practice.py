s = "once upon a time, there lived a lion in a dense forest"

d = {}

for ch in s:

    # if d.get(ch) == None:
    #     d[ch] = 1
    # else:
    #     d[ch] = d[ch] + 1
    d[ch] = d.get(ch,0)+1
    # print(ch, end=" ")

print(d)


# expression = eval(input())
# 
# print(expression)



# n = int(input("Enter n:"))

# i = 0

# while i <= n:

#     if i % 2 == 0:
#         i += 1 # i = i +
#         continue
#     print(i, end=" ")
#     # if i % 2 != 0:
#     #     print(i, end=" ")
#     i = i + 1



# # def func():
# #     pass
# #     # no return statement written
# #     # return None
# #     # return
# #     # All 3 given statements returns value "None"
# # x = func()

# # print(x)