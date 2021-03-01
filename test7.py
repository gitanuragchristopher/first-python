# name = "      Yogesh      "
# dots = ".................."
# print(name + dots)
# print(name.lstrip() + dots)
# print(name.rstrip() + dots)
# print(name.strip() + dots)
# #Strip method will not remove space in between the string varaible
# mystatus = "      My world is amazing and i am loving it      "
# print(mystatus+dots)
# #to remove all spaces you can use replace method
# print(mystatus.replace(" ",""))

# Replace Method
# msg1 = "she is beautiful and she is good dancer"
# print(msg1.replace(" ",""))
# print(msg1.replace("is","was"))
# print(msg1.replace("is","was",1)) #this will only replace 1 occurrence
 
# Note: String are immutable in Python. In Ruby programming language it is mutable.
# It means that replace method will not permanently replace the character inside the variable,
# it is replacing only for print method.
# We can change the value of a variable, but methods cannot change our string variable content permanently.
# You can do the below for permanent replacement:
msg1 = "This is a good is"
# msg2 = msg1.replace("is","was")
msg2 = msg1.replace(" ","")
print(msg2)