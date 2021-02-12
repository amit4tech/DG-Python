class ABC:

    def __init__(self):
        self.__a = 10
        self.__b = 20
        self.__c = 30
    
    def print_abc(self):
        print("a:", self.__a, "b:", self.__b, "c:", self.__c)
        self.__does_nothing()

    def __does_nothing__(self):
        pass

obj = ABC()
# obj.print_abc()

# print("a:", obj.__a, "b:", obj.__b, "c:", obj.__c)

print("a:", obj._ABC__a, "b:", obj._ABC__b, "c:", obj._ABC__c)
# obj._ABC__does_nothing()
# print(dir(obj))
# print(dir(ABC))
