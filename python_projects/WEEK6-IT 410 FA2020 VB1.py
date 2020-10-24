# Problem 1.

fave_pizza = 'Dominoes'

print(fave_pizza)

fave_pizza = 'choc chic'




print(fave_pizza)

# Problem 2-2

# Create a variable and store the name of the last business you made a purchase from in it. 
# Create another variable and store the name of one of the items you purchased on your last trip.

# Then, print out a message that says something like, 
# "The last time I went to <name of business>, I purchased <the name of an item>." 
# Using string concatenation to splice your variables into your output message.
# So, if I said that the last store I went to was Amazon.com and the last thing I bought was a book, my message would say,"
# The last time I went to Amazon.com I purchased a book."

store = 'Walmart'

items = 'Vanilla Cheesecake'

print('The last time I went to ' + store, 'I purchased ' + items + '.')

# Problem 2-3

# Store the name of your favorite car in a variable. Print it out using lower, upper, and title case.

my_car = 'ferrari'

# Printing car with lower case.
print('\n')
print(my_car.lower())

# Printing car with upper case.
print('\n')
print(my_car.upper())

print('\n')
# Printing car with title case.
print(my_car.title())


# Problem 2-4

# Store a favorite quote of yours as a variable. Then, add \t\n to the beginning and end of it using concatenation. 
# Print out the quote. Then, apply lstrip() to the quote and print the result. Lastly, apply strip() to your quote and print the result.

quote = '\t\nThe finish line is my loveline\t\n'

# quote = 'The finish line is my loveline'

print(quote)

# apply lstrip()
print(quote.lstrip())

#apply strip()
print(quote.strip())


# Problem 2-5

# Invent your own math problem (this can be addition, subtraction, multiplication, or division) and store the result as a variable. 
# Print a message that says, "The result of my math problem is: <stored result>." 
# So, if I said that my math problem was 1 + 1, my message would say, "The result of my math problem is: 2."


math_problem = (2 * 2) - 3 + 2 + (2 * 2)

print('\nThe result of my math problem is:',  math_problem)

# Chapter 3 Problems:

 

# Problem 3-1:

# Create a list of the last 4 books you've read. Print each book out, one at a time, in title case, with the message "I just read: " in front of it. 
# You may not use loops for this.

four_books = ['The Davinci code', 'Harry potter', 'Law of Attraction', 'Mastery']

print("\nI just read:", four_books[0].title())

 

# Problem 3-2:

# Make a list of your top 4 favorite TV shows that are actively being produced and store them as a list.

tv_show = ["Money heist", "You", "All American", "Queen of the South"]

# Now, pretend that one of them got cancelled. 

print('\nWe are sorry to announce the cancellation of '  + tv_show[1] + ' show')

# Replace the show that got cancelled with a new show you also like.

tv_show[1] = 'Will and Grace'

print('\nWe will be airing ' +tv_show[1] + ' in replacement.')

# Add two more shows to your list. 

# One must added using append() 

tv_show.append('Friends')

# and the other must be added using insert()
# The show you add using insert() cannot be added in the first or last position in the list.

tv_show.insert(2, 'Ru Paul"s drag race')

# Remove the last item from the list using pop() and print it out. 
print('\nRemoving last item from list using pop method.\n')
use_popmethod = tv_show.pop()

print(use_popmethod)
 
# Use a del statement to remove the first three shows from the list. Print whatever is left.

del tv_show[0:2]

print(tv_show)

# Problem 3-3:

# Consider any collection of data that you could store in a list. 
# For this exercise, you will need to store the collection in a variable and write a program that uses the following functions on the list at least once:
data_list = ["soccer", "football", "tennis", "badminton", "cycling"]

print('\nThe length of data list: ', str(len(data_list)))

# print the list using sort.

data_list.sort()
print('\nUsing sort on data list: ', data_list)

# Print list using sorted.
print('\nUsing sorted on data list: ', sorted(data_list))

# Print list using reverse.
data_list.reverse()
print('\nUsing reverse on data list: ', data_list, '\n')

# Problem 3-4:

