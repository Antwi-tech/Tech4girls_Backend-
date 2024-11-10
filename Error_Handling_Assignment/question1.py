# Question 1: Division Calculator

#This has 2 while statement beacause after the denominator has occured an error I wanted it to continue 
#from thre rather than starting all over again. It also prints the prvious numerator entered

while True: 
    try:
        numerator = int(input("Enter the numerator: "))
    except ValueError:
            print('\nPlease enter an integer') 
            continue
    except ZeroDivisionError as z:
            print(f"\n{z} is not possible")
            continue
    except NameError:
            print('\nPlease re-enter number') 
            continue       
        
    
    while True:
            try:
                denominator = int(input("Enter the denominator: "))
                result = numerator / denominator
            except ValueError:
                print('\nPlease enter an integer') 
                print(f"Your numerator: {numerator} ")
                continue
            except ZeroDivisionError as z:
                print(f"\n{z} is not possible")
                print(f"Your numerator: {numerator} ")
                continue
            except NameError:
                print('\nPlease re-enter number') 
                print(f"Your numerator: {numerator} ")
                continue   
            
            else:
                print("The result is:", result)    
                break
    break           

                
