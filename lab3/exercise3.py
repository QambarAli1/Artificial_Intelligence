import datetime
#### LAB TSAKS

## Exercise 1

## I. a Python program to square and cube every number in a given list of integers using Lambda. 

nums = [1, 2, 3, 4]
square_nums = list(map(lambda x: x**2, nums))
cube_nums = list(map(lambda x: x**3, nums))
print(square_nums)
print(cube_nums)

list_1 = [1,2,3,4]
square = lambda a : a*a
cube = lambda a : a*a*a
def suqareAndCube(lst):
    for i in lst:
        print(square(i))
        print(cube(i))
suqareAndCube(list_1)




## II. a Python program to find if a given string starts with a given character using Lambda. 

check_char = lambda full_word,char: True if full_word.startswith(char) else False;
print(check_char("Qambar","Q")) 


## III. a Python program to extract year, month, date and time using Lambda. 
now = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time
print(year(now))
print(month(now))
print(day(now))
print(time(now))


## Exercise 2
## Q1

cities_data =  open('cities.txt','x')
cities_data =  open('cities.txt','a')
cities_data.write("City Population Mayor")
def addCity():
    cityName = input("Enter City Name: ")
    population = input("Enter Population: ")
    mayorName = input("Enter Mayor Name: ")
    cities_data.write(f'\n{cityName} {population} {mayorName}')
addCity()


## Q2
student_data =  open('student.txt','x')
student_data =  open('student.txt','a')
student_data.write("Now we are AI students")
