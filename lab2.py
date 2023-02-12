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





###################----- LAB EXERCISES -----####################
###----- EXERCISE 1 -----#####
##--- Q1

def calculateVolume():
    width = int(input("Enter Width : "))
    height = int(input("Enter Height : ")) 
    depth = int(input("Enter Depth : ")) 
    volume = width*height*depth
    print(f'Volume is {volume}')
    if volume >=1 and volume <=10:
        print("Extra Small")
    elif volume >=11 and volume <=25:
        print("Small")
    elif volume >=26 and volume <=75:
        print("Medium")
    elif volume >=76 and volume <=100:
        print("Large")
    elif volume >=101 and volume <=250:
        print("Extra Large")
    elif volume >= 251:
        print("Extra-Extra Large")
    else:
        print("Extra-Extra-Extra Large")

calculateVolume()


##--- Q2

time_taken = int(input('Enter time taken by worker: '))
if (time_taken >= 2) and (time_taken <=3):
    print('Highly Efficient!')
elif (time_taken >= 3) and (time_taken <=4):
    print('Improve Speed!')
elif (time_taken >= 4) and (time_taken <=5):
    print('Training is required to improve!')
elif (time_taken > 5):
    print('You are fired!')
else:
    print("Enter hours above 2 or equals!")


##--- Q3

username = 'qambarali'
password = 'QAMBAR@123'
inp_name = input("Enter Username: ")
inp_pass = input("Enter Password: ")
if(username == inp_name.lower() or password == inp_pass.lower()):
    print("Welcome! ")
else:
    print("Incorrect Credentials! ")




###----- EXERCISE 2 -----#####
##--- Q1

n = 3
while n >= 0:
    n -= 1
    print(n) 
## ANS = 2 1 0 -1



##--- Q1

n = 4
while n > 0:
    n -= 1
    print(n)


##--- Q2

# 0Make a program that lists the countries in the set
clist = ['Pakistan','Turkey','Canada','USA','Mexico','Australia']


## 1. Create a loop that counts from 0 to 100
for nums in range(1,101):
    print(nums)

## 2. Make a multiplication table using a loop
def table(num):
    for i in range(1,11):
        print(f'{num} * {i} = {num*i}')
table(6)

## 3. Output the numbers 1 to 10 backwards using a loop
limit = 10
while limit > 0:
    print(limit)
    limit -= 1

## 4. Create a loop that counts all even numbers to 10
highest = 10
even_count = 0
while highest > 0:
    if highest%2 == 0:
        even_count += 1
    highest -= 1
print(even_count)

## 5. Create a loop that sums the numbers from 100 to 200
sum = 0
for x in range(100,201):
    sum += x
print(sum)


##--- Q3

## 1. Make a program that lists the countries in the set below using a while loop.
c_list = ["Canada","USA","Mexico"]
numb = 0
while numb < len(c_list):
    print(c_list[numb])
    numb+=1