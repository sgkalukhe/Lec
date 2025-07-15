# laptop={'name':'HP','version':3.01,'Price':[25631,45632,98745]}
# print(laptop["name"])
# print(laptop["version"])
# print(laptop["Price"])

# print(laptop.get["name"])
# print(laptop["Version_"])
# print(laptop["version"])
# print(laptop["Price"])


# stu={'name':'priya','Marks':56}

name={'Pooja':50,'Kia':60,'Hina':78,'Rani':78}
# updated={k:v for k,v in name.items()if k=='Pooja' or k=='Hina'}
# print(updated)

updated_name={k:v for k,v in name.items() if k.startswith("R")}
print((updated_name))
