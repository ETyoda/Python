shopping_list = ['Banana','Orange','Mango','Milk','Bread']
def add_list():
    shopping_list.append('Apple')
def show_list():
    print('The shopping list ')
    for list in shopping_list:
        print(list)
def remove_list():
    shopping_list.remove('Bread')
add_list()
remove_list()
show_list()