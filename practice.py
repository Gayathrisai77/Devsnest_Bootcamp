       #LAST DIGIT OF A NUMBER
num= int(input("enter a number:"))
print("last digit is",num%10)    #if we do % to any number it wull return last digit of a numer ex:num%10




#checking the last digit is divisible by 3 or not
#ex1
num = int(input("enter any number"))  
id = num%10
if id%3 ==0:
  print("last digit is divisible by 3")
else:
  print("last digit is not divisible by 3")




#ex2
num = int(input("enter any number:"))
value = num%10
if value%3 ==0:
  print("last digit is dividible by 3")
else:
  print("last digit is not divisible by 3")