# Question 6: Age Validator
age = int(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative!")
elif age > 120:
    print("That age is unlikely!")
else:
    print("Your age is:", age)

