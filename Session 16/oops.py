class Dog:
    no_of_legs = 4
    no_of_eyes = 2
    tail_length = 0.5
    practice = 100

    def __init__(self, n):#, p):
        self.name = n
        # self.practice = p
        # print("Dog Created...")

    def just_print():
        print("Hey, m just printing...")

    just_print = staticmethod(just_print)

    def just_print_class(cls):
        print("Hey, m just printing with class...")

    just_print_class = classmethod(just_print_class)

    def walk(self):
        print(self.name,"Walking...")
    
    def smell(self):
        print(self.name,"Smelling...")
    
    def sit(self):
        print(self.name, "Sitting...")

    def jump(self):
        print(self.name, "Jumping...")

dog1 = Dog("Browny")#, 10)
dog2 = Dog("Bruno")#, 20)
dog3 = Dog("Jacky")#, -1)

# dog1.walk()
# dog2.walk()
# dog3.sit()


# print(dog1.no_of_eyes)
print(dog1.practice)
print(dog2.practice)
print(dog3.practice)

print(Dog.practice)

# class Human:
#     name = "Manu"

#     def input_user():
#         return input("Enter something:")
    
# print(Human.name)
# print(Human.input_user())


# # # class Human:
# # #     name = "Manu"
# # #     place = "Sadiq Nagar"
# # #     city = "New Delhi"
# #     # state = "Delhi"


# # class Human:
# #     pass

# # Human.name = "Manu"
# # Human.place = "Sadiq Nagar"
# # Human.city = "New Delhi"


# # print(Human.name)
# # print(Human.place)
# # print(Human.city)

# # Human.state = "Delhi"
# # print(Human.state)


