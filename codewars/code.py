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