# Write some code that has an indexing error in it. Underneath the code, write out a fix for the problem you created. Have the fixed code be commented out.
#print(data_list[5])

# Decreasing the index by 1 will do the trick.

# Seeing actual list or using len() to find out length of list will usually resolve this error.

# Chapter 4:

# 4-1:

# Think of four of your favorite places to visit. Store these locations in list, and then use a for loop to print out each item in the list.

# As you print out each location, add the phrase: "is a nice place to visit". So, if you had a list that had The Grand Canyon in it, it would print out as:

# The Grand Canyon is a nice place to visit
places = ['Grand Canyon', 'Niagara Falls', 'Venice', 'Boulder, CO']

print('\nI have always had it in mind to visit:\n')
for place in places:
    print(place, 'is a nice place to visit.\n')


# Problem 4-2:

# Use a for loop to print the numbers from 90 to 100, inclusive.

numbers = list(range(90, 101))

for number in numbers:
    print(number)
print()

# Problem 4-3:
# Create a list of numbers from 100,000 to 1,000,000. 
biglist_numbers = list(range(100000, 1000000))

# Calculate and print out the sum of all of these numbers.
print()
print(sum(biglist_numbers))

# Problem 4-4:
# Make a list of 20 numbers and place them in a random order (don't arrange them in ascending or descending order - make sure the list is truly random).

random_numbers = [23, 45, 67, 242, 95, 53, 0, 78, 54, 43, 67, 21, 25, 17, 82, 74, 66, 70, 91, 100]

# Calculate and print out the largest number in the list and the lowest number in the list.
print()
print(max(random_numbers))
print()
print(min(random_numbers))

# Problem 4-5:

# Make a list of multiples of 5 between 1 and 100. 

multiple_five = list(range(1, 100, 5))

# Once you have your list, print it out.

print('\n',multiple_five)

 

# Problem 4-6:
# Generate a list of values from 20 to 30 and print it out.

thelists = list(range(20, 30))
print('\n',thelists)

# Use a list comprehension to double each number in the list. Then, print out the list of doubled values.
doubled_values = [thelist * 2 for thelist in thelists]

print('\n', doubled_values)

# Problem 4-7:

# Using the list you generated in problem 4-4, use slices to:

# Print the first 2 values in the list

print(multiple_five[0:2])

# items 5-10 in the list
print(multiple_five[4:10])

# Print the last 4 items in the list
# Before you print out each list, be sure to include a message stating what it is that you are printing out.

print(multiple_five[-4:])
print('\nFind below the last 4 items of the list generated at question 4-4:\n')
for item in multiple_five[-4:]:
    print(item)

# Problem 4-8:

# Make a list of three of your favorite musicians or bands.
musician = ['justin timberlake', 'lizzo', 'amy winehouse'] 
# Then, copy that list to another variable. 
musician_copy = musician[:]

# Add a musician or band to the original list. 
musician.append('adele')

# Then, print out both lists to prove that they are different lists.
print('\nOriginal list:\n',musician)

print('\nCopy:\n',musician_copy)

# Problem 4-9:

# A school only has the following grades in it: 1st, 2nd, 3rd, 4th, and 5th.
# Store these grades in a tuple and then attempt to modify one of the values using list syntax.

grades = ('1st', '2nd', '3rd', '4th', '5th')

# grades.insert(4, '6th')



# ###############     Week 6 - Variables and Simple Data Types Assignment     ###############

# For this assignment, you need to submit a Python program that does the following:

# Stores your first name as a variable. Use all lowercase letters when you declare it.

fname = "karim"


# Stores your last name as a variable. Use all uppercase letters when you declare it.

lname = "MOH'D"

# Prints out, "Hello, <first name> <last name>" with the first name converted to uppercase letters and the last name converted to lowercase letters using string functions.
print("\nHello " + str(fname).upper() + ' ' + str(lname).lower())

# Prints out two newlines.
print('\n\n')

# Prints out the following:

# 'Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi'
# Your output must have quotes at the beginning and the end of your outputted text.

print("\n'Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi'\n")


# Stores 2 decimal numbers as variables.

