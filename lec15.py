# var=[56,45,8,64,78,6,1,74,56,23,37,99]
# max_val=0
# for i in range len(var):
#     if var [i] >= var [i+1]:
#         max_val = var [i+1]
#     else:
#         i=i+1
#
# print(max_val)


# v=(4,5,6,78,9,12,3,6)
# v.append(56)
#
# print(v)


# v=(1,2,3)
# w=(1,5,3)
# print(v>=w)

# data=("hina",'Python','8am to 10am',"Mauli",'Java','8am to 10am')
# name,sub,time_,*other_data=data
# print(name)
# print(sub)
# print(other_data)
# print(time_)

scholership_names=('HDFC','Tata capital','yuva','Halidiram','mahadbt')
updated_scholership=(i for i in scholership_names if i=='HDFC' or i=='yuva')
print(tuple(updated_scholership))


