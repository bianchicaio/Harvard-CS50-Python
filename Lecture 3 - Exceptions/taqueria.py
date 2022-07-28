menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


value = 0
while True:
    try:
        order = input('Item: ')
        order = order.title()
        if order in menu:
            value += menu[order]
            print("$", f"{value:.2f}", sep="")
    except (ValueError, KeyError):
        pass
    except EOFError:
        print("\n")
        break