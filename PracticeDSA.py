# #Fibonacci using LOOP
# x=0
# y=1
# print(x)
# print(y)

# for i in range(18):
#     z=x+y
#     print(z)
#     x=y
#     y=z
    
# #fibonacci using Recursion

# print(0)
# print(1)
# count = 2

# def fibonacci(x, y):
#     global count
#     if count <= 19:
#         z = x + y
#         print(z)
#         x = y
#         y = z  
#         count += 1
#         fibonacci(x, y)
#     else:
#         return

# fibonacci(1, 0)
    
# #Nth fibonacci number

# def F(n):
#     if n <=1:
#         return n
#     else:
#         return F(n-1) + F(n-2)
    
# print(F(19)) 


#BUbble sorting has time complexity of O(n**2)

# my_array = [7, 3, 9, 12, 11]

# n=len(my_array)

# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_array[j]> my_array[j+1]:
#             my_array[j],my_array[j+1]= my_array[j+1],my_array[j]

# print(my_array)


# #Bubblesort Improvement
# my_array = [7, 3, 9, 12, 11]
# n=len(my_array)

# for i in range(n-1):
#     swapped=False
#     for j in range(n-i-1):
#         if my_array[j]> my_array[j+1]:
#             my_array[j],my_array[j+1]= my_array[j+1],my_array[j]
#             swapped= True
#     if not swapped:
#         break
            
# print(my_array)


#Selection sorting

my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n=len(my_array)

for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_array[j]< my_array[min_index]:
            min_index=j
    min_value=my_array.pop(min_index)        
    my_array.insert(i,min_value)
    
print(my_array)

#Improvement of Selection sort
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n=len(my_array)

for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_array[j]<my_array[min_index]:
            min_index=j
    my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
    
print(my_array)