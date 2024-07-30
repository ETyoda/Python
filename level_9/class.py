class human():
    def __init__(self,name,age):
        print("I'm a human :) ")
        print("my name is ",name, " And i am ",age)
        self.person_name=name
    def accident(self,location):
        print(" Help ",self.person_name," At ",location)

lawra = human("lawra",23)
robert = human("robert",20)
lawra.accident("Tunel")