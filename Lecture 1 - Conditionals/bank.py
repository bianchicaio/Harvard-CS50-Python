greeting = input('Greeting: ')
greeting = greeting.lower()
greeting = greeting.replace(' ', '')

if 'hello' in greeting[0:5]:
    print('$0')

elif greeting[0] == 'h':
    print('$20')

else:
    print('$100')