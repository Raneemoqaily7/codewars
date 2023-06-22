# Write a function that reverses a string. 
# The input string is given as an array of characters s.
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


# def reverseString (nums):
#     for i in range(len(nums)//2):
#         temp = nums[i]
#         nums[i] = nums[len(nums)-(i+1)]
#         nums[len(nums)-(i+1)] = temp
#     return nums
        

# print (reverseString(["h","e","l","l","o"]))

# reverse string in a list with kkeeping the order of the elements 
def reverseString (nums):
    for i in range(len(nums)):
        string =""
        for j in range(len(nums[i])):
            string +=nums[i][len(nums[i])-(j+1)]
        nums[i] =string
            
    return nums

        
print(["hello","yoou","loong","luji","ooops"])
# print (reverseString(["hello","yoou","loong","luji","ooops"]))



# Reverse string 
# Given a signed 32-bit integer x, return x with its digits reversed.
#  If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
