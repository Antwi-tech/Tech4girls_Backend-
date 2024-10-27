
#number represents the numbers from 1 to 50

for number in range(51):
    if (number % 3 == 0):
        print('Fizz')
    elif (number % 5 == 0):
        print(' Buzz')
    elif (number % 3 == 0 & number % 5 == 0):
        print('FizzBuzz')   
    else:
        print(number)  

