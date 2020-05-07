# password checker - take in a username and password and outputs the username and password length
username = input('Enter username ')
password = input('Enter password ')

password_length = len(password)
hidden_password = "*" * password_length


print(f'{username}, your password {hidden_password} is {password_length} characters long')
