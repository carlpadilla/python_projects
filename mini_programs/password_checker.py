# password checker - take in a user 
username = input('Enter username ')
password = input('Enter password ')

password_length = len(password)
hidden_password = "*" * password_length


print(f'{username}, your password {hidden_password} is {password_length} characters long')
