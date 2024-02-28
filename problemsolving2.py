#1) Reserving the string and upper, length

# string= input("Enter the string you prefer? ")

# b='' 
# for i in range(len(string)-1,-1,-1):
#     b= b + (string[i])
    
# print(b)
    
# print(string.upper())
# print(len(string))


#2) arrang string character such that lowercase letters should come first in another string

# a=input('Enter the string? ')

# a= 'Hello Man'
# b= ''
# c= ''
# for i in a:
#     if i.islower():
#         b =b + i
#     else:
#         c= c + i
# print(b+c) 
        
        
#3)finding the value of char, digit and special char in the string

# str= "P@#yn26at^&i5ve"
# char=0
# digit=0
# spe=0
# for i in str:
#     if i.isdigit():
#         digit= digit + 1
#     elif i.isalpha():
#         char= char + 1
#     else:
#         spe= spe + 1
        
# print(len(str))
# print(f"digit= {digit}" )
# print(f"char= {char}")
# print(f"Special= {spe}")
        
#4) count vowels from the given string

str='Hello mama'
count=0
for char in str:
    if char in 'aeiouAEIOU':
        count =count + 1

print(count)
