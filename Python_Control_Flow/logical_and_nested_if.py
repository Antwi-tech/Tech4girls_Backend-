
# #Anwer is manually recorded
# is_student = True
# is_employed = True

# if is_student and is_employed:
#     print("You are a working student.")
# elif is_student and not is_employed:
#     print("You are a student.")
# elif not is_student and is_employed:
#     print("You are employed but not a student.")


# #Or you can take input fron a user

# print('\nAnswer True or False for the ff questions:')

# print('Are you a student?')
# is_student = input()

# print('Are you emplyed?')
# is_employed = input()



# if is_student == 'True'  and is_employed == 'True' :
#     print("You are a working student.")
# elif is_student == 'True' and not is_employed == 'True':
#     print("You are a student.")
# elif not is_student == 'True'  and  is_employed =='True':
#     print("You are employed but not a student.")
# else:
#     print('Invalid Status')    





#CHECK FOR DRIVER'S LICENSE ACCORDING TO AGE

print('Please enter age:')

age = int(input())

if age >= 18:
    print('Do you have a driver\'s license?\n')
    print('Y for yes')
    print('N for No\n')
    answer = input()
    
    if answer == 'Y' or  answer =='y':
        print('You are allowed to drive.')
    elif answer == 'N' or answer == 'n' :
        print('You need a driver\'s license to drive.') 
else:
        print('You are not old enough to drive.')     

               
          
    
    





    
        