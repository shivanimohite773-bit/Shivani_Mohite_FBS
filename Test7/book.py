
class Book:
    def __init__(self, bid, name, price, author):
        self.bid = bid
        self.name = name
        self.price = price
        self.author = author

    def display(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.name)
        print("Book Price:", self.price)
        print("Book Author:", self.author)
