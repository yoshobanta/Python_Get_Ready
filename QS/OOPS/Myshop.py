from collections import defaultdict
class Kharidlo:
    shop_name = "Kharidlo_2.0"
    owner = "Yosho"
    mbl = "RKL"
    contact = 9876543210
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

    def __init__(self,name,add,pno):
        self.name = name
        self.add = add
        self.pno = pno
        self.cart = defaultdict(int)
        # here cart is object member and we cannot access it through class
        # example Kharidlo.cart will throw an error

    def display(self):
        print(f"The Name of the customer is {self.name}")
        print(f"The Address of the customer is {self.add}")
        print(f"The Contact of the customer is {self.pno}")

    def add_item(self, item , q=1,/):
        if item in self.cart:
            self.cart[item] += q
            print('Item Added to cart Successfully')
        else: 
            print("Sry we do not have this item")



c1 = Kharidlo('steve', 8143167926, 'BBSR')




