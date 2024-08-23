
#if else example

price = int(input("enter your price:"))
if price > 100000:
  tax = 15/100*price    # to convert percentage to decimal we use /100
                          # value/total value*100
elif price > 50000 and price <= 100000:
  tax =10/100*price
else:
  tax = 5/100*price
print("tax to be paid:",tax)
  