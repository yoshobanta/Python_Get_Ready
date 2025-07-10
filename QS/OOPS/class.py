class Demo:
    a = 10
    b = 20

x = Demo()
y = Demo()
name = 'steve'

# bname
# manager name
# contact
# ceo
# location
# branch
# ifsc
# accno
# name
# pno
# email
# address
# aadhar
# pan
# atm pin


# class Bank:
#     bname = 'SBI'
#     ceo = 'Mukesh'
#     contact = 7896548523
#     ifsc = 'SBIN0021519'
#
# c1 = Bank()
# c2 = Bank()
# c1.name = 'Steve'
# c1.pno = 8179267926
# c1.email = 'steve@gmail.com'
# c1.bal = 8520
# c2.name = 'mike'
# c2.pno = 9621862055
# c2.email = 'mike@gmail.com'
# c2.bal = 952

class Bank:
    bname = 'SBI'
    ceo = 'Mukesh'
    contact = 8855699665
    ifsc = 'SBIN0021519'
    manager = 'Sundri'
    mbl = 'Mumbai'

def demo(self, name, pno, email, add, bal):
    self.name = name
    self.pno = pno
    self.email = email
    self.add = add
    self.bal = bal

c1 = Bank()
c2 = Bank()

demo(c1, 'steve', 8179267926, 'steve@gmail.com', 'pune', 58569)
# demo(c2, 'mike', 8585858585, 'mike@gmail.com', 'BBSR', 5869)


class Bank:
    bname = 'SBI'
    ceo = 'Mukesh'
    contact = 8855699665
    ifsc = 'SBIN0021519'
    manager = 'Sundri'
    mbl = 'Mumbai'

    def __init__(self, name, pno, email, add, bal):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.bal = bal

c1 = Bank('likith', 8179626264, 'likith@gmail.com', 'BLR', 852)