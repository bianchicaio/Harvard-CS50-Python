expression = input('Type a math expression: ')
expression = expression.split(' ')

first_num = expression[0]
signal = expression[1]
second_num = expression[2]

if signal == '+':
    result = int(first_num) + int(second_num)
    print(float(result))

elif signal == '-':
    result = int(first_num) - int(second_num)
    print(float(result))

elif signal == '*':
    result = int(first_num) * int(second_num)
    print(float(result))

elif signal == '/':
    result = int(first_num) / int(second_num)
    print(float(result))