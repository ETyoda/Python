class burgur:
    def __init__(self):
        print("Testy and Health food")
    def menu(self):
        print("Double or Triple")
class injoy(burgur):
    pass
piazza_branch = injoy()
piazza_branch.menu()

# computer model inheritance
class computer:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
    def info(self):
        return self.__brand + str(self.__model)
computer_type=computer("acer",2011)
print(computer_type.info())
        
