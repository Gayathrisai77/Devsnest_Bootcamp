# def count_vowel(string):
#     if not string:
#         return 0
#     if string[0].lower() in "aeiou":
#         return 1 + count_vowel(string[1:])
#     else:
#         return count_vowel(string[1:])
# string ="hello world this is geeks for geeks world"
# print("number of vowels:",count_vowel(string))




def count_vowel(string):
    if not string:
        return 0
    if string[0].lower() in "aeiou":
        return 1 + count_vowel(string[1:])
    else:
        return count_vowel(string[1:])
string = "a mrw"
print("vowel count is:",count_vowel(string))
# def vowel_count(string):
#     if not string:
#         return 0
#     if string[0].lower() in "aeiou":
#         return 1 + vowel_count(string[1:])
#     else:
#          return vowel_count(string[1:])
# string = "hello welcome to my channel"
# print(vowel_count(string))


def vowel_count(string):
    if not string:
        return 0 
    if string[0].lower() in "aeiou":
        return 1 + vowel_count(string[1:])
    else:
        return vowel_count(string[1:])
string = "today iam very tensed"
print("no.of vowels:",vowel_count(string))