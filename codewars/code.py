#problem Domain
# There is a bus moving in the city which takes and drops some people at each bus stop.

# You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

# Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

# Take a look on the test cases.

# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

# The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

#Solution 

def numbers(bus_stops):
    get_in = 0
    get_off = 0

    for stop in bus_stops :
        get_in += stop[0]
        get_off+=stop[1]
    still= get_in - get_off
    return still


print (numbers([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])) #==>21



#Problem Domain 
# write a function my_add() that takes two arguments. If the arguments can be added together it returns the sum. If adding the arguments together would raise an error the function should return None instead.

# For example, my_add(1, 3.414) would return 4.414, but my_add(42, " is the answer.") would return None.

# Hint: using a try / except statement may simplify this kata.



#Solution 
def my_add(a,b):
    
    try:
        sum = a +b
        return sum


    except:
        sum =None 

print (my_add(1, 3.414)) #=== >4.414
print(my_add(10, "2")) #===>None 



# Problem Domain 
# You have a two-dimensional list in the following format:

# data = [[2, 5], [3, 4], [8, 7]]
# Each sub-list contains two items, and each item in the sub-lists is an integer.

# Write a function process_data()/processData() that processes each sub-list like so:

# [2, 5] --> 2 - 5 --> -3
# [3, 4] --> 3 - 4 --> -1
# [8, 7] --> 8 - 7 --> 1
# and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3


#Solution 

def process_data(data):
    sum = 0 
    res =1
    for i in data :
        sum = i[0]-i[1]
        res *= sum
    return res

print (process_data([[2, 9], [2, 4], [7, 5]]))  #=>(28)



#Problem Domain 

# implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]



#Solution

def array_diff(a,b):

    return [a[i] for i in range (len (a)) if a[i] not in b]


print (array_diff([1,2,2], [])) # [1, 2, 2]
print (array_diff([], [1,2])) #[]
print (array_diff([1,2], [1])) # [2]



# Problem Domain
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).


#Solution

# def multiply (number):
#     sum = 0 
#     for i in range (number):
#         if i % 3 ==0 or  i %5 == 0  :
#             sum += i

#     return sum



# print (multiply(6))


#Problem Domain
# Write a function that takes a shuffled list of unique numbers from 1 to n
# with one element missing (which can be any number including n). Return this missing number.
#example :[4, 2, 3]  =>  1

#Solution :

def find_missing_number(numbers):
#A
    # count = 1 
    # for _ in numbers:
        
    #     if count in numbers :
            
    #         count += 1
            
    # return count
        


#B
    n = len (numbers) +1
    return int((n * (n+1)  / 2) - sum (numbers))

    

print (find_missing_number ([4, 2, 3]))



# Problem Domain 
# Write a function that takes an array of numbers and returns the sum of the numbers.
#  The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

#Solution :

def sum_array(a):

    sum = 0
    for i in a :
        sum +=i 

    return sum 





print (sum_array([1, 5.2, 4, 0, -1]))





# Problem Domain 
#Given a list of unique words.
#Find al l pairs of distinct indices (i, j) in the given list so that the concatenation of the two words, i.e. words[i] + words[j] is a 
# palindrome.


#Solution :


def palindrome_pairs(words):
#A:
    # res = []
    # for i in range (len(words)):
    #     for j in range (len(words)):
    #         if words[i]+words[j] == (words[i]+words[j])[::-1] and i!=j:
    #             res.append([i,j])
    # return res

#B:
    return [[i,j] for i in range (len(words)) for j in range (len(words)) if words[i]+words[j] == (words[i]+words[j])[::-1] and i!=j]


print(palindrome_pairs (["abcd", "dcba", "lls", "s", "sssll"]))













#Problem Domain
# Create a function that takes an array of letters, and combines them into words in a sentence.
# The function should combine all the 0th indexed letters to create the word 'just', 
# all the 1st indexed letters to create the word 'live', etc.
# The array will be formatted as so:

# [
#   ['J','L','L','M'],
#   ['u','i','i','a'],
#   ['s','v','f','n'],
#   ['t','e','e','']
# ] 
# Output  => "Just Live Life Man"

# Solution :
array =[
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
 
] 

