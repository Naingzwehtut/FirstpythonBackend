print('Create acount now')
username = input('Enter username: ')
password = input('Enter password: ')

print('Your account has been created sucessfully.')
print('Login now!')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('Logged in successfully.')
else:
    print('Invalid credentials')