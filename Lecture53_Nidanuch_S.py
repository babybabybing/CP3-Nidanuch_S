price = input ("please enter the price:")
def taxcal(price):
        result = (price+(price*7/100))
        return result
print("totalprice :"+ str(taxcal(price)))