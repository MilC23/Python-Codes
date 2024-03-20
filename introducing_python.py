#print('morgan')
name = 'morgan'
#print(name)
#This is a comment
#This is multiple assignment in python
name, age, Class = 'morgan', '24', 'Data Science'
#print(name)
#print(age)
#print(Class)

#Data types in python
#strings(str) = words enclosed in a quote
#boolean(bool) = statements that are either True or False
#integers(int) = Whole numbers
#floats(float) = decimal numbers
#height = 196.8
#physicalStudent = True
#print(physicalStudent)
#print (not physicalStudent)

#commonly used inbuiltwords in python
#print = gives us an output
#len = gives us the number of characters in a string
#not = negates a statement
#str(), int(), float(), bool()* = datatypes

#operators in python
#+ - addition
#- -- subtraction
#/ - division
#% - modulus;gives a remainder
#* - multiplication
#print(9%5)

#Typecasting in python = combining two or more data types in pythonstudent_name = 'Morgan'
#age = 24
#height = 197.6
#physicalStudent = True
#print('Morgan, who is 24 years old and 197.6 cm tall, is a physical student')
#print(student_name+ ', who is '+str(age)+ ' years old and ' +str(height)+'cm tall, is a physical student: '+str(physicalStudent))
#Accepting user input in python
#name = input('please enter your name: ')
#password = int(input('please enter your password: '))
#print('you are '+name+' and your password is '+str(password))
#working with strings in python
#name = 'messi'
#print(name)
#print((len(name)))
#print(name*3)
#print(name.lower())
#print(name.upper())
#print(name.count('e'))
#print(name.isalpha())
#print(name.find('s'))
#print(name.capitalize())
#index,denoted by [], is the position of an element in a variable; often starting from 0

#typecasting in python
#x, y, z = 1, 2.0, '3' #multiple assignment
#print('x is ' +str(x))
#z = int(z)


#string slicing in python(extraction of part of string)
#name_2 = 'Techsavannah Software Institute'
#first_name = name_2[0:13]
#print(first_name)
#last_name = name_2[7:16]
#print(last_name)
#funky_name = name_2[0:16:2]
#print(funky_name)
#reversed_name = name_2[::-1]
#print(reversed_name)

#slicing part of a string
#website = 'https://google.com'
#slice = slice(8,-4,1)
#print(website[slice])
#print(website[8:-4])

#data structures in python include lists, tuples, sets and dictionaries
#list -- working with lists, enclosed in []
#Morgan_shopping_list = ['shoes', 'toothpaste', 'books', 'pens', 'clothes']
#print(Morgan_shopping_list)
#print(type(Morgan_shopping_list))
#Morgan_shopping_list.append('Mathematical set')
#print(Morgan_shopping_list)
#Morgan_shopping_list.remove('shoes')
#Morgan_shopping_list.insert(0, 'shoes')

#Morgan_shopping_list.count()
#print(Morgan_shopping_list)

#Morgan_shopping_list = ('Shoes', 'shoes', 'toothpaste', 'books', 'pens', 'clothes')
#print(Morgan_shopping_list)
#print(type(Morgan_shopping_list))
#print(len(Morgan_shopping_list))
#y = list(Morgan_shopping_list)
#print(type(y))
#y.append('toothpaste')
#print(y)
#y = tuple(y)
#Morgan_shopping_list = tuple(y)
#print(Morgan_shopping_list)
#Morgan_shopping_list.

#Morgan_shopping_list = {'shoes', 'toothpaste', 'books', 'pens', 'clothes'}
#y = list(Morgan_shopping_list)
#alter the contents of a list before changing it back to set
#Morgan_shopping_list = set(y)

#Dictionary
# house = {
#     'furniture': 'Chair',
#     'Electronics': 'T set',
#     'clothes': 'Trousers'
# }
# x = house.items()
# print(x)
# house['clothes'] = 'shorts'
# print(x)
#print(house)
#print(type(house))
#mansion = {
   # 'furniture': ['Chair', 'tables', 'beds'],
  #  'Electronics': {'T set', 'Radios'},
 #   'clothes': ('Trousers', 'T-shirts'),
#}
#print(mansion)


