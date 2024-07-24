name = input('What is yout name?')
age = input('How old are you?')

def age_update(name,age):
    new_age = int(age) + 1
    print("Hi "+name+ "," "Get " +str(new_age)+ " years old next year")
age_update(age=43,name="tina")
age_update(name,age)   