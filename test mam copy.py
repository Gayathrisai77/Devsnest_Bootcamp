#2.write a recursive function calculate the power of a number
#input = n=5 and p = 2

def power (n,p):
  if p != 0:
    return n*power(n,p-1)
  else:
    return 1
print(power(5,2))



#4.write a function to count the no.of vowels in a string
def vowel_count(string):
  if string=="":
    return 0
  if string[0].lower() in "aeiou":
    return 1+vowel_count(string[1:])
  else:
    return vowel_count(string[1:])
string = "I love coding"
print("no.of vowels are:",vowel_count(string))


# 3.check if two strings are anagrams
def check_anagram(str1,str2):
   if sorted(str1)==sorted(str2):
     print("yes")
   else:
     print("no")
str1 = "listen"
str2 = "silent"
print(check_anagram(str1,str2))



















