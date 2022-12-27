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