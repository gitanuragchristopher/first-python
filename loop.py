# while loop
# starting value
# condition
# starting value will increase or decrease after every run.

# i = 1
# while i<=50:
#     # print("Hello World")
#     print(f"This is loop no {i}")
#     i = i + 1

# i = 50
# while i>=1:
#     # print("Hello World")
#     print(f"This is loop no {i}")
#     i = i - 1




# # print the table of 5
# i = 1
# while i<=10:
#     n=5
#     print(f"5 x {i} = {n*i} ")
#     i = i + 1
# # =================================
# sum of 1 to 10 (1+2+3 like that)
# usr = input("Tell me the number till which you find out the Sum = ")
# x = 1
# y =int(usr)
# sum = 0
# while x<=y:
#     sum = sum + x
#     x = x + 1
# print(f"The sum from {1} to {y} =  {sum} ")

# sum of 1 to 10 (1+2+3 like that)?????

# print numbers from 1-10?
# x = 1
# while x<=10:
#     print(f"Print {x}")
#     x = x + 1
    
# ========================================================================

# #Example: Input user name and add 4 * before and after name
# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# Nested loop

# print 1-100 even numbers
# n1 = input("Kindly input Number = ")
# # x = 1
# n2 = int(n1)
# n3 = n2%2
# print(n3)

# if (n3==0):
#     print("This is Even Number")
# else:
#     print("This is Odd Number")
# print 1-100 even numbers

# x = 1
# y = 0
# while x<=100:
#     y = x%2
#     if (y==0):
#         print(f"The Even Number = {x} ")
#     # print(f"Even Number is {x}")
#     x = x + 1


# x = 1
# y = 0
# while x<=100:
#     y = x%2
#     if (y!=0):
#         print(f"The Odd Number is = {x} ")
#     # print(f"Even Number is {x}")
#     x = x + 1

# x = 1
# y = 0
# s = 0
# while x<=100:
#     y = x%2
#     if (y==0):
#         s = s + x
#         # print(f"The sum from {1} to {y} =  {s} ")
#     # print(f"Even Number is {x}")
#     x = x + 1
# print(f"The Sum of Even Number 1-100 is {s}")

# starting value
# x = 1
# y = 0
# s = 0
# s2 = 0
# # condition
# while x<=10:
#     y = x%2
#     if (y==0):
#         s = s + x
#     if (y!=0):
#         s2 = s2 + x
#     x = x + 1
# # starting value will increase or decrease after every run.
# print(f"The Sum of Even Number 1-10 is {s}")
# print(f"The Sum of Odd Number 1-10 is {s2}")

# =====================================================================

# n = input("Kindly Input 7 digit Number = ")
# x = -1
# while x>=-7:
#     # print(f"{x}")
#     print(n [x])
#     # print(n [0::1])
#     x = x - 1

# usr = input("Tell me the number till which you find out the Sum = ")
# x = 1
# y =int(usr)
# sum = 0
# while x<=y:
#     sum = sum + x
#     x = x + 1
# print(f"The sum from {1} to {y} =  {sum} ")

# num = input("Kindly Input 7 digit Number = ")
# ctr = 0
# sum = 0
# prd = 1
# while ctr<=6:
#     sum = sum + int(num[ctr])
#     prd = prd * int(num[ctr])
#     ctr = ctr + 1
# print(f"The sum of digit is {sum} ")
# print(f"The product of digit is {prd} ")

# num = input("Kindly Input The Number = ")
# length = len(num)
# ctr = 0
# sum = 0
# # len2 = length - 1
# while ctr<=(length -1):
#     sum = sum + int(num[ctr])
#     ctr = ctr + 1
# print(f"The sum of digit is {sum} ")


# Anurag is python expert - "By March 2021"
# ctr_x = 1
# ctr_y = 1
# while ctr_x<=5:
# 	while ctr_y<=ctr_x:
# 		print("*", end =" ")
# 		ctr_y = ctr_y + 1
# 	print("\n")
# 	ctr_y = 1
# 	ctr_x = ctr_x + 1

    # ======================================
    # Anurag is python expert - "By March 2021"
# input number from user, Ex:302187.. print the min & Max Number
# #to find the position of the character in the variable
# msg1 = "she is beautiful and she is good dancer, Navneet sir woke up late again"
# print(msg1.find("sir"))

# num = input("Kindly Input The Number = ")
# a = 50
# b = 30
# c = 80
# d = 10
# max = 0
# if (max <=a): # true
#     max = a # 50
# if (max <=b): #false
#     max = b # skip
# if (max <=c): # true
#     max = c
# if (max <=d): # false
#     max = d
# print(f"The maxumum {max}")

# =================================================

# a = 50
# b = 10
# c = 80
# d = 100
# min = a # 50
# if (min >=a):
#     min = a #50
# if (min >=b): # true 50
#     min = b # 30 (replace)
# if (min >=c): # 30 false
#     min = c # 80 skip
# if (min >=d): #false
#     min = d # false
# print(f"The minimum {min}")

# n1,n2,n3,n4=input("kindly insert 4 values seperated by comma = ").split(",")
# max = 0
# print(f"The sum of values is {n1},{n2},{n3} =  {int(n1) + int(n2) + int(n3)}")
# take 4 comma seperated number from users as input. find out min and max of those number
# n = input("Kindly input 4 numbers seperated by comma = ").split(",")
# n1,n2,n3,n4=input("kindly insert 4 values seperated by comma = ").split(",")
# a = int(n1)
# b = int(n2)
# c = int(n3)
# d = int(n4)
# max = 0
# min = a
# if (max <=a): # true
#     max = a # 50
# if (max <=b): #false
#     max = b # skip
# if (max <=c): # true
#     max = c
# if (max <=d): # false
#     max = d
# if (min >=a): # true
#     min = a # 50
# if (min >=b): #false
#     min = b # skip
# if (min >=c): # true
#     min = c
# if (min >=d): # false
#     min = d
# print(f"The min is {min} & max is {max}")

# Ask user to enter a 10 digit number and find the min and max digit : 7835262189
# x = -1
# while x>=-7:
#     # print(f"{x}")
#     print(n [x])
#     # print(n [0::1])
# 7835262189
n =input("kindly insert 10 digit number = ")
x = 0
max = 0 
# int (n [0])
while x<=9:
    if (max <=int (n [x])): # true
        max = int (n [x]) # 50
    x = x + 1
print(f"The max is {max}") 