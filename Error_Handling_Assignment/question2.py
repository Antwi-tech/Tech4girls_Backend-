# Question 2: Dictionary Lookup
#Without the while loop the program won't continue to run
while True:
    try:
        data = {"name": "Alice", "age": 25, "country": "Wonderland"}
        print(f"Keys available: {data.keys()}")
        key = input("Enter the key you want to look up: ")
        print("Value:", data[key])
    except KeyError:
        print('\nThat Key does not exist\n')
        continue
    break