#loopss
#numbers = [1,2,3,4,5,6,7,8,9]
#for number in numbers:
    #print(number,end='-')

#4>2
#while True:
 #   print('Four is always greater than two')
  #  break

# def greeting():
#     print('hey, Morgan')
# greeting()
#arguments in python #single argument
# def greeting(name):
#     print('hey, '+name+',')
# greeting(name='Morgan')

#double arguments
# def greeting(first_name,second_name):
#     print('hey, '+first_name+second_name)
# greeting(first_name='Ngundi',second_name='Morgan')

#args #arrange in a tuple
#def greeting(first_name,second_name):
#     print('hey, '+first_name+second_name)
# greeting(first_name='Ngundi',second_name='Morgan')

#**kwargs

# def greeting(*name):
#     print(f'hey {name[0]} your friend is {name[1]}')
#     print(f'hey {name[2]} your friend is {name[3]}')
# greeting('Ngundi','john','mike','Morgan')

# def greeting(**Name):
#     for key, value in Name.items():
#         print(f'{key}:{value}')
# greeting(name='Ngundi',age=25, position='data scientist')

# def courses(**courses):
#     for course_name, marks in courses.items():
#         print(f'{course_name}:{marks}')
# courses(statistics=78, mathematics=60, biology=87)
#
#
# def courses(**courses):
#      for course_name, marks in courses.items():
#           print(f"{course_name}:{marks}")
# courses(Statistics=78, Mathematics = 90, Biology = 56)
#

#OOP(OBJECT ORIENTED PROGRAMMING) IN PYTHON
#Classes and objects

# def man():
#     print('blabla')
#     man()
#
# class man:
#     #is he a human being = True #attribute
#     def __init__(self, name):
#         self.name = name   #initialization
#
#     def neverCeaseTrying(self):
#         print('{}'.format(self.name)+ ' is always a hardworking man')   #instance
# Morgan = man('Morgan')  #object
# Mestar = man('Mestar')
#
# Morgan.neverCeaseTrying()
# Mestar.neverCeaseTrying()

# class counties:
#     def __init__(self,county):
#         self.county = county
#
#     def readbudget(self):
#         print('{}'.format(self.county)+' has read its budget')
#
# # Kisumu = counties('Kisumu')
# # Mombasa = counties('Mombasa')
# # Nakuru = counties('Nakuru')
# #
# # Kisumu.readbudget()
# # Mombasa.readbudget()
# # Nakuru.readbudget()
#
# class countryKenya(counties):
#     pass
# Kisumu = counties('Kisumu')
# Mombasa = counties('Mombasa')
# Nakuru = counties('Nakuru')
#
# Kisumu.readbudget()
# Mombasa.readbudget()
# Nakuru.readbudget()

# class animals:
#     def __init__(self,rodent):
#         self.rodent = rodent
#
#     def eat(self):
#         print('{}'.format(self.rodent)+' has eaten everything')
#     def run(self):
#         print('{}'.format(self.rodent)+' has run away')
#
# Mole = animals('Mole')
# Rabbit = animals('Rabbit')
# Rat = animals('Rat')
#
# class rodents(animals):
#      pass
# Mole = animals('Mole')
# Rabbit = animals('Rabbit')
# Rat = animals('Rat')
#
# Mole.eat()
# Rabbit.eat()
# Rat.eat()
#
# Mole.run()
# Rabbit.run()
# Rat.run()
#
# Polymorphism
# methods/functions/operators with the same name that can be executed on many objects or classes
# 1.Function polymorphism
# #len()
# -string - returns the number of characters
# -tuple - returns the number of items in the tuple
# -dict - returns the number of key/value pairs
#
# 2.Class polymorphism
# -multiple classes with the same method name
# *car,boat and plane(move)
#
#
# *inheritance class polymorphism
# -use vehicles as parent then (car,boat,plane) as children
#
# Encapsulation
# -principle that involves buildind data(attributes) and methods(functions) that operate on the data within a single unit known as class
# -this helps in hiding the internal details of the class and restrivting direct access to certain attributes or methods from outside the class
# -attributes and methods prefixxed by __ are considered private
#

















print('Is that your ass in the background?HAHAHA')




