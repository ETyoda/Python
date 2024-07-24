#Creating function to add two number
def add(a,b):
 return(a+b)
#Creating function to substract two number
def sub(a,b):
 return(a-b)
#Creating function to multiply two number
def multi(a,b):
 return(a*b)
#Creating function to divide two numbers
def div(a,b):
 return(a/b)

oprator = input("Enter the operator (*,/,+,-): ")
num1=float(input('Enter the first number '))
num2=float(input('Enter the second number '))
if oprator == '+':
    print("The sum is ",add(num1,num2))
elif oprator == '-':
    print('The difference of the two numberis ',sub(num1,num2))
elif oprator == '*':
    print('The multipl of two number ',multi(num1,num2))
elif oprator == '/':
    print('The divide of the two value is ',div(num1,num2))
else:
    print('Invalid oprator')

    
