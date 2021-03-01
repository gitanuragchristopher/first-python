# # Python 3.6 formating
# n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# print(f"The First Number is = {n1}, The Second Number is = {n2}, The Third Number is ={n3}")

# # # Python 1 formating
# # n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# print("The First Number is = " +n1 +"," +"The Second Number is = " +n2 +", "+"The Third Number is = " +n3)

# # Python 3 formating
# #python (3) string formatting
# print("hello {} your age is {} ".format(name, age))
# # {} this is place holder
# print("hello {} your age is {} ".format(name, age + 2))

# n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
# print("The First Number is ={},The Second Number is ={}, The Third Number is ={}".format(n1,n2,n3))


n1,n2,n3=input("kindly insert 3 values seperated by comma = ").split(",")
n4= (int(n1)+ int(n2)+int(n3)) /3
print(f"The avarage of values {n1},{n2},{n3} =  {n4}")
