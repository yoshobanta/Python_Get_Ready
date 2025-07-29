def div_EH():
    try:
        a = eval(input("Enter a number"))
        b = eval(input("Enter a number"))
        return a/b
    except ZeroDivisionError:
        print("Pls Enter the denominator other than '0'")
        return div_EH()
    except TypeError:
        print("Pls enter only numeric character")
        return div_EH()