amount = 0
num = int(input("enter u r bill"))
if num <= 100:
  amount= 0
if num >= 100 and num <= 200:
  amount = (num-100)*5  #given num-100 and then multiply with 5
if num > 200:
  amount = 500 + (num-200)*10  #here we are taking 500 becz above 100 is already taken care of and then we are multiplying with 10
print("u r bill is",amount)