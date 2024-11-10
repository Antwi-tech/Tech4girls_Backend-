# Question 6: Age Validator

while True:
        try:
            age = int(input("Enter your age: "))
        except ValueError as v:
            print(f'{v}.It not accepted.Enter an integer')
            continue
        except Exception as e:
            print(f'{e}. Invalid')
            continue
        if age < 0:
            print("Age cannot be negative!")
        elif age > 120:
            print("That age is unlikely!")
        else:
            print("Your age is:", age)
        break    

