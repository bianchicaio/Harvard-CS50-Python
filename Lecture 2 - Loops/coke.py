due = 50
while due > 0:
   print(f'Amount Due: {due}')
   coin = int(input('Insert Coin: '))
   if coin in [5, 10, 25]:
       due -= coin
change = abs(due)
print(f'Change Owed: {change}')




#due = 50
#amount = 0
#while amount < 50:
#    print(f'Amount Due: {due}')
#    coin = int(input('Insert Coin: '))
#    if coin in [25, 10, 5]:
#        if coin > due:
#            change = coin - due
#            print(f'Change Owed: {change}')
#        else:
#            due -= coin