def arr_adder(arr):
  
    r = ""
    z= len (array[0])
    for i in range (z):     
         
        for j in array : 
           
                
                
                
                r +=j[i]
        if i == z-1:
                   r= r
        else :
             r += " "
    return r
                
    
      
         
         

print(arr_adder(array))

# i = 0  j =0
# i =1 j =0






# def palindrome_pairs(words):
   

# print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))





# Find longest sequence of zeros in binary representation of an integer.

# 10000010001 -->5
# 1000 -->0

# def binarygap (N):
#     counter = 0
#     max = 0
   
#     M=(str(N).split("1"))
#     l = len(M)-1
    
#     if M[l] != "":
#         M= M[0:len(M) -1]
   
#     for i in M:
            
        
#             for j in i :
#                 counter +=1 
#             if counter > max :
#                 max = counter 
#                 counter = 0
            
                 
               

#     return max
            
                     

# print (binarygap ( 11111000100000))  #==>3


#Example :
# Rotate an array to the right by a given number of steps
# given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    # [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    # [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    # [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

#Solution :
b =[3, 8, 9, 7, 6]
def rotate (arr ,k):
    # list = [3, 8, 9, 7, 6]
    for i in range (k):
#shifted backwards (to left)
      p = arr.pop()
      arr.insert (0,p)
    return(arr)
    

print (rotate ([3, 8, 9, 7, 6] ,3  ))  #[6,3,8,9,7]



# example :
# reverse array :
#solution :

# def reverse (arr):
#     temp = 0
    
#     for i in range (len (arr)//2):
#             temp = arr [(len(arr))-(i+1)]
            
#             arr [(len(arr))-(i+1)]=arr[i] 
            
#             arr[i] = temp 
          
            
#     return  (arr)

    

     


# print (reverse([2,3,4,5,6,7,8]))   #---> [7,6,5,4,3,2]


def unpaired  (arr):
    
    for i in range(len(arr)):
        c=0
        for j in range(len(arr)):
                
                if arr[i]==arr[j]:
                     c+=1

                
                      
                     
        if c%2==1 :
                     return arr[i]
        
        c=0
             

    return   

print (unpaired ([9,3,7,9,3,3,3]))



# Count minimal number of jumps from position X to Y.
# A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach its target.

def jumps (x,y,d):
     
  res = (y-x)/d
  if res %2 !=0 :
        res +=1
  return int(res) 

print (jumps (10,200,30))


# Find the missing element in a given permutation.

#Solution 
# [1,2,3,5]
def missing (arr):
     n = len(arr)+1
     total = int(n*(n+1) /2)
     res = total -sum(arr)
     return res
     

print (missing ([1,2,3,4,5]))




# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.




# 
# 
# def solution (arr):
    # c = 0
    # neew =[]
    # arr.sort()
    # newlist = [abs(i-j) for i in arr for j in arr if i !=j ]
    # print (newlist)
    # k = max(set (newlist) ,key =newlist.count)
    # print (k ,"lll")
    # 
    # for i in arr :
        #  for j in arr:
        # 
                    #  if i !=j :
                            # if abs(i-j) == k:
                                #  
                            #  neew.append(i)
# 
    # x= set(neew)
    # for i in x :
        #  c+=1
# 
    # return c
    # 
# 
# 
# print (solution ([4,7,1,5,3]))
# 

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order
def twoSum( nums, target):
       
    
    
      
       
        for i in range (len (nums)):
           k =i +1
           for j in range (k , len (nums)):
               if nums[i] +nums [j] == target :
                   res = i , j
        return res 

print (twoSum ([2,8,7,3] , 9))
# 
# We have two special characters:
# 
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
# 
#  
# 
# Example 1:
# 
# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:
# 
# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.
#  
# 
# Constraints:
# 
# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.



# Given two sorted arrays nums1 and nums2 of size m and n respectively,
#  return the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).

#Solution :

