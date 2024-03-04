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

# my_array = [64, 34, 25, 5, 22, 11, 90, 12]

# n=len(my_array)

# for i in range(n-1):
#     min_index=i
#     for j in range(i+1,n):
#         if my_array[j]< my_array[min_index]:
#             min_index=j
#     min_value=my_array.pop(min_index)        
#     my_array.insert(i,min_value)
    
# print(my_array)

# #Improvement of Selection sort
# my_array = [64, 34, 25, 5, 22, 11, 90, 12]

# n=len(my_array)

# for i in range(n-1):
#     min_index=i
#     for j in range(i+1,n):
#         if my_array[j]<my_array[min_index]:
#             min_index=j
#     my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
    
# print(my_array)


#Palindrome 

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str= str(x)         #first ma integer lai string ma convert hanim         
#         rev=x_str[::-1]       #ani str mai reverse hanim 
#         return x_str == rev   #ani reverse haneko value start ko value samma equal chha ki xaina check garim
    
# sol=Solution()
# print(sol.isPalindrome(121))
# print(sol.isPalindrome(-121))
# print(sol.isPalindrome(10))


# #Length of last word
# #given a string s consisting of words and spaces, return the length of the last word in the string.
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.strip().split()

#         if words:
#             return len(words[-1])
#         else:
#             return 0

# sol=Solution()
# print(sol.lengthOfLastWord("Hello World"))
# print(sol.lengthOfLastWord("   fly me   to   the moon  "))
# print(sol.lengthOfLastWord("luffy is still joyboy"))

#Remove Duplicates from the sorted Array
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize pointers
        slow_ptr = 0

        # Iterate through the array with a fast pointer
        for fast_ptr in range(1, len(nums)):
            # If the current element is not equal to the previous element,
            # update the slow pointer and copy the current element to the slow pointer position
            if nums[fast_ptr] != nums[slow_ptr]:
                slow_ptr += 1
                nums[slow_ptr] = nums[fast_ptr]

        # The length of the unique elements is one more than the slow pointer position
        return slow_ptr + 1

# Test the code
sol = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = sol.removeDuplicates(nums)
print(k, nums[:k])
