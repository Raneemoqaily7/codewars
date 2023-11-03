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
            print (s[i:i+1])
           
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
# print (missingElemment([1,2,3,4,5,6,9] ,[9,2,3,0,1,5]))

# /////////////////////////////////////

# combine two lists alternatingly taking elements 
# input [a,b,c] , [1,2,3]
# output [a,1,b,2,c,3]


def combineLists(nums1,nums2):
    list1=[]
    for i in range(len(nums1)) :
        # for j in range(len(nums2)):
        #     if i ==j:
                list1.append(nums1[i])
                list1.append(nums2[i])

    return list1

# print (combineLists(["a","b","c"] , [1,2,3]))


# ////////////////////////////////////////////////////////////////
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]


def getConcatenation (nums):
    ans =[i for i in nums]  + [i for i in nums] 
    return ans
       

# print (getConcatenation([1,2,1]))



# /////////////////////////////////////////////////////////////////////////////////////

# given a string str , convert the first letter of each word in the string too uppercase
# input str = "i love programming"
#  output "I Love Programming"


def uppercase(s):
    words = s.split(" ") #["i" ,"love" ,"programming"]
    for i in range(len(words)):
        str =""
        str+=chr(ord(words[i][0])-32)
        str+=words[i][1::]
        words[i]=str
    return (" ".join(words))
    
# print(uppercase("i love programming"))



# ////////////////////////////////////////////////////////////
# given a list contains digits from 1 to n except of one missing number,return that missing number 
# input =[2,3,4,5]  
# output = 4

def missingNumber (nums):
    n = len(nums)
    
    return ((((n+1 ) * (n+2))  //2 ) - sum (nums))


# print (missingNumber([1,2,3,4,6] ))



# ////////////////////////////////////////////////////////////////////////////////
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# input "elettcodcode"  # output 1
# input "eettcodcode"  # output -1

def firsOccure(string):


    for i in range(len(string)):
        if string[i] not in string[:i]+string[i+1::]:
            
             return i
            
    return -1

# print(firsOccure("elettcodcode"))


# ////////////////////////////////////////////////////////////////////////////
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# inputs => s = "anagram", t = "nagaram"  //  output true
#inputs s = "rat", t = "car"    //Output: false


def isAnagram (s,t):
    
    list1=[i for i in s]
    list2=[i for i in t]
    return sorted(list1) ==sorted(list2)
        
# print (isAnagram("aacc","caac"))

# //////////////////////////////////////////////////////////////////////////
# A phrase is a palindrome if, after converting all uppercase letters into lowercase
#  letters and removing all non-alphanumeric characters, it reads the same forward 
# and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Input: s = "A man, a plan, a canal: Panama"
# Output: true


def isPalidrome (s):
    string =""
    for i in s:
        if 91>ord(i) >=65 or 123>ord(i) >=97 or 57>=ord(i) >=48  :
            string +=i
    string = string.lower()
   
    return string ==string[::-1]
# print (isPalidrome("Marge, let's \"[went].\" I await {news} telegram."))

# /////////////////////////////////////////////////////////////////

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def commonPrefix(strings):
    
    minimum = min(len(s) for s in strings)
    prefix= ""
    for i in range(minimum):
        char = strings[0][i]
        for j in range(1,len(strings)):
            if strings[j][i] !=char:
                return prefix
            
        prefix+=char
    return prefix
                    
                   
                    


# print (commonPrefix(["flower","flow","flight"]))

def test (nums):
    
        i=0
        j=1
        while i<=j and j<len(nums):
            if nums[i]==nums[j]:
                j+=1
                
            else :
                nums[i+1]=nums[j]
                i+=1
        print(nums)
        return i+1



# print(test([1,1,2,2,3]))

def find_elements_with_no_greater_right(arr):
    res=[]
    max = float("-inf")
    for i in range(len(arr) -1 ,-1 ,-1):
        if arr[i]>max:
            res.append(arr[i])
            max =arr[i]
    res.reverse()
    return res
    

# print (find_elements_with_no_greater_right([2,8,5,4]))


def getString(s1,s2):
    return len(set(s1)) == len(set(s2))
# print(getString ("geeks" ,"geks"))

# //////////////////////////////////////////////////////////////////////////////////

# "Write a function that will take in an array and index and return new 
# shuffled array where the fist element 

# will be starting from that index and the second will be the original one and so on
# input: [1, 2, 3, 4, 5, 6], idx = 3 // output: [4, 1, 5, 2, 6, 3] 
def shuffle_array_from_index(arr, idx):
    n = len(arr)
    shuffled_array = []
    
    # Start from the given index and alternate elements from the left and right of it
    for i in range(idx, n):
        
        shuffled_array.append(arr[i])
        if i - idx ==idx :
            break 
        shuffled_array.append(arr[i - idx])
    
    return shuffled_array


input_array = [1, 2, 3, 4, 5, 6]
index = 3
output_array = shuffle_array_from_index(input_array, index)
# print(input_array)
# print(output_array)  # Output: [4, 1, 5, 2, 6, 3]


# ///////////////////////////////////////////////////////////////////////////

# Find all the missing numbers between the min and the max number in this array (No built in methods allowed) // 
# array = [0, 5, 4, 9, 3]; 
def maxi(arr):
    array = []
    maximum = max(arr)
    minimum = min(arr)
    for i in range (minimum+1 , maximum):
        if i not in arr:
            array.append (i)
    return array
print (maxi([5, 2, 9, 1, 7, 3]))
# /////////////////////////////////////////////////////////////////////////

def find_repeated_letters(string):
    letter_counts = {}

    for char in string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    repeated_letters = [(letter, count) for letter, count in letter_counts.items() if count > 1]
    
    return repeated_letters

# print (find_repeated_letters("fyooooeeez"))

def cube (num):
    res =0
    for i in str(num):
        res += int(i)**3
    # return res == num
# print (cube(152))


def sum_repeated_numbers(nums):
    

    output = []
    running_sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            running_sum += nums[i]
        else:
            output.append(running_sum)
            running_sum = nums[i]

    output.append(running_sum)  # Add the final sum

    return output
print(sum_repeated_numbers( [2, 2, 2, 7, 3, 3, 1, 2]))









