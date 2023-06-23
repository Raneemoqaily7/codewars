# Write a function that reverses a nums. 
# The input nums is given as an array of characters s.
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


# def reversenums (nums):
#     for i in range(len(nums)//2):
#         temp = nums[i]
#         nums[i] = nums[len(nums)-(i+1)]
#         nums[len(nums)-(i+1)] = temp
#     return nums
        

# print (reversenums(["h","e","l","l","o"]))

# reverse nums in a list with kkeeping the order of the elements 
def reversenums (nums):
    for i in range(len(nums)):
        nums =""
        for j in range(len(nums[i])):
            nums +=nums[i][len(nums[i])-(j+1)]
        nums[i] =nums
            
    return nums

        
# print(["hello","yoou","loong","luji","ooops"])
# print (reversenums(["hello","yoou","loong","luji","ooops"]))



# Reverse nums 
# Given a signed 32-bit integer x, return x with its digits reversed.
#  If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# input -123
# output -321
def reverseInteger (x):
 
    if x<0:
        is_negative=True
        x=abs(x)
    else:  
     is_negative=False
    r =0
    for i in str(x)[::-1]:
        r=r*10+int(i)
    if is_negative :
          r*= -1
    return r

  



# print (reverseInteger((-123890)))
# /////////////////////////////////////////////////////////

# Reverse words in a nums s reverse the order the order of characters 
# in each word withen a sentence while still preserving whitespace and initial word order
# input "let's take leetcode contest"
# output "s'tel ekat edocteel tsetnoc"


def reverseWords (s):
    nums = s.split()

    
    for i in range(len(nums)):
        str =""
        for j in range(len(nums[i])):
            
            str +=nums[i][(len(nums[i])-(j+1))]
            # [(nums[i][(len(nums[i])-(j+1))])]
        nums[i]=str
            
    result=(" ").join(nums)
    return result
    
# print("let's take leetcode contest")
# print (reverseWords ("let's take leetcode contest"))


# /////////////////////////////////////////
#  ggiven two strings s and t , return True if s is a subsequence of t or false otherwise 

#  input s= "abc" , t="ahbgdc"     # output True
# input s="axc" ,t="ahbgdc"       # output False

def isSubsequence (s,t):
    i=0
    str=""
    for j in range(len(t)):
        for k in s[i:i+1]:
            if t[j] == k:
                str+=t[j]
                i+=1
    if str == s:
        return True
    else :
        return False 



# print (isSubsequence("ac","hgdcb"))


# ///////////////////////////////////////////////////////////
# given a non-empty array of integers nums every element appears twice except for one find that single one
# input [4,1,2,1,2]
# output 4


def findSingle(nums):
   return 2*sum(set(nums))-sum(nums)

# print (findSingle( [6,4,4,1,2,1,2]))


# ////////////////////////////////////////////////////////////
#  ffind element which is present in first array and not in second
# input [1,2,3,4,5] ,[2,3,0,1,5]
# output 4

def missingElemment (nums1,nums2):
    # solution1
    for i in nums1:
        if i not in nums2:
            return i
        

    #solution 2
    # return sum(nums1)-sum(nums2)
print (missingElemment([1,2,3,4,5,6] ,[2,3,0,1,5]))

   
    