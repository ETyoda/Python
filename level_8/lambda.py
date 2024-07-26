#lambda input:function
#map(function,list)
square_list = [1,2,3,4,5,6]
new_list = list(map(lambda x:x**2,square_list))
#print(new_list)

sum_list = [(1,2,5),(53,67,21)]
new_list2 = list(map(lambda x:sum(x),sum_list))
#print(new_list2)

 

