#calculating year
birth_year= input("Type Birth Year: ")
#age = 2024 - birth_year #WRONG
#age = 2024 - '1999' #different type
age = 2024 - int(birth_year) #type-casting
print(age)
# print(type(birth_year)) #to identify data types
# print(type(age))

# #Exercise
# ''' Ask a user their weight (in pounds),
# convert it to kilograms and print on the terminal '''
# # 1 pound = 0.453592 kg
# weight_pound = input("Type your weight (lbs): ")
# in_kg = int(int(weight_pound) * 0.45)
# print(in_kg)