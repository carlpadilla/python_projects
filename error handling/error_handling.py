# Error Handling

while True:
    try:
        age = int(input('Whats your age? '))
        print(age, 'Years old')
    except:
        print('Please enter a number!')
    else:
        print('Thank you!')
        break
