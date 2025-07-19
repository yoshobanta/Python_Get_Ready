class Bank:
    bname = 'ICICI'
    ceo = 'Mukesh'
    mbl = 'Mumbai'
    ifsc = 'ICICI1234Z'

    def __init__(self, name ,pno, email, add, aadhar, pan, bal):
        self.__name = name
        self.__pno = pno
        self.__email = email
        self.__add = add
        self.__aadhar = aadhar
        self.__pan = pan
        self.__bal = bal
        self.__transactions = []

    def deposit(self, amount):
        if amount >= 50000:
            upan = input('enter your PAN number:')
            if upan == self.__pan:
                self.__bal += amount
                self.__msg()
                self.__transactions.append(f"Credited amount of {amount}")
            else:
                print('Invalid PAN details')
        else:
            self.__bal += amount
            self.__msg()
            self.__transactions.append(f"Credited amount of {amount}")

    def withdraw(self, amount):
        if amount <= self.__bal:
            if amount >= 50000:
                upan = input('enter your PAN number:')
                if upan == self.__pan:
                    self.__bal -= amount
                    self.__msg()
                    self.__transactions.append(f"Debited amount of {amount}")
                else:
                    print('Invalid PAN details')
            else:
                self.__bal -= amount
                self.__msg()
                self.__transactions.append(f"Debited amount of {amount}")
        else:
            print('Insufficient balance')

    def display(self):
        print(f"The name of the customer is {self.__name}")
        print(f"The Pno of the customer is {self.__pno}")
        print(f"The email of the customer is {self.__email}")
        print(f"The address of the customer is {self.__add}")
        print(f"The aadhar of the customer is {self.__aadhar}")
        print(f"The pan of the customer is {self.__pan}")
        print(f"The balance of the customer is {self.__bal}")

    def ch_pno(self, new):
        self.__pno=new

    def ch_email(self, new):
        self.__email = new

    def create_pin(self):
        if 'pin' not in self.__dict__:
            pin = int(input('enter the PIN:'))
            cpin = int(input('re-enter the PIN:'))
            if pin == cpin:
                self.__pin=pin
            else:
                print('Pin Not Matched')
        else:
            print('You have already created a PIN \n To change your pin please call "ch_pin" method')

    def ch_pin(self):
        if 'pin' in self.__dict__:
            upin = int(input('enter the current PIN:'))
            if upin == self.pin:
                new = int(input('Enter the New PIN:'))
                cnew = int(input('Re-Enter the New PIN:'))
                if new == cnew:
                    self.pin = new
                else:
                    print('PIN not Matched')
            else:
                print('Invalid Current PIN')
        else:
            print('Please Create your pin First \n To create your pin please call "create_pin" method')

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def statement(self):
        if self.__transactions:
            for transaction in self.__transactions:
                print(transaction)
        else:
            print('You have Not done any Transactions.')
            print('\t\t\t By the way...')
        print(f"The available Balance is {self.__bal}")

    @staticmethod
    def __msg():
        print('Transaction Successful')

c1 = Bank('Steve', 8179267926, 'steve@gmail.com', 'Pune', 885577448855, 'abcde1234x', 5000)
c2 = Bank('mike', 8143167926, 'mike@gmail.com', 'BBSR', 123654789585, 'ABVF1234P', 4500)