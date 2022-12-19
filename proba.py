
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








