# =========================================
# agee = input("Enter your age : ")
# useage = int(agee)
# if useage >= 18:
#     print("you are an Adult")
# else:
#     print("you are a baby")

# if the age is in between 1-3, you entry is free. if the age is in between 4-10, you entry fee is 150 free.
# if the age is in between 11-60, you entry fee is 250. if the age is above 60 years you entry fee is 200.
# These are conditional statement
# agee = input("Enter your age : ")
# useage = int(agee)
# if useage <=0:
#     print("Invalid Input, enter valid age")
# elif 0<useage<=3:
#     print("you entry is free")
# elif 3<useage<=10:
#     print("you entry fee is 150/-")
# elif 10<useage<=60:
#     print("you entry fee is 250/-")
# elif 60<useage<=65:
#     print("you entry fee is 200/-")
# elif useage >= 65:
#     print("Buzurg citizen welcome free")
# else:
#     print("Phir se dekh")

# ===================================================================
# enter your lucky number in between 0-100 game.
# ln=69
# user=input("Welcome to the Game of Luck, enter you lucky number in between 0-100 = ") 
# n1=int(user)
# if n1 <=0:
#     print("Invalid Input, enter valid number")
# elif n1 ==ln:
#     print("You are a winner")
# elif 0<n1<=68:
#     print("Value is too Low")
# elif 70<n1<=100:
#     print("Value is too High")
# user enter you gender M/F,age.
# if the gender is M and age is 21 print (you are ready) and F is 18 (you are ready)
# else you are not eligible
# if gender ==M and age>=21 

# age,gen=input("Please enter you Age, Gender = ").split(",")
# n1=int(age)
# if ((n1>= 21) and (gen=="M")):
#     print("You are Eligible")
# elif ((0<n1<=21 and (gen=="M"))):
#     print("You are Not Eligible, Try Later")
# if ((n1>= 18) and (gen=="F")):
#     print("You are Eligible")
# elif ((0<n1<=18 and (gen=="F"))):
#     print("You are Not Eligible, Try Later")
#========================================================

# These can be called as logical operators" "and / or /not".
# age,gen=input("Please enter you Age, Gender = ").split(",")
# n1=int(age)
# if(gen!='M' and gen!='F'):
#     print("Invalid Gender")
# elif ((n1>= 21) and (gen=="M")) or ((n1>= 18) and (gen=="F")):
#     print("You are Eligible")
# # elif ((n1>= 18) and (gen=="F")):
#     # print("You are Eligible")
# else:
#     print("You are Not Eligible, Try Later")

# ===========================================================

# if age is 0-10 baby, 10-18 teen, 18-30 Married, 30-40, 40 and above to go to Himalya.

# agee = input("Enter your age : ")
# useage = int(agee)
# if useage <=0:
#     print("Invalid Input, enter valid age")
# elif 0<useage<=10:
#     print("yYou are a Baby")
# elif 10<useage<=18:
#     print(" Teenager")
# elif 18<useage<=30:
#     print("Batchelor 0r Married")
# elif 30<useage<=40:
#     pass
# elif useage >= 40:
#     print("Buzurg Himalaya nikal lo")

# =====================================================
# ask user his name, if user have "A" or "a" you can watch the movie else you will get ghanta.?
# ask user his name, if user name start with "A" or "a", you can watch the movie?
# ask user his name. if the user does not enter any thing and pressed enter then "we didn't get any input from you"?
# pos1 = msg3.find("sir")
# User Input
# n1 = input("Kindly Enter you Name = ")
# pos1 = n1.find("A")
# # print(pos1)
# pos2 = n1.find("a")
# # print(pos2)
# # condition
# if(pos1 >=0 or pos2 >=0):
# # #perform action
#     print("You Can watch Movie")
# # # # condition
# #  elif(n1 ==""):
# # # #perform action
# #      pass
# # # # condition
# else:
# # # #perform action
#     print("You will get Ghanta")
n1 = input("Kindly Enter you Name = ")
if (n1==""):
    print("you did not enter anything")
elif(('A' in n1) or ('a' in n1)):
    print("you can watch movie")
else:
    print("you will get GHANTA")



