
#git@github.com:sigzer/Python-Exercises.git

#Write a program to find whether a given number (accept from the user) is even or odd,
#print out an appropriate message to the user.


number = int(input ("Enter a number: "))


if number % 2 == 0:
    print(f"The number {number} is an even number")
else:
    print(f"The number {number} is an odd number")

#Write a program to check whether a number entered by the user is positive, negative or
#zero.


number = int(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive")
elif number < 0:
    print(f"The number {number} is negative")
else:
    print(f"The number {number} is exactly zero")

#Write a program to display the calendar of a given date.
#i made a change here

yy = int(input("Enter today's year: "))
mm = int(input("Enter today's month: "))
dd = int(input("Enter today's day: "))

calendar = (f"{yy}-{mm}-{dd}")

print(calendar)

#Write a program to ask the user to enter the string and print that string as output of the
#program.


def check_enter(enter):
    try:
        value = int(enter)
        print(f"The value: {value}, you entered is, ", type(value))
    except ValueError:
        try:
            value1 = float(enter)
            print(f"The value: {value1}, you entered is, ", type(value1))
        except ValueError:
            print("The input is a string")

enter = input("enter something: ")
check_enter(enter)

#Write a program to concatenate two strings.


string_one = str(input("Enter the first string: "))
string_two = str(input("Enter the second string: "))

string_final = string_one + " " + string_two
print(string_final)

#Write a program to check if an item exists in the list

myList = ['narancs', 'alma', 'korte', 98, 43.9843, True, 5843]

s = 'narancs', 'alma', 'korte'
matched_indexes = []
i = 0
length = len(myList)

while i < length:
    if s == myList[i]:
        matched_indexes.append(i)
    i += 1

print(f"matched indexes are: {matched_indexes} in the list: {myList}")

#Write a program to join two or more lists

list_one = ['This', 'is', 'list', 1]
list_two = ['This', 'is', 'not', 'list', 1, 'but', 'list', 2]
list_three = [3, 333, 33, 3.33]

#this is the part where I join more strings together
all_lists = list_one + list_two + list_three
word = 'is'
#at this statement I wanted to remove all the 'is' strings 
#i had to do it twice, because .remove(*) only removes the first element 
if all_lists.count(word) > 1:
    print(all_lists.remove(word), all_lists.remove(word))
    print(all_lists)
else:
    print("shitas")


#Write a program to calculate cube of a number.

x = float(input("Enter a number: ")) # I did it with float numbers so we can calculate the cube of int and float numbers
y = x ** 2 

print(y)

#Write a program to calculate square root of a number

x = float(input("Enter the number which you want to know the root: "))
y = x ** (1 / 2)

print(y)

#Write a program that takes a list of numbers (for example, i = [6, 10, 75, 60, 55]) and
#makes a new list of only the first and last elements of the given list.

i = [6, 10, 75, 60, 55]
 #   0   1   2   3   4 

new_list = i[0], i[-1]
make_new_list = list(new_list)
print(make_new_list)


#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.

enter = list(input("x = "))
i = enter[-1]

if enter[0] == i:
    print('true')
else:
    print("false")



