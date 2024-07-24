name = input('Enter username: ')

if name == 'Yodahe':
    password = input('Enter your password: ')
    if password == '1234':
        print('Welcome ' +name)
    else:
        print('Incorrect Password')
else:
    print('Username doesnot exit')
