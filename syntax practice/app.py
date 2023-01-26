# print("Hospital Checkings")

# name = "John Smith"
# age = 20
# new_patient = True

# print("Patient name is:",name, "He is ", age, "years old", "new Patient: ",new_patient)

# inputs
# name = input("tell us your name: ")
# print("Welcome to Legacy ", name)


# Type Conversions / Type casting
# Calculate age from birth year

# birth_year = input("What year were you born? ")
# age = 2022 - int(birth_year)

# print("Your actual age is ", age)

# Sum 2 numbers
# First = float(input("First: "))
# Second = float(input("Second: "))

# Sum = Second + First

# print ("Sum: ", Sum)


# Strings

# Topic = "The Nations Wealth"
# print(Topic.capitalize())
# print(Topic.upper())
# print(Topic.lower())
# print(Topic.find("Wealth"))
# print(Topic.replace("Wealth", "Pride"))
# print(Topic)
# print("Nations" in Topic)


# Arithmetic Operations
# a = 3 + 5
# b = 3 - 5
# c = 3 * 5
# d = 3 / 5
# e = 10 // 5
# f = 3 ** 5

# print(
#     a, " ",
#     b, " ",
#     c, " ",
#     d, " ",
#     e, " ",
#     f, " "
# )

# Comparison Operators

# a = 3 > 4
# b = 3 >= 4
# c = 3 < 4
# d = 3 <= 4
# e = 3 != 4
# f = 3 == 4

# print(
#     a, " ",
#     b, " ",
#     c, " ",
#     d, " ",
#     e, " ",
#     f, " "
# )


# Logical Operators

# Count = 2
# print( Count > 2 and Count < 20)
# print( Count > 2 or Count < 20)
# print(not  Count > 2 )


# Weight Converter

# weight = float(input("Weight: "))
# uint = input("(K)g or (L)bs: ")

# x = weight / 0.45
# y = weight * 0.45

# if uint.upper() == "K" :
#     print("Weight in lbs: ", x)

# elif uint.upper() == "L" :
#     print("weight in Kg: ", y)

# else : print("invalid input")


# # While Loops
# i = 0

# while i <= 10 :
#     print(i * "*")
#     i += 1

# ## Countdown
# y = 10
# print("Begin Countdown")
# while y >= 0 :
#     print(y)
#     y -=1


## List

# Fish = ["Salmon", "Tuna", "Titus", "CatFish"]
# print(Fish)
# Fish[0] = "Shark"
# print(Fish[0])
# print(Fish[-1])
# print(Fish[-3])
# print(Fish[0:3])


## List Methods
### add Tickt number to list

# Ticket_Numbers = [232,10344773,6656.0924,315006,-347,224,670.5,]
# print(Ticket_Numbers)

# Ticket_Numbers.append(10)
# print(Ticket_Numbers)

# Ticket_Numbers.insert(1, 0.003)
# print(Ticket_Numbers)

# Ticket_Numbers.remove(10344773)
# print(Ticket_Numbers)

# print(20 in Ticket_Numbers) # check if number is in list

# list_length = len(Ticket_Numbers)
# print(list_length)


### Print Ticket_Numbers in new line
## Forloops

# for numbers in Ticket_Numbers :
#     print(numbers)

# from re import I


# Jobs = ["Source Control", "Build", "Unit Test", "Deploy"]

# print(Jobs)

# ### Using forLoop
# for jobs in Jobs :
#     print(jobs)

# ### Using while loop

# i = 0

# while len(Jobs) > i :
#     print(Jobs[i])
#     i += 1



## using whileLoop

# i = 0

# while i < len(Ticket_Numbers) :
#     print("Ticket: ", Ticket_Numbers[i])
#     i += 1


## Range Function
# for numbers in range(0,50, 5) : # Start, Stop, Step 
#     print(numbers)

## Tuples

# names = ("Ukeme", 10, True, 10.45 )
# name2 = ["Ukeme", "Ukeme", 10, 5,5,5,5, True, 10.45 ]
# # for items in name2 :
# #     print(items)

# names.count(5)
# # print(check)
# print(names)



# command_list = ["showinfo","showwarning", "showerror","askquestion", "askokcancel", "askyesno" ]

# # for word in command_list:
# #     print(word)

# i = 0
# while i < len(command_list):
#     cleanse = command_list[i].strip().split(" ")
#     print(command_list[i])
#     i += 1


## Set time out on function
# import signal

# ## signal handler
# def handler(signum, frame):
#     print("Forever is Over!")
#     raise Exception("end of time")

## Long running function
# def loop():
#     import time
#     while True:
#         print("sec")
#         time.sleep(2)

# # loop()

# x = -1
# if x < 0 :
#     raise Exception("sorry, no numbers below zero")

# y = "Hello"

# if not type(y) is int :
#     raise TypeError("Only Integers are allowed")

# try:
#     print(x)
# except:
#     print("An exception occurred")

# Register signal handler

# signal.signal(signal.SIGALRM, handler)

# # Define Timeout for function
# signal.alarm(10)

# try:
#     loop()
# except Exception as exc:
#     print(exc)




# import csv

