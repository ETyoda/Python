ticket_num = int(input('What is yout ticket number 1 or 3 \n'))
price = 4490
if ticket_num == 1 or ticket_num == 3 :
    print(f'Your ticket number is {ticket_num}')
else:
    print(f'You must be buy tickect and purchesed {price:.2f} pound')