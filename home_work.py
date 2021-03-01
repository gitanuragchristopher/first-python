# # ***** Exercise : print these following lines *********
# # This is \\ double backslash
# # these are mountains /\/\/\/\/\ mountains
# # he is 	awesome (use escape sequences instead of manual spaces)
# # \" \n \t \' (print this as an output)

# n1=input("Dear User, Kindly press enter to learn something new")
# n2=input("This is Double '\\\\' BackSlash")
# print=n1+n2

# n1=input("Dear User, Kindly press enter to see magic")
# n2=input("These are mountains /\\/\\/\\/\\/\\")
# print=n1+n2

# n1=input("Insert you Name = ")
# n2=input("Hello Mr. Anurag,\nYou are awesome, \nHave a great day ahead..!")
# print=n1+n2

# n1=input("\" \n \t \' (print this as an output) ")
# n2=input("Hello Mr. Anurag,\nYou are awesome, \nHave a great day ahead..!")
# print=n1+n2


n1,n2,n3=input("kindly insert 3 values seperated by space").split()
#need to input 3 values
t1=int(n1)
#convert string to integer
t2=int(n2)
#convert string to integer
t3=int(n3)
#convert string to integer
t4=t1*t2*t3
#declaire 4th varibale to calculate sum
print("The sum is = " +str(t4))