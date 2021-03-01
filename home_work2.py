# # python (1)
# name = "yogesh"
# age = 24
# print("hello " + name + " your age is " +str(age)) # ugly syntax

# #python (3) string formatting
# print("hello {} your age is {} ".format(name, age))
# # {} this is place holder
# print("hello {} your age is {} ".format(name, age + 2))

# #python 3.6 string formatting
# print(f"hello {name} your age is {age}") # clean format
# print(f"hello {name} your age is {age + 2}")

# # 3 Liner code
# Name = "Anurag"
# value = 50
# print(f"hello {Name} the average of 3 values is {value + 50+50/100}")
# # 2 Liner code
# value = 50
# print(f"hello Anurag the average of 3 values is {value + 50+50/100}")
# # 1 Liner code
# print(f"hello Anurag the average of 3 values is {50+50+50/100}")
# # 2 Liner code ##
# n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# print(f"Hello Anurag the average of 3 values is =  {int(n1) + int(n2) + int(n3) /3}")

# n1=("Kindly insert your name = ")
# print("n1"[-1::-1])

# Ask user his username ad print it in reverse.make it in two lines.
# Name = input("Kindly insert your name = ")
# print(str(Name)[-1::-1])
# print(str(Name).lower())
# print(str(Name).upper())
# print(str(Name).title())

# Take 2 comma input seperated from user (name & single character),
# find user name length, find the single character count in the name.
name,chr=input("kindly insert 2 values Name & Single Character seperated by comma = ").split(",")
# print(len(name)+" "+name.count(chr))
print(f"length of the name is {len(name)} character count is {name.count(chr)}")