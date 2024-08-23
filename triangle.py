num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
num3 = int(input("enter a number:"))
if num1==num2==num3:
  print("Equalateral triangle")
elif num1!=num2 and num2!=num3 and num3!=num1:
  print("scalene triangle")
elif num1==num2 or num2!=num3 or num3==num1:
  print("isosceles triangle")
else:
  print("invalid")