name = input("What is your Name?");
age = int(input("How old are you, {0}?".format(name)))
print(age)


if age < 18:
  print("You have to wait {0} years to vote".format(18-age))
elif age == 900:
  print("Sorry, yoda, you die in Return of the Jedi.")
else:
  print("You are old enough to vote.")
  print("Please put an X in the box")
  
 



# for i in range(1,15):
#   print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
#   print("*" * 80)