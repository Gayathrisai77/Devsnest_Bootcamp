n = int(input())     #6
for row in range(n,0,-1): #it give row size means 1 line contain 6
                           # 2 has 5
                           # 3 has 4
                           # 4 line has 3 numbers and so on
    for col in range(1,row+1):
       # this for loop for coloums here we want col as many as rows thats why we are giving row+1 
        #row is 5 col is 5
        #row is 4 col 4     #here we are giving input as 6 in line6 we are giving range(1,6+1)(1,7) o/p:123456 in first coloumns
     print(col,end="")
    print()






n = int(input())
for row in range(n,0,-1):
   for col in range(1,row+1):
      print(row,end="")       #here is changing point
   print()