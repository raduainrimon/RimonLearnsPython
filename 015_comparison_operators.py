# temp = input("Type temperature: ")
# print(int(temp))
# if int(temp)>30:
#     print("It's a hot day")
# elif int(temp)<30:
#     print("It's a cold day")
# else:
#     print("It's neither hot nor cold")



# #Exercise
# '''
# if name is less than 3 characters long
# name must be at least 3 characters
# otherwise if its more than 50 characters long
# name can be a maximum of 50 characters
# otherwise
# name looks good
# '''
name = "Raduain Rimon"
#name = input("Type name: ")
print(len(name))
if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name can be a maximum of 50 characters")
else:
    print("name looks good!")