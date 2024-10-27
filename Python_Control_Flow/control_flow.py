print('How old are you?')

#This is to accept user input string and convert the string into an integer
age = int(input())


if (age < 18):
    print ('You are a minor')
elif ( age >= 18 and age <= 64):
    print('You are an adult')  
else:
    print('You are a senior ')      
