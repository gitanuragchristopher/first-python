# first_name=input("Please enter your First Name = ")
# last_name=input("Please enter your last Name = ")
# print("Hello how are you Boss "+first_name + " " +last_name)
# age=input("enter your age = ")
# new_age=int(age)
# final_age=new_age-10
# f_age=str(final_age)
# # print("You are young ="+f_age)
# print("You are young ="+str(final_age))
# print("your new age is " +new_age)
#what is the variable name in which the value of first name will be stored?
#when ever we use input function we will get value as "String"
# now we have to do data type conversion data into integer.
# we understand type casting converting data types (str or int)

#======================================================================

# # name,age="Anurag","33"
# print("Hello " +name +" your age is "+ age)

# name,age=input("Enter your name and age").split()
# print("Hello " +name +" your age is "+ age)
# n1,n2,n3=input("kindly insert 3 values seperated by space").split()
# #need to input 3 values
# new_n1=int(n1)
# #convert string to integer
# new_n2=int(n2)
# #convert string to integer
# new_n3=int(n3)
# #convert string to integer
# n4=new_n1+new_n2+new_n3
# #declaire 4th varibale to calculate sum
# print("The sum is = " +str(n4))
# # print the sum in form of string, type cast back to string


# python (1)
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

# n1,n2,n3=input("kindly insert 3 values seperated by space").split(",")
# n4=
# print(average is = +n1+n2+n3)

# print(f"kindly insert 3 values seperated by comma {name} your age is {age}").split(",")
print(f"kindly insert 3 values seperated by comma {,} your output is {age 3/2}")

##string Indexing
prg_lang = "python"
# p = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2
# n = 5, -1
#print (prg_lang[1]) # output is 'p'
#print (prg_lang[6]) # you get error
print (prg_lang[-1]) # output is 'n'
#print (prg_lang[-7]) # you get error

=============================================

#string slicing is used to fetch values within a starting and ending range
#syntax [start argument : stop argument -1]
prg_lang = "python"
print(prg_lang[0:4]) #output is pyth
print(prg_lang[-3:6]) #output is hon
print(prg_lang[3:]) #output is hon
print(prg_lang[:3]) #output is pyt 

n1=("Kindly insert your name = ")
print
