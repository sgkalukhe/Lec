#Indexing
from builtins import PythonFinalizationError

# st="hey Welcome to the seven mentor"

# print(st[0])
# print(st[3])
# print('Hello')
#
# print(st[-1])
# print(st[-5])
# print(st[-32])   #string index out of range
# print(len(st))

#Sclicing

# var="hey Welcome to the seven mentor"
#
# # print(var[Start:End:Jump]):
# print(var[0:7])    #hey Wel
# print(var[:7])     #hey Wel
# print(var[0:])     #give complete string   =hey Welcome to the seven mentor
# print(var[::2])    #Jump   = hyWloet h ee etr
# print(var[0::3])   # = h lmtt v nr


# name="Shubham Ganesh Kalukhe"
# print(name[0:7])   #Shubham
# print(name[8:14])  #Ganesh
# print(name[15:22]) #Kalukhe

# var='Python'
# print(var[-4:-1])
# print(var[-5:-1])
#
# print(var[-5:])
# print(var[::-1])
#
# print(var[-6:-4])
# print(var[-2:])

# var='Hey how are you'
# var[0]="gh"  #Erroe String is inmuttable

#remove

#var.remove("hey")  #Error
# del var
# print(var)

# print("Hello"+" "+"Student")
# print("Hello"+"Student")
# print("s"*4)

#Comparision Operator
# print("Python"=="Java")

# print("Hello","Student",end='\n')


# var="Python"
# print(len(var))
# print(type(var))
# print(max(var))
# print(min(var))


# Case Conversion

#Upper case conversion
# user_input=input("Enter your name")
# print(user_input.upper())

# lowert case conversion
# user_input=input("Enter the Name")
# print(user_input.lower())

# user_input=input("password")
# u=user_input.lower()
# if u=="shubh@123":
#     print("Correct")
# else:
#     print("Wrong")

#Title :- Convert first leyyer of each word into a capital letter.
# user_input=input("Enter")
# print(user_input.title())

# Capitallize:-Make firswt letter of first word capitle
# user_input=input("Enter the Name")
# print(user_input.capitalize())

#swapcase
# user_input=input("Enter the Name")
# print(user_input.swapcase())

# var="python"
# print(var[0].upper())
# print(var[0:4].upper())
# print(var[0:4])

#find = find gives the first occurance of the charactor
#otherwise -1
# var="python is easy is"
# print(var.find("is"))
# print(var.rfind("is"))


#index = First occurence ortherwise error1
# print(var.index("easy"))

# Trimming
#streip.lstrip,rstrip

# var="   Python "
# var1=" python Word "
# var2='@python@'
#
# print(var.strip(" "))
# print(var1.strip(" "))
# print(var2.strip("@"))

# # lstrip
# var="...Python..."
# print(var.lstrip("."))
#
#
# #rstrip
# var="...Python..."
# print(var.rstrip("."))


# var="$  Python  $"
# print(var.strip("$"))
# print(var.lstrip("$"))
# print(var.rstrip("$"))

# msg="Java is dynamic language"
# print(msg.replace('Java','Python'))
# print(msg)
#
# up_=msg.replace('Java','Python')
# print(up_)
#
# print(id(up_)==id(msg))

#Count :- How many time value is repeted

# var="Hello python use"
# print(var.count("e"))


