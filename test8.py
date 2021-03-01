# #to find the position of the character in the variable
# msg1 = "she is beautiful and she is good dancer, Navneet sir woke up late again"
# print(msg1.find("sir")) # will return the position of 1st 'is'
# msg2 = "she is beautiful and she is good dancer, Navneet sir woke up late again, but sunte nahi sir"
# print(msg2.find("sir",50)) #we are specifying from which position we need to search
# #example: To find position of 2nd 'is' in the variable
# msg3 = "she is beautiful and she is good dancer, Navneet sir woke up late again, but sir ki to "
# pos1 = msg3.find("sir")
# pos2 = msg3.find("sir",pos1 +1)
# print(pos1)
# print(pos2)

# # ==================================================
# #Example: Input user name and add 4 * before and after name
# name = input("Enter your name : ")
# print(name.center(len(name)+9, "*"))
# ========================================================
# assignment operator
# name1 = "yogesh"
# name1 = name1 + "it"
# print(name1)
# name2 = "Sharma"
# name2 += "it"
# print(name2)
# age1 = 23
# age1 = age1 + 1
# print(age1)
# age2 = 33
# age2 += 1
# print(age2)
# age3 = 43
# age3 *= 10
# print(age3)
# age4 = 53
# age4 -= 10
# print(age4)
# age3 = 43
# age3 /= 10
# print(age3)

# =========================================
agee = input("Enter your age : ")
useage = int(agee)
if useage >= 18:
    print("you are an Adult")