def sumarr(nums,target):
    a=[]
    for i in range (len(nums)):
        for j in range (len(nums)):
            if i != j and nums[i]+nums[j]==target:
               
                a.append(i)
            
            
           
            
    return a
        
# print(sumarr([2,7,11,15] ,9))


def median(nums1,nums2):
    nums=(nums1+nums2)
    nums.sort()
    
    # print(len(nums)//2)
    if len(nums)%2==0:
        res=float((nums[len(nums)//2]+nums[(len(nums)//2)-1])//2)
        return (res)

    res = float(nums[len(nums)//2])
    return (res)


# print (median([1,2] ,[3,4]))


# ////////////////////////////////////////////////////////////
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
#  Then return the number of unique elements in nums.
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]


def remove_duplicate(nums):
    i=0
    j=1
    while i<=j and j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
    print(nums)
    return i+1
# print  (remove_duplicate([1,2,3]))

# ///////////////////////////////////////////////////////
# Given an integer array nums,
#  rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

def rotate_list(nums ,k):
    # n=len(nums)    
    for _ in range(k):   
        prev=nums[-1]
        for i in range(len(nums)):
            print(prev,nums[i],"=>",nums[i] ,prev)
            temp = nums[i]
            nums[i]=prev
            prev=temp
            
    return nums
    
# print([1,2,3,4,5,6,7,8])
# print(rotate_list([1,2,3,5,6,7],3))


# //////////////////////////////////////////////////////////////
# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true


def containsDuplicate(nums):
    
    # for i in range (len(nums)):
        
    #     if nums[i] not in nums[i+1:]:
    #         res=False
    #     else :
    #         res=True
    #         break
    # return res

    return  len(nums) !=len(set(nums))
         
            
         
            

# print(containsDuplicate([1,7,2,3,6]))



# //////////////////////////////////////////////
# Given a non-empty array of integers nums,
#  every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Input: nums = [2,2,1]
# Output: 1



def singleNumber(nums):
    # for i in range(len(nums)):
    #     c=0
    #     for j in range(len(nums)):
    #         if nums[i] == nums[j] and i !=j:
    #             c+=1
    #     if c==0:
    #         return nums[i]
    return 2*sum(set(nums)) - sum(nums)
            
        

# print (singleNumber([1,2,3,3,2,1,5,3]))


# //////////////////////////////////////////////
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Input: digits = [1,2,3]
# Output: [1,2,4]

def plusOne (nums):
    string = ""
    for i in nums:
        string+=str(i)
    string =int(string)+1
    nums = [int(i) for i in str(string)]
    
      
    return nums


# print (plusOne([9]))


# ///////////////////////////////////////////
