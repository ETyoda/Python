bank_name = ("CBE","Awash","Abisiniya",56,67.3)
bank_name = list(bank_name)
print("Before change the bank name" +str(bank_name))
bank_name[4] = "Dashn"
bank_name.remove(56)
print("List data type"+str(bank_name))
bank_name = tuple(bank_name)
print("Tuple data type ",bank_name)
for dis in  range(0,3):
    print("Hello",bank_name[dis])