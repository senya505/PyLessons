name = input('Enter your name: ')
if len(name) < 5:
    surname = input('Enter your surname: ')
    print((name + surname).upper())
else:
    print(name.lower())
