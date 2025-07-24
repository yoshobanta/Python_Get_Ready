# single level inheritance.=
class Bank:
    bname = 'SBI'
    manager = 'SaiRam'
    ifsc = 'SBIN0021519'

    # constructor method of a parent class
    def __init__(self, name, add, bal):
        self.name = name
        self.add = add
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
        else:
            print('In sufficient Balance')

    # object method of a parent class.
    def display(self):
        print(f"The Name of the customer is:{self.name}")
        print(f"The Address of the customer is:{self.add}")
        print(f"The Balance of the customer is:{self.bal}")

c1 = Bank('sathish', 'Blr', 845)

class Bank1(Bank):
    ceo = 'Mukesh'
    contact = 8855669988

    # constructor method  of child class.
    def __init__(self, name, add, bal, pno, email, aadhar, pan):
        # constructor chaining
        # calling a parent class constructor method inside the child class constructor method.
        Bank.__init__(self, name, add, bal)
        self.pno = pno
        self.email = email
        self.aadhar = aadhar
        self.pan = pan

    # object method of a child class
    def display(self):
        # method chaining
        # calling object method of a parent class inside object method of a child class
        Bank.display(self)
        print(f"The pno of the customer is:{self.pno}")
        print(f"The email of the customer is:{self.email}")
        print(f"The aadhar of the customer is:{self.aadhar}")
        print(f"The pan of the customer is:{self.pan}")


c2 = Bank1('mike', 'Pune', 8524, 8855996644, 'mike@gmail.com', 456987456987, 'ABCDE1234x')