name = "Yodahe gosa"
x = name.split(" ")
print("split by space: ",x)

fname= "zebenay/kebede/habtemariyam"
y = fname.split("/",1)
print("split by notation upto 1: ",y)

gname = "Gosa\nEshetu\nkassa"
z = gname.splitlines()
print("split by n upto newline: ",z)

sname = ("isaac","Abuka")
x = "yodahe".join(sname)
print("JOin the name by the two name: ",x)

name2 = "Baby yoda"
x = name2.lstrip("Baby ")
# return yoda 
x = name2.replace("Baby","Master") 