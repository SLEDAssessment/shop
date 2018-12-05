class Stock:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def create_Stock():
        stock_list = []
        name = input('Enter the name of the product: ')
        print(name)
        price = input('Enter the price of the product: ')
        print(price)
        quantity = input('Enter the quantity available: ')
        print(quantity)
        c = Stock(name, price, quantity)
        stock_list.append(c)


    