## IMPORT MODULES
import my_modules

#### PYTHON LAMBDA AND ARRAYS:
### 1
x = lambda a:a+5
print(x(4))

### 2
prod = lambda a,b : a*b;
print(prod(10,2));

### 3
sum = lambda a,b,c : a+b+c
print(sum(1,2,3))

#### Arrays
### 4
cars = ["Civic", "BMW", "Alto", "Cultus"]
cars[0] = "Vigo"
print(cars[0])
print(cars)
print(len(cars))
for x in cars:
    print(x)

#### FILE INPUT OUTPUT IN PYTHON:

## READ FILE
f = open('document.txt','r')
print(f.read())
f.close()

## APPEND TEXT IN FILE
file = open('./document.txt', 'a')
file.write("\nI am MERN Stack Developer")
file.write("\nI am student of UBIT")
file.close()

## OVERWRITE TEXT IN FILE
file_1 = open('document.txt', 'w')
file_1.write("\nI am MERN Stack Developer")
file_1.close()

## CREATES NEW FILE
new_file =  open('myfile.txt','x')
file_new = open('myfile.txt','w')
file_new.write("I have created a new file from pyhton")


#### PYTHON MODULES:
my_modules.greeting("Qambar")
my_modules.table(2)
print(my_modules.person1["name"])