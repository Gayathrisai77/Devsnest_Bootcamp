num1 = int(input("enter total number of working days:"))
num2 = int(input("enter no.of days absent:"))
per = (num1-num2)/num1*100
print("your attendence is:",per)
if per < 75:
  print("you are not eligible to sit in examhall")
else:
  print("you are eligible to sit in exam hall")