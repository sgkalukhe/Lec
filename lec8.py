#nested loop

#student appear or not - marks cheak for them
#
# apper=input("appear to the exam yes or not")
#
# if apper=="yes": #no
#     print("proccessing")
#     marks=int(input("Enter your marks"))
#     if marks>=35:
#         print("You are passed")
#     else:
#         print("Sorry try next time")
# else:
#     print("No problem try next year")

# num=int(input("Enter the number"))
# if num>=0:
#     print("Number is positive")
#     if num%2==0:
#         print("Number is Even")
#     else:
#         print("Number is odd")
# else:
#     print("Number is negative")
#     if num%2==0:
#         print("Number is Even")
#     else:
#         print("Number is odd")
#

#Loops

# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)


# num=int(input("Enter your number"))
# for i in range(1,11):
#     print(num*i)

# for i in range(1,31,2):
#     print(i)


#list,tuple,dict,set

# student_name=['mauli','shubham','roshan','omkar']
# for name in student_name:
#     if name=='roshan':
#      print(name)

#
# marks=[1,2,3,4,5]
# for i in marks:
#     print(i+5)

#
# sub='python'
# for i in sub:
#     print(i)


# numbers=(1,2,3,4,5)
# for i in numbers:
#     print(i+1)


#break

# list=['mauli','shubham','omkar','roshan']
# for i in list:
#     print(i)
#     if i=='omkar':
#         break
#


# for i in range(1,31):
#     if i%2==0:
#         print(i)
#     if i==20:
#         break

for i in range(3):
    password=input("Enter your password")
    if password=="shubham@123":
        print("Correct")
        break
    elif i==2:
        print("your out of attemt")
    else:
        print("wrong password")


