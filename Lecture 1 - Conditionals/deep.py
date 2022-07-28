x = input('What is the answer to the Great Question of Life, the Universe and Everything: ')
x = x.lower()
x = x.replace(' ', '')

if x == '42' or x == 'forty-two' or x == 'fortytwo':
    print('Yes')
else:
    print('No')