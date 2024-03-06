# a way of solving a problem
# learning how to solve a problem how a computer does

# looping through things


# algorithm = function


# building a function that does a specific task. Usually that means
# searching through a dataset to either find a specific value, set of values, or
# manipulate values.


# write an algorithm, which given a list of numbers, will find whether or not a specific
# value exists


# function definition = blueprint for the function
# list = input
def find_num(list):
    print("in our function", list)
    for num in list:
        if num == 2:
            print("We found the number 2!")
            return num
    print("We didn't find it")
    return False


[1,24,5,6,7]
    

# dataset
our_list = [2,54,57,9,2]
list_2 = [532105468,3215,6,21,12491235]

# function call
returned_value = find_num(list_2)
print("our returned value:",returned_value)



    # [2,4,5,7,8]


# 1. Turn our folder into a git repo - git init
# a git repo has a hidden folder called .git which keeps track of all of our changes



