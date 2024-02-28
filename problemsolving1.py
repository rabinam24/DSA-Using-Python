#1)
# first= int(input('Enter the first number?'))
# second= int(input('Enter the second number?'))

# if first>second:
#     print(f"The greater number is {first}")
# else:
#     print(f'The greater number is {second}')


#2)

# gender= input("Enter the gender?")

# if gender== 'male':
#     print("Goodmorning sir!")
# else:
#     print('Goodmorning madam!')
    
    
#3)
# Value= int(input('Enter the value of integer?'))

# if Value % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')

#4)

# alphabet= input('Enter the alphabets? ')

# if alphabet in 'aeiouAEIOU':
#     print("The alphabet is the vowel! ")
    
# else:
#     print('Alphabet is const')


#5)
# n= int(input('Enter the number? '))
# for i in range(1,n+1):
#     print(i)
    
    
#6)
   
# n= int(input('Enter the number? '))
# for i in range(n,0,-1):
#     print(i)


#7)

# n = int(input('Enter the number? '))
# for i in range(1,11):
#     print(f'{n} * {i} = {n * i}')

#8)

# n= int(input('Enter the number? '))
# #total= n*(n+1) //2
# sum=0
# for i in range(1,n+1):
#     sum= sum + i
# print(f"The sum to n terms is {sum} ")


#9)

# n= int(input('Enter the number? '))

# factorial= 1

# for i in range(1,n+1):
#     factorial = factorial * i
    
# print(factorial)

#10)
# n=int(input('Enter the number? '))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
    
    
#11) Strong number or not
# n=int(input('Enter the number? '))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum= sum + i
        
# if sum == n:
#     print('The number is perfect number')
# else:
#      print('Not perfect')


#12)prime number or not

# n=int(input('Enter the number? '))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
   
# if count == 2: 
#     print('The number is prime')
# else:
#     print('The number is not prime')
        
    

#13) Separate the digit in each 

# n = int(input('Enter the number? '))

# while n >0:
#     print(n%10)
#     n= n//10
    
#14) Palindromic number or not

n= int(input('Enter the numbers? '))
copy = n
rev= 0
while n>0:
    z= n % 10
    rev= rev * 10  + z
    n= n//10
    
if copy == rev:
    print('Palindrome numbers')
else:
    print('Not a palindrome')
        
    