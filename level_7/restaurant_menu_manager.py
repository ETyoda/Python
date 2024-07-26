menu = {
    "Burger":('main',10.5),
    "Soup":('Appetizer',5.0),
    "Ice Cream":('Dessert',2.5),
    "Salad":('Appetizer',8.6)
}
#add item on menu
menu['steak']=("Main",20.0)
menu['soda']=("Drink",2.0)
#remove item on menu
menu.pop('Salad')

#display menu     
def display_menu(menu):
    print("menu:")
    for dish,info in menu.items():
        print("menu",dish,"| Catagory:",info[0]," Price ",info[1],"$")
        
#count catagory
def count_menu(menu):
    menu_catagory = {}
    for dish,info in menu.items():
        if info[0] in menu_catagory:
            menu_catagory[info[0]]+=1
        else:
            menu_catagory[info[0]]=1
    return menu_catagory

display_menu(menu)
print("The catagory of the menu ",count_menu(menu))

#Update new price
def dis_menu(menu,dish_name,new_price):
     if dish_name in menu:
        menu[dish_name]=(menu[dish_name][1], new_price)
     else:
        print("Enter correct the dish")
dis_menu(menu,"soda",523)
display_menu(menu)