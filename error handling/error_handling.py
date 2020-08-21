# Error Handling

while True:
    try:
        age = int(input('Whats your age? '))
        10/age
        print(age, 'Years old')
    except ValueError:
        print('Please enter a number!')
    except ZeroDivisionError:
        print('Please enter a number higher than 0!')
    else:
        print('Thank you!')
        break
