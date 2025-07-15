#Dictionary
from operator import truediv
from unittest.util import unorderable_list_difference

#Dont get indexing
# get order
# key value pair
#Duplicate keys are not allowed

# student_name={'name':'Shubham','Role':'Student','Batch':'Python'}
# print(student_name)
# print(type(student_name))


#set
# unordered
# nonindexing
# duplicate non allowed
#
# Date_of_birth={'12/02/2005','17/06/2005'}
# print(Date_of_birth)

# None data type

# variable=None
# print(variable)
# print(type(variable),id(variable))
#
# variable=10
# print(type(variable),id(variable))


#Data Casting

# num='10'
# print(int(num))
#
# var=True
# print(float(var))
#
#
# set={10,20,20,30,40,30}
# tup=(11,22,33,44)
# dict={'name':'mauli'}
#
# print(list(set))
# print(list(set))
# print(list(dict))
#
# list=['mauli','shubham']
# print(dict(list))

#list

#
# top1=(1,2,3,4)
# list1=[5,6,7,8]
#
# #print(top1+tuple(list1))
# print(list(top1)+list1)



#input function
#input

# user=input("Please Enter name")
# print("Welcome to python class",user)

#Ask age and then class name and print both

age=input('Enter your age')
class_name=input('In which class')

print('my age is',age)
print('I am studying in',class_name)