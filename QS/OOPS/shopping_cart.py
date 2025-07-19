from collections import  defaultdict
class Kharidlo:
    sname = 'Kharidlo Care'
    ceo = 'Likith'
    contact = 8179267926
    mbl = 'Qspiders'
    stock = {
        'iphone 13': 15,
        'iphone 13 pro': 10,
        'iphone 13 pro max': 5,
        'iphone 14': 15,
        'iphone 14 pro': 10,
        'iphone 14 pro max': 5,
        'iphone 15': 15,
        'iphone 15 pro': 10,
        'iphone 15 pro max': 5,
        'iphone 16': 15,
        'iphone 16 pro': 10,
        'iphone 16 pro max': 5,
    }
    price = {
        'iphone 13': 52458,
        'iphone 13 pro': 61523,
        'iphone 13 pro max': 70114,
        'iphone 14': 59845,
        'iphone 14 pro': 66667,
        'iphone 14 pro max': 75395,
        'iphone 15': 65432,
        'iphone 15 pro': 76543,
        'iphone 15 pro max': 89654,
        'iphone 16': 77889,
        'iphone 16 pro': 85694,
        'iphone 16 pro max': 123456,
    }
    discount = {
        'iphone 13': 15.0,
        'iphone 13 pro': 10.0,
        'iphone 13 pro max': 5.0,
        'iphone 14': 15.0,
        'iphone 14 pro': 10.0,
        'iphone 14 pro max': 5.0,
        'iphone 15': 15.0,
        'iphone 15 pro': 10.0,
        'iphone 15 pro max': 5.0,
        'iphone 16': 15.0,
        'iphone 16 pro': 10.0,
        'iphone 16 pro max': 5.0,
    }

    def __init__(self, name, pno, email, add):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.cart = defaultdict(int)

    def ch_pno(self, new):
        self.pno = new

    def ch_email(self, new):
        self.email = new

    def display(self):
        print(f"The Name of the customer is {self.name}")
        print(f"The Contact of the customer is {self.pno}")
        print(f"The Email of the customer is {self.email}")
        print(f"The Address of the customer is {self.add}")

    def add_item(self, item, q=1, /):
        if item in self.stock:
            if self.stock.get(item) >= q:
                self.cart[item] += q
                Kharidlo.stock[item] -= q
                print('Item Added to cart Successfully')
            else:
                print(f"Sorry The {item} we have only {self.stock.get(item)}")
        else:
            print(f"Sorry We don't Sell {item}")

c1 = Kharidlo('steve', 8143167926, 'steve@gmail.com', 'BBSR')
c2 = Kharidlo('Mike', 814325698, 'mike@gmail.com', 'Pune')