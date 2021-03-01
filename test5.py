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
# print (prg_lang[-1]) # output is 'n'
#print (prg_lang[-7]) # you get error


#string slicing is used to fetch values within a starting and ending range
#syntax [start argument : stop argument -1]
# prg_lang = "python"
# print(prg_lang[0:4]) #output is pyth
# print(prg_lang[-3:6]) #output is hon
# print(prg_lang[3:]) #output is hon
# print(prg_lang[:3]) #output is pyt 


prg_lang = "harshit"
# print(prg_lang[1:4])

# Step Argument
# syntax - [start argument : stop argument -1 : step -1]
# print("Harshit"[2:5]) # Output is rsh
# print("Harshit"[0:5:2]) # Output is Hrh
# print("Harshit"[0::2]) # Output is Hrht
# print("Harshit"[0::3]) # Output is Hst
# print("Harshit"[::3]) # Output is Hst
# print("harshit"[5::-1]) # Output is ihsraH
# print("Harshit"[-1::-1]) # Output is tihsraH
print("Harshit"[::-1]) # Output is tihsraH

# prg_lang = "Harshit"
# print(prg_lang[2:5]) 
h/w

# ask user his username ad print it in reverse.make it in two lines.
Name = input("Kindly insert your name = ")
print(str(Name)[-1::-1])
print(str(Name).lower())
print(str(Name).upper())
print(str(Name).title())


