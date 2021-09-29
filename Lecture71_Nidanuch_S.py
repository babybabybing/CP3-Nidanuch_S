menulist = []
menuPay = []
while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:  menuPrice = input("price:")
  menulist.append(menuName)
  menuPay.append(menuPrice)
def Showbill():
    print ("-------my food-------")
    for number in range(len(menulist)):
        print (menulist[number],menuPay[number])
    print ("Total:",sum(menuPay))
    print ("------Thank you------")
print (Showbill())