# header = ["name", "description", "Image", "Price", "Tag"]
# item = ["Fanta", "Orange Drink", "Image", 200, "Drinks"]
# item2 = ["Hisense Tv", "Television", "Image", 300000, "Electical Appliance"]


# with open('./test.csv', "a") as f :
#     writer = csv.writer(f)
#     writer.writerow(header)

#     writer.writerow(item2)


#nested loops
## Domino tiles examples

# for left in range(7):
#     for right in range(left, 7):
#         print("["+ str(left)+"|"+str(right)+"]", end=" ")
#     print()


# Team Pairing example
# make sure the same team are not paired
## home and away paring

# teams = ["Manchester United", "Barcalona", "Liverpool", "PSG", "Real Mardrid"]

# for home in teams:
#     for away in teams:
#         if home != away:
#             print(home + " Vs " + away)


## Recoursion

# def sum_positive_numbers(n):
#     # The base case is n being smaller than 1
#     num = 1
#     if n < num:
#         for i in range(n):
#             num += i
#     return num

# print(sum_positive_numbers(3))




'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⡥⠶⢶⣿⣿⣿⣿⣷⣆⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢡⡞⠁⠀⠀⠤⠈⠿⠿⠿⠿⣿⠀⢻⣦⡈⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠘⡁⠀⢀⣀⣀⣀⣈⣁⣐⡒⠢⢤⡈⠛⢿⡄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠉⠐⠄⡈⢀⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠇⢠⣿⣿⣿⣿⡿⢿⣿⣿⣿⠁⢈⣿⡄⠀⢀⣀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠟⣡⣶⣶⣬⣭⣥⣴⠀⣾⣿⣿⣿⣶⣾⣿⣧⠀⣼⣿⣷⣌⡻⢿⣿
⣿⣿⠟⣋⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣷⠄⢻
⡏⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢂⣭⣿⣿⣿⣿⣿⠇⠘⠛⠛⢉⣉⣠⣴⣾
⣿⣷⣦⣬⣍⣉⣉⣛⣛⣉⠉⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿'''



    #                no maidens?
    # ⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
    # ⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
    # ⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
    # ⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
    # ⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
    # ⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
    # ⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
    # ⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
    # ⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    # ⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    # ⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    # ⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    # ⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀


'''
 ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
'''


# String Methods
"this is a string".upper()
"this is a string".lower()

" this is a string ".strip()
" this is a string ".count("a")

"".join(["This","is","a","sentence"])


# formating Strings

# name = "Skywalker"
# lucky_number = len(name)*2

# print("Hello {}, your lucky number is {}".format(name, lucky_number))


# def student_grade(name, grade):
# 	return "{name} recieved {grade}% on the exam".format(name = name, grade = grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))



# price = 13.2424
# with_tax = price + 5.32155
# name = "James"
# print("Hello {} the price is ${:.2f}, total with tax {:.2f}".format(name, price, with_tax))


'''
Question 1
The is_palindrome function checks if a string is a palindrome. 
A palindrome is a string that can be equally read from left to right or right to left, 
omitting blank spaces, and ignoring capitalization. Examples of palindromes are words 
like kayak and radar, and phrases like "Never Odd or Even". 
Fill in the blanks in this function to return True if the passed string is a palindrome, 
False if not.
'''

# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for letter in input_string:
# 		# Add any non-blank letters to the 
# 		# end of one string, and to the front
# 		# of the other string. 
# 		if letter != " ":
# 			new_string += letter.lower()
# 			reverse_string = new_string.lower()[::-1]
# 	# Compare the strings
# 	if new_string == reverse_string:
# 		return True
# 	return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True


# def replace_ending(sentence, old, new):
# 	# Check if the old string is at the end of the sentence 
    
#     if sentence.endswith(old):
# 		# Using i as the slicing index, combine the part
# 		# of the sentence up to the matched string at the 
# 		# end with the new string

#         i = sentence.rfind(old)
#         new_sentence = sentence[:i]+new 
        
#         return new_sentence

# 	# Return the original sentence if there is no match 
#     return sentence
	
# print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april")) 
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April")) 
# # Should display "The weather is nice in April"


names = ['Folake', 'Abraham', 'Johnson', 'Oluchi']

# total_chars = 0
# for name in names:
#     total_chars += len(name)

# print("Total Characters: {}, the average characters {}".format(total_chars, total_chars/len(names)))

for index, name in enumerate(names):
    print("{} - {}".format(index + 1, name) )


# def staff_info(staffs):
#     result = []

#     for fullname, email in staffs:
#         result.append("{} <{}>".format(fullname, email))
#     return print(result)

# staff_info([("ukeme", "ukeme@gmail.com"), ("James", "jamieG@yahoo.com")])

#list comprehension

languages = ["Java", "Python", "Ruby", "Solidity", "Javascript"]

lengths = [len(langauage) for langauage in languages]

# print(lengths)


def biograpy_list(people):
    for person in people:
        name, age, proffesion = person
        print(f"{name} is {age} years old and works as a {proffesion}")

# biograpy_list([("ukeme", 23, "cloud engineer"), ("chi chi", 24, "Teacher")])

x = {}
file_count = {"txt": 23, "jpg": 10, "mp3": 12}
print (file_count)

print(file_count["jpg"])
print("mp3" in file_count)

file_count["jpg"] =34
print(file_count)

del file_count["txt"]
print(file_count)