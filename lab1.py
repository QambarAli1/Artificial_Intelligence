###### Exercise: Dir and Help 

# import math
# import random
# var1 = 'hello world'
# print(dir(var1))
# print(help(var1.find))
# print(var1.find('o'))


###### Exercise Python input /output Basic operations
### Q1

# a = 2
# b = 56
# c = 78
# d = 9
# a,b,c,d = d,c,b,a
# print('a = ' , a )
# print('b = ' , b )
# print('c = ' , c )
# print('d = ' , d )

### Q2
# print("Enter 1 for Celsius to Fahrenheit.\nEnter 2 for Fahrenheit to Celsius.")
# option = int(input())
# if(option == 1):
#     Celsius = float(input("Temperature in Celsius: "))
#     Fahrenheit = Celsius*(9/5)+32
#     print("Temperature in Fahrenheit : ",Fahrenheit)
# elif(option == 2):
#     Fahrenheit = float(input("Temperature in Fahrenheit: "))
#     Celsius = 5*((Fahrenheit-32)/9)
#     print("Temperature in Celsius : ",Celsius)
# else:
#     print("Enter a valid option")


###### Exercise: Lists 
### Q1 
# list1 = [ 1, 2, 3, 4, 5, 1, 2 ]
# list1.reverse()
# list1.append('1')
# print(list1)


### Q2
# list2 = [ 'hello', 'world', '1234', '4321' ]
# print(list2.count('1234'))


###### Exercise: Dictionaries 
### Q1 
# user = { 'id': 1, 'first_name': 'Qambar' , 'last_name': 'Ali', 'position': 'React JS Developer' }
# print(dir(user))
# print(user.pop('id'))
# print(user.get('id'))
# print(user)
# user.clear()
# print(user)


### Q2 
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={**dic1,**dic2,**dic3}   
# print(dic4)



###### Exercise: List Comprehensions 
### Q1
# names = [ 'QAMBAR', 'ALI', 'KARACHI', "PAKISTAN" ]
# for i in range(len(names)):
#     if(len(names[i]) > 5):
#         print(names[i].lower())
#         names[i] = names[i].lower()
# print(names)


### Q2 
# colors  =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
# del colors[4:6]
# colors.remove(colors[0])
# print(colors)


###### Exercise : Operators:

# x = 6
# if (type(x) is int):
#  print ("true")
# else:
#  print ("false")
### Output = true


# x = 7.2
# if (type(x) is not int):
#  print ("true")
# else:
#  print ("false")
### Output = true


# list1=[1,2,3,4,5]
# list2=[6,7,8,9]
# for item in list1:
#  if item in list2:
#     print("overlapping")
# else:
#  print("not overlapping")
### Output = not overlapping


# a=6.3
# a//=3
# a**=5
# print('floor divide = ',a)
# print('exponent = ' ,a)
### Output = floor divide =  32.0
### Output = exponent =  32.0


# a=60
# b=13
# c=a&b   
# d=a|b   
# e=a^b   
# f=~a    
# g=a<<2  
# h=a>>2  
# print("Line 1 ",c)
# print("Line 2 ",d)
# print("Line 3 ",e)
# print("Line 4 ",f)
# print("Line 5 ",g)
# print("Line 6 ",h)



##### Function to print table
# def table(num):
#     for i in range(1,11):
#         print( num , ' x ' , ' = ' , i*num)
# table(9)


##### Function to print Even Numbers in list
# def evenNumber(inp_list):
#     for i in range(len(inp_list)):
#         if(inp_list[i]%2 == 0):
#             print(inp_list[i])
#     print(list)

# list22 = [ 3 , 2, 5, 8, 12, 10 ]
# evenNumber(list22) 