user = {
    "name":"Yodahe Gossa",
    "username":"isaac",
    "password":"1234",
    "address":{"street":"Niger","house_number":3421}
}
 
print(user.values())
user["job_title"] = "Computer Science"
 
for val in user.items():
    print(val)
job = user.pop("job_title")
print(job,user.values())
 
for key,value in user.items():
    print(key,value)