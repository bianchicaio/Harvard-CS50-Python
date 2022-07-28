vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text = input('Type text: ')
for i in text:
    if i in vowels:
        print('', end='')
    else:
        print(i, end='')
