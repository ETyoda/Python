tasks =['planning','design','coding','testing']
time_spent=[0,0,0,0]
def log_time(task,time):
    for i in range(len(tasks)):
        if task == tasks[i]:
            time_spent[i] = time_spent[i] + time
        i+=1
while True:
    task = input("Select the task 'Planning,Design,Coding,Testing' or if you want to exit write exit \n ").lower()
    if task in tasks:
        time=int(input('Enter the time spent \n'))
        log_time(task,time)
    elif task not in tasks:
        print("The task isn't in the list Please Enter the right task")
    elif task == 'exit':
        break
print("Summary of the tasks and their time spent ")
for i in  range(len(tasks)):
    print(tasks[i]+' = '+str(time_spent[i]))