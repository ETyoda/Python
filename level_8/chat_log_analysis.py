chat_logs = [
    "My order is delayed",
    "I want to return  my purchase",
    "The app is crashing frequently",
    "Payment issues, please help",
    "Need help with account recovery",
    "Delivery was incomplete",
    "Can't login to my account",
    "Having trouble with checkout"
]
categories = {"Order":0,"App":0,"Payment":0,"Account":0,"Delivery":0}
#function  to categories issuses 
def issues(chat_log):
    for log in chat_log:
        for category in categories.keys():
            if category.lower() in log.lower():
                categories[category] +=1
            
    
print(categories)
issues(chat_logs)
print(categories)
#search the keyword
def keyword(keyword,logs):
    result =[]
    for log in logs:
        if keyword.lower() in log.lower():
            result.append(log)
    print(result)
word= input("Enter a keyword: ")
keyword(word,chat_logs)