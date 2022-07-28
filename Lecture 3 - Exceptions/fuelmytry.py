# My try

def main():
    x, y = get_fraction()
    result = convert_percentage(x, y)
    result = int(result)
    final_print(result)

def get_fraction():
    frac = input('Fraction: ')
    count = -1
    for c in frac:
        count += 1
        if c == '/':
            before_slash = frac[:count]
            after_slash = frac[count+1:]
            return before_slash, after_slash

def check_numeric(X, Y):
    if X.isnumeric() and Y.isnumeric():
        return True

def convert_percentage(X, Y):
    if check_numeric(X, Y) == True:
        X = int(X)
        Y = int(Y)
        if X <= Y and Y > 0:
            result = (X/Y)*100
            return result

def final_print(result):
    if result <= 1:
        print('E')
    elif result >= 99:
        print('F')
    else:
        print(f'{result}%')

try:
    main()
except (ValueError, ZeroDivisionError):
    pass