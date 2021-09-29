menuList = []
def showBill():
    totalprice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number])
        totalprice += int((menuList[number][1]))
    print("total:", totalprice)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])
showBill()