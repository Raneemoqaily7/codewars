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

def solution (N):
    counter = 0
    max = 0
   
    M=(str(N).split("1"))
    l = len(M)-1
    
    if M[l] != "":
        M= M[0:len(M) -1]
   
    for i in M:
            
        
            for j in i :
                counter +=1 
            if counter > max :
                max = counter 
                counter = 0
            
                 
               

    return max
            
                     

print (solution ( 11111000100000))  #==>3
