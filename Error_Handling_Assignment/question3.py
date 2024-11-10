# Question 3: Integer Conversion
while True:
    try:
        user_input = input("Enter a number: ")
        converted_number = int(user_input)
    except ValueError:
        print('Enter a whole number')
        continue
    except Exception as e:
        print(f'Enter only integers.')
        continue
    else:
        print("The number you entered is:", converted_number)
    break    
