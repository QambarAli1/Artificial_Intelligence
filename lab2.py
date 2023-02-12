####----- EXAMPLE 1 -----#####
## Print square root of negative or positive number using if and operators.

num1 = int(input("Enter number to get Square root: "))
if num1 > 0:
    square = num*(1/2)
    print(f'square root of {num1} is {square}')
if num1 <= 0:
    print("Please Enter Positive number only !")


####----- EXAMPLE 2 -----#####
## Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between.

num2 = int(input("Enter 1 or 0 to revert it : "))
if num2 == 1:
    num2 = 0
elif num2 == 0:
    num2 = 1
else:
    print("Enter 1 or 0 only!")
print(num2)


####----- EXAMPLE 3 -----#####

num3 = int(input("Enter number between 10-20 : "))
if num3 <= 20 and num3 >= 10:
    print("Good! You have entered number in between 10-20! ")
else:
    print("Sorry! Entered number is out of range! ")


####----- EXAMPLE 4 -----#####

num4 = int(input("Enter number between 10-20 or 30-40 : "))
if (num4 <= 20 and num4 >= 10) or (num4 <= 40 and num4 >= 30) :
    print("Good! Entered number is in range! ")
else:
    print("Sorry! Entered number is out of range! ")



####----- CONTROL STRUCTURES LOOP -----#####
####----- EXAMPLE 1 -----#####
i = 0
while i < 100:
    print("Karachi")
    i += 1


####----- EXAMPLE 2 -----#####
## Take collection of number input from user. Print the total positive and negative number.

positive_count = 0
negative_count = 0
j = 0 
count = int(input("How many nums you want ot enter: "))
while j < count:
    user_num = int(input("Enter number: "))
    if( user_num >= 0):
        positive_count += 1
    else:
        negative_count += 1
    j += 1
print(f'positive count = {positive_count}')
print(f'negative count = {negative_count}')


####----- EXAMPLE 3 -----#####
## Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.

value = 'b'
userValue = input("Guess alphabet between a to e : ")
while (userValue != value):
    print("Wrong Answer")
    userValue = input("Guess alphabet between a to e : ")
print("Right Answer")





