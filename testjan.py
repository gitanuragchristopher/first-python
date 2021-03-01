# 1)Ask user to input 3 numbers in single line seperated by comma. Calculate the product and display message
# " The product of num1 and num2 and num3 is num4", using python 3.0 string formatting.

# n1,n2,n3=input("kindly insert 3 values seperated by comma =").split(",")
# #need to input 3 values
# t1=int(n1)
# #convert string to integer
# t2=int(n2)
# #convert string to integer
# t3=int(n3)
# #convert string to integer
# t4=t1*t2*t3
# #declaire 4th varibale to calculate sum
# print("The product of " +str(t1) +" and " +str(t2) +" and " +str(t3) +" is = "  +str(t4))

# # 2)
# # Display “My Name Is James” as “My**Name**Is**James”
# msg1 = '"My Name Is James"'
# msg2 = msg1.replace(" ","**")
# print(msg2)

# # 3)
# # Write a program to display below: escape sequences
# # \"  \'
# # n1 = ('"\\", "\\'"')
# n1=("\\\"\\\'")
# # \\=\,
# # \"=",
# # \'='
# print(n1)

# # # # 4)
# # # # WAP to print sad and smily emoji
# print("\U0001F606" "\U0001F600" "\U0001F923")

# # 5)
# # Create 2 string variables, 1st in camel case and 2nd in snake case
# n1="snake case user_1_anurag, "
# n2=" Camel Case is Not applicable in Python"
# print(str(n1)+str(n2))
# user_name_a= "Anurag"
# UserNameA= "Navneet"
# print(user_name_a + " " +UserNameA)

# # 6)
# # Ask user a number and convert it to float and print
# n1=input("Kindly insert Number = ")
# # print(int(n1) /100)
# n2=float(n1)
# print(n2)
# float = decimal number
# Int= whole number
# str= combination of text and numbers

# # 7)
# # Ask user to enter name and print only the first character
# name = input("Kindly Enter your Name = ")
# print(str(name)[0])
# print(name[0])

# # 8)
# # Ask user to enter the users full name and display his name skipping 1 character
# name = input("Kindly Enter your Name = ")
# # print(name[0::2])
# print(name[::2])

# # 9)
# # Ask user to enter his name and print in reverse order
# name = input("Kindly Enter your Name = ")
# print(name[-1::-1])

# # 10)
# # ask user his full name and display the same in Upper case, Lower Case, Title Case, display the length.
# # Also count the number of characters, excluding spaces
# Name = input("Kindly insert your name =")
# print(str(Name).upper())
# print(str(Name).lower())
# print(str(Name).title())
# print(len(Name),Name.count(""))
# print(Name.replace(" ",""))
# n1=(Name.replace(" ",""))
# print(len(n1))

# # 11)
# # Take two comma seperated inputs from user
# #1. user's name
# #2. a single character
# #output - print 2 lines
# #1. User's name length
# #2. count the number of times that character exists in his name.
# # Note that user can type the character in lower or upper case but program should still be able to count 
# msg3 = "she is beautiful and she is good dancer, Navneet sir woke up late again, but sir ki to "
# pos1 = msg3.find("sir")
# name,chr=input("kindly insert 2 values Name & Single Character seperated by comma = ").split(",")
# print(f"User's name length {len(name)} character count is {name.count(chr)}")
# # print(str(name).lower())
# n1=name.lower()
# n2=chr.lower()
# print(n1.count(n2))

# # 12)
# # Ask user to enter a message and then print that message back without spaces
# Name = input("Kindly insert your name = ")
# msg = Name.replace(" ","")
# print(msg)

# # 13)
# # Ask user to enter his name and add 4 * before and after his name
# name = input("Enter your name : ")
# print(name.center(len(name)+8, "*"))

# # 14) (Issue)
# # Ask user to enter his name and print first 2 character and last 2 character his name
# name = input("Kindly Enter your Name = ")
# # print(name[0:2])
# # print(name[-2:])
# print(name[0:2] + "," + name[-2:])


# # 15)
# # Ask user to input 3 numbers and you have to print average of three numbers using string formatting.
# n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# print(f"Hello Anurag the average of 3 values is =  {(n1) + (n2) + (n3) /3}")

# n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# print(f"Hello Anurag the sum of 3 values is =  {int(n1) + int(n2) + int(n3) /3}")
# print("The sum is = " +str(t4))
# Python 3.6 formating
# n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# # print(f"Hello Anurag the sum of values is =  {int(n1) + int(n2) + int(n3)}")
# n4= int(n1) + int(n2) + int(n3)
# # print(n4)
# print(f"The sum of values is {n1},{n2},{n3} =  {int(n1) + int(n2) + int(n3)}")
# # print(f"Hello Anurag the sum of 3 values is =  {n1}{n2}{n3} ")

# n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# print(f"Hello Anurag the sum of values is =  {int(n1) + int(n2) + int(n3)}")
# n4= int(n1) + int(n2) + int(n3)
# print(n4)
n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
print(f"The sum of values is {n1},{n2},{n3} =  {int(n1) + int(n2) + int(n3)}")
# print(f"Hello Anurag the sum of 3 values is =  {n1}{n2}{n3} ")
