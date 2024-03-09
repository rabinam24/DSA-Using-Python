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

# from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         # Initialize pointers
#         slow_ptr = 0

#         # Iterate through the array with a fast pointer
#         for fast_ptr in range(1, len(nums)):
#             # If the current element is not equal to the previous element,
#             # update the slow pointer and copy the current element to the slow pointer position
#             if nums[fast_ptr] != nums[slow_ptr]:
#                 slow_ptr += 1
#                 nums[slow_ptr] = nums[fast_ptr]

#         # The length of the unique elements is one more than the slow pointer position
#         return slow_ptr + 1

# # Test the code
# sol = Solution()
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# k = sol.removeDuplicates(nums)
# print(k, nums[:k])



# Remove Element 
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# from typing import List

# class Solution:
#     # @staticmethod
#     def removeElement(nums: List[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k = k + 1
#         return k

# nums = [2, 3, 3, 2,4,5,2,9]
# val = 2
# k = Solution.removeElement(nums, val)
# print(k, nums[:k])

#Search Insert Position
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# from typing import List
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return left
# Sol=Solution()
# nums1, target1 = [1, 3, 5, 6], 5
# result1 = Sol.searchInsert(nums1, target1)
# print(result1)  

# nums2, target2 = [1, 3, 5, 6], 2
# result2 = Sol.searchInsert(nums2, target2)
# print(result2)  

# nums3, target3 = [1, 3, 5, 6], 7
# result3 = Sol.searchInsert(nums3, target3)
# print(result3) 


# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# def permuteUnique(nums):
#     def backtrack(start):
#         if start == len(nums):
#             result.append(nums[:])
#             return
        
#         used=set()
        
#         for i in range(start,len(nums)):
#             if nums[i] not in used:
#                 used.add(nums[i])
#                 nums[start],nums[i]= nums[i],nums[start]
#                 backtrack(start + 1)
#                 nums[start],nums[i]= nums[i],nums[start]
        
#     result=[]
#     backtrack(0)
#     return result


# nums1 = [1, 1, 2]
# print(permuteUnique(nums1))


# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Input: head = [1,1,2]
# Output: [1,2]
# Importing the "Optional" type hint from the "typing" module.
from typing import Optional

# Defining a class called "ListNode" for a single element in a linked list.
class ListNode:
    # Constructor method to initialize a ListNode with a value (default is 0) and a reference to the next node (default is None).
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the current node.
        self.next = next  # Reference to the next node in the list.

# Defining a class called "Solution" that contains a method to delete duplicate values from a linked list.
class Solution:
    # Method to delete duplicate values from a linked list.
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # Starting from the head of the linked list.

        # Looping through the linked list until either it reaches the end or there's only one element left.
        while current and current.next:
            # Checking if the current node's value is the same as the next node's value.
            if current.val == current.next.val:
                # If yes, skipping the next node by updating the "next" reference.
                current.next = current.next.next
            else:
                # If no, moving to the next node in the linked list.
                current = current.next

        return head  # Returning the modified linked list.

# Function to print the elements of a linked list.
def print_linked_list(head):
    while head:
        print(head.val, end=" ")  # Printing the value of the current node.
        head = head.next  # Moving to the next node.
    print()

# Creating an instance of the "Solution" class.
sol = Solution()

# Test case 1: Creating a linked list [1, 1, 2], calling the deleteDuplicates method, and printing the result.
head1 = ListNode(1, ListNode(1, ListNode(2)))
result1 = sol.deleteDuplicates(head1)
print("Test case 1:")
print_linked_list(result1)
# Expected Output: 1 2

# Test case 2: Creating a linked list [1, 1, 2, 3, 3], calling the deleteDuplicates method, and printing the result.
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result2 = sol.deleteDuplicates(head2)
print("Test case 2:")
print_linked_list(result2)
# Expected Output: 1 2 3
