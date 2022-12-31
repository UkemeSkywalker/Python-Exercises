# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

# For example,

sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

## Solution 1
def count_sheep(sheeps):
    num = 0
    for i in sheeps:
        if i == True:
            num +=1
    return num

print(count_sheep(sheeps))

#solution 2

def count_sheep2(sheeps):
    return sheeps.count(True)

print(count_sheep2(sheeps))


# Make a function that will return a greeting statement that uses an input; 
# your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return ("Hello, "+name+" how are you doing today?")

def greet2(name):
    return "Hello, %s how are you doing today?" % name

def greet3(name):
    return f'Hello, {name} how are you doing today?'


# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:


junk = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

def findNeedle(junk):
    for i in junk :
        if i == "needdle" :
            print ("Test")
            return print("found the needle at position " + str(junk.index(i)))



def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

findNeedle(junk)



# In this simple assignment you are given a number and have to make it negative. 
# But maybe the number is already negative?

def make_negative(number):
    return -abs(number)

## option 2
def make_negative2( number ):
    if number == 0 :
        return number
    elif number > 0 :
        return number - (number*2)
    elif number < 0:
        return number


make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0


# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language )
# that receive a list of integers as input, and return the largest and lowest number in that list,
# respectively.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


arr = [4,6,2,1,9,63,-134,566]        

minimum(arr)
maximum(arr)


# In this little assignment you are given a string of space separated numbers, and have to return the 
# highest and lowest number.

def high_and_low(numbers):
    num = list(map(int, numbers.split))
    high = max(num)
    low = min(num)

    return f"{high} {low}"


high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"