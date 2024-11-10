# Question 5: List Index Access


items = ["apple", "banana", "cherry"]


while True:
    try:
        index = int(input("Enter the index of the item you want to access: "))
        print("You selected:", items[index]) 
    except IndexError:
        print('\nThere\'s not an index that')
        continue
    except ValueError:
        print('\nInput an integer')    
        continue
    except Exception as e:
        print(f'\nThis error occured: {e}.So enter a valid number')
    break 
       
