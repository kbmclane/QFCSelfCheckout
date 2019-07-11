"""author: troof
last edit: 7/10
This program will roughly emulate a QFC self-checkout. It will welcome the customer,  "for purchase" and then return an itemized reciept. It does not draw from a predetermined inventory, so item numbers will chan The program will track item names, prices, and quantity in a dictionary with an assigned  tuple 
Assumptions: Users would enter the quantity of items and if a duplicate item was enter, the string would be the same as previously entered.
"""
receipt = {}
groceryList = []
itemCode = 0000
itemName = ""
itemPrice = 0.00
itemQuantity = 0
cartSize = 0
seattleTaxRate = .065
sodaTaxRate = .0175
sodaTax = 0.00
salesTax = 0.00
subTotal = 0.00
total = 0.00
print("Welcome valued customer. Scan first item: ")
while itemName != ("end" or "End"):
  itemName = input("Item Name: ")
  if itemName == ("end" or "End"):
    break
  if itemName in groceryList:
      for item in receipt.values(): 
        if itemName in item:
          item[0] += int(input("Quantity: "))
  else:
    groceryList.append(itemName)
    itemCode += 1;
    itemPrice = float(input("Price: "))
    itemQuantity = int(input("Quantity: "))
    receipt[itemCode] = [itemQuantity, itemName, itemPrice]
  cartSize += int(itemQuantity)
  print("Scan next item...")

bags = int(input("Enter the number of bags you wish you purchase: "))
bagCharge = bags * .25

#get sub total
for item in receipt.values():
  charge = item[0] * item[2]
  if "sodapop" in item[1]:
    sodaTax += (charge * sodaTaxRate)
  subTotal += charge
salesTax = subTotal * seattleTaxRate
total = subTotal + sodaTax + bagCharge + salesTax

print("Subtotal: $", round(subTotal, 2))
if sodaTax > 0:
  print("Soda Tax: $", round(sodaTax, 2))
if bags > 0:
  print("Cost of Bags: $", round(bagCharge, 2))
print("Sales Tax: $", round(salesTax,2))
print("Your total is $", round(total, 2), ".")