def median (nums1 ,nums2):
    nums = ( nums1+nums2)
    nums.sort ()
    if len (nums) %2 ==0:
         return float( nums[(len(nums)//2)-1] + nums[(len(nums)//2)])/2
    return float(nums [len(nums)//2])
         
    





print (median ([1,3] ,[2,4]))




#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
#  such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

#Solution:

def three_sum (nums):
    list1 =[]
    for i in range(len(nums)):
         k = i+1
         for j in range (k , len(nums)):
                y = j+1
                for z in range (y,len(nums)):
                     if nums[i] +nums[j]+nums[z] == 0 and [nums[i] ,nums[j],nums[z]] not in list1:
                          l = [nums[i] ,nums[j],nums[z]]
                          l.sort()
                          if l not in list1 : 
                            list1.append(l) 
                          

    return list1
              

print (three_sum([-1,0,1,2,-1,-4])) 


# 
# Given an integer array nums of length n and an integer target, find three integers in nums 
# such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# [-1,2,4,1]
def closest (nums , target):
    list1= []
    min = float ("inf")
    for i in range (len(nums)):
          
          k = i+1
          for j in range (k ,len(nums)):
               y = j+1
               for z in range (y,len (nums)):
                    
                    list1=[nums [i],nums[j],nums[z]]
                    for val in list1 :
                        if sum (list1) == target:
                              return target
                    
                        if abs(target-val)< min :
                         min = abs(val-target) #5
                         list2 =list1
    return list2
   
   
                     
                         
                         
            
                         



print (closest ([-1,2,1,-4] , 1),"nnn")




def  remove_duplicates(arr):
    
    print ('The original list is : '+ str(arr))
     
    # using list comprehension + arr.index()
    # to remove duplicated
    # from list
    res =[]
    for i in range(len(arr)):
          if i == arr.index(arr[i]):
               
               print(i ,"i")
               print(arr.index(arr[i]),"index")
               res.append(arr[i])
   
     
    return res


print (remove_duplicates([1,2,3,5,5]))



# Remove specific val from A given list 
def remove_val (nums,val):


    nums = [i for i in nums if i !=val]
 
    return nums


print (remove_val ([3,2,2,3],3))




# Given two strings a and b, return the index of the first occurrence of a in b, 
# or -1 if a is not part of b.


def first_occurrence (a,b):
     
  if b in a :
       
       return a.index(b,0,1000)
  return -1
       
  

print (first_occurrence("mississippi" , "issip"))



#Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].


#Solution

def find(nums ,target):
    list1 =[]
    if target in nums :
        list1.append (nums.index(target))
        for i in range (len(nums)-1,-1,-1):
         if nums[i] == target :
              list1.append(i)
              break
    else :
     list1= [-1,-1]
    
    return list1
    


print (find ([5,7,7,8,8,10], 8))



     
def search( nums, target):

   
   
   
   
        for i in nums :
            print (i,"i")
            if i == target :
                x= nums.index(i)
           
           
           
        return x
            
print (search([4,5,6,7,0,1,2],0))



# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# You must write an algorithm with O(log n) runtime complexity.

#Solution 

def insert (nums , val):
    x= 0
    if val in nums :
        return nums.index(val)
    else :
        
        for i in range (len(nums)):
                if val > nums[-1]:
                     return len(nums)
                elif val > nums[i] and val <nums[i+1]:
                             nums = nums[:i+1]+[val]+nums[i+1:]
                             x = nums.index(val)
                
                     
                
                        
                   

        return x
 

print (insert ([1,3,5,6] , 0))




# Given an array of integers, 
# \determine the minimum number of elements to delete to leave only elements of equal value.

#[1,2,2,3] ==> 2


def equalizeArray(arr):
     
    counter = 0
    count = 0
    for i in range (len (arr)):
        k = i+1
        for j in range (len(arr[i+1::])):
              print (arr[i::])
              if arr[i] == arr[j] :
                   counter +=2
        if counter>count :
             count = counter
             
        return count



print(equalizeArray([3,3,3,3,3,3]))

def mcount(arr):
  n = []                  #To store count of each elements
  for x in arr:
      count = 0
      for i in range(len(arr)):
          if x == arr[i]:
              count+=1
      n.append(count)
  a = max(n) 
  if a ==1:
       a=0
               #largest in counts list
   #element,frequency
  return   len(arr) - a

print (mcount([1,3,4,2,2]))