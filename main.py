# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

pocet = len(names)-1

vyber = random.randint(0, pocet)
print(names[vyber])




