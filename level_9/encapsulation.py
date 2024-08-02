class computer:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    def get_info(self):
        return ("The computer name ",self.__brand," and the model ",self.__model)
    
Acer = computer("Acer",2024)
print(Acer.get_info())