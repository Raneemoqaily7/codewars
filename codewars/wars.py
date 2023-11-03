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
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


def moveZeros(nums):
    
    # for i in range(len(nums)):
        # j=1
        # i=0
        # for i in range(len(nums)):
        #         for i in  range(len(nums)-1):
                     
           
        #          if nums[i] ==0 and nums[i+1]!=0 :
        #             nums[i],nums[i+1] = nums[i+1],nums[i]
                   
                 
            
      
               

        # return nums

        j=0
        for i in range(len(nums)):

            if nums[i] != 0 and nums[j]==0:
                temp = nums[j]
                nums[j]=nums[i]
                nums[i] =temp
                # nums[i] ,nums[j] = nums[j], nums[i]

            if nums[j]!=0:
                j+=1

        return nums



            
       
# print (moveZeros([0,1,0,3,12 ,0,9,9,6,8]))



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


def twoSome (nums , target):
    for  i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i !=j:
                return i,j


# print (twoSome([3,2,4],6))


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeElemnt(nums , val):
    i=0
    j=len(nums)-1
    
    while i <=j :
        
        print (i)
        print (j)
        print (nums)
        
        if  nums[i] != val  :
            
            i+=1
       
        
        if nums[i] == val :
            nums[i],nums[j] = nums[j],nums[i]
            
            j-= 1
        else :
            i+=1
      
        
  
    return  i
            
print (removeElemnt( nums = [3], val = 3))

