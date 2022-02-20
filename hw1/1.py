if input('Is it raining? ').lower() == 'yes':
    if input('Is it windy? ').lower() == 'yes':
        print('It\'s too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')
