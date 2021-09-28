def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("-----------------")
    return menuSelect()
def menuSelect():
    userSelected = int(input("Please select the menu >>"))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()
def vatCalculator():
    price = int(input("Price (THB) : "))
    vat = 7
    result = price + (price * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    totalPrice = price1 + price2
    result = totalPrice + (totalPrice * vat / 100)
    return result

print("total price include tax:", login())