num1 = 23.4

num2 = 10.4



# Stores one addition, one subtraction, one multiplication, and one division operation of these variables as variables.
addition = num1 + num2
subtraction =  num1 - num2
multiplication = num1 * num2
division = num1 / num2


# Prints out each of the four results as:

# <numeric value of variable 1> plus <numeric value of variable 2> equals <value of variable that stored the result of addition>.

print(str(num1) + ' plus ' + str(num2) + ' equals ' + str(addition), '\n')

# <numeric value of variable 1> minus <numeric value of variable 2> equals <value of variable that stored the result of subtraction>.

print(str(num1) + ' minus ' + str(num2) + ' equals ' + str(subtraction), '\n')

# <numeric value of variable 1> multipliedby <numeric value of variable 2> equals <value of variable that stored the result of multiplication>.

print(str(num1) + ' multiplied by ' + str(num2) + ' equals ' + str(multiplication), '\n')

# <numeric value of variable 1> divided by <numeric value of variable 2> equals <value of variable that stored the result of division>
print(str(num1) + ' divided ' + str(num2) + ' equals ' + str(division), '\n')

# Stores the current month as a string variable (e.g. March, June, etc.) and day of the month as a numeric variable.
month = 'october'

day = 12

# Outputs "Today is day <day of month> of the month of <month variable>. This should be on a new line and tabbed over two times.

print('\nToday is day ' + str(day) + ' of the month of ' + month)


###############     ###############     Week 6 - Working with Lists Assignment     ###############     ###############

# For this assignment, you need to submit a Python program that does the following:

#1  Create a list of all of the courses that you have taken at Walsh College. Each course should be listed in all lowercase letters when you store them.
courses = ['maths', 'chemistry', 'arts', 'biology']


# 2 

# Sort that list and print each element in that list with a message "I have taken <course> at Walsh College.".

# The value of <course> should be in all uppercase letters
courses.sort()

print('\nI have taken the modules listed below at Walsh College:\n')
for course in courses:
    print(course.upper())


# 3 

# Add courses that you plan to take next term to your list.
courses.append('physics')
courses.append('zoology')

# re-sort it.
courses.sort() 

# Print out each element in your list. 
# Before you print out your list, add the message, "This is my course of study with upcoming courses added:".
print("\nThis is my course of study with upcoming courses added below:\n")
for course in courses:
    print(course)



#4  Next, remove any course you have taken already from the list and print each course you removed out.

# Before printing out the courses you removed, add the message, "I do not have to take these courses:".
removed_courses = [courses.pop(0), courses.pop(0), courses.pop(0), courses.pop(0)]
print("\nI do not have to take the courses listed as follow:\n")
for course in removed_courses:
    print(course)


#5 Next, print out each item in your list of courses left in your list on its own line with the message, 
# "I plan to take the following courses next term" above the list.
print('\nI plan to take the following courses next term:\n')
for course in courses:
    print(course)

# 6 Create a list of numbers from 1 to 1000 that are divisible by 6.
print('\n')
div_six = [num for num in list(range(1, 1000)) if num % 6 == 0]

print(div_six)

# 7 Print out the first 20 numbers in that list, each on its own line. 
# Before this list is printed out, print the message, "Here are twenty numbers divisible by 6."

print('\nHere are twenty numbers divisible by 6.')
for num in div_six[:20]:
    print(num)

# 8 Calculate the maximum number of the original large list using Python and store this value as a variable.

maximum_num = max(div_six)


# 9 Print out the maximum number variable in the list with the message, "The maximum value in the list is: <max number variable>"
print("\nThe maximum value in the list is:", maximum_num)



# Calculate the sum of values in the original large list that are between the 10th value in the list and the 50th using Python.
#  and store the value of the sum as a variable. Print out the sum with the message, "Here is the sum of several values in the list: <sum of values variable>"

sumof_values = sum(div_six[10:50])

print("\nHere is the sum of several values in the list:", sumof_values)

# Overwrite the variable that originally contained the list of courses you have taken at Walsh 
# with the original large list of numbers you created for requirement #6.

courses = div_six