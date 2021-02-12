class A:
    # a = -1
    def __init__(self):
        self.a = 10

    def print_self(self):
        print("a:", self.a)

class B(A):
    # pass
    def __init__(self):
        # A.__init__(self)
        B.__mro__[1].__init__(self)
        # super().__init__()
        # A().__init__() ## Totally different than the function call at line 12
        self.b = 20
    
    def print_self(self):
        super().print_self()
        # A.print_self(self)
        print("b:", self.b)

obj = B()

print(B.__mro__)
# obj.a = 100
# print(A.a)
# print(B.a)
# print(obj.a)
# obj.print_self()





# class A:
#     pass

# class B(A):
#     pass

# class D(A, B):
#     pass

# print(D.__mro__)
# class A:
#     def print_name(self):
#         print("A")


# class B(A):
#     pass
#     # def print_name(self):
#     #     print("B")

# class C():
#     # pass
#     def print_name(self):
#         print("C")

# # class E(A):
#     # pass

# class D(C, B):
#     pass
#     # def print_name(self):
#     #     print("D")


# # a = A()
# # b = B()
# # c = C()
# # d = D()


# print(D.__mro__)

# # a.print_name(),b.print_name(),c.print_name(), d.print_name()
