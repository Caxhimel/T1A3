# Separate file to store functions to use across the program

# Validate numerical input
def validate_num(min, max):
        while True:
            try: 
                data = int(input(f"Enter number: "))
            except ValueError:
                print("Data is not a number, please try again")
                continue
            if data < min or data > max:
                print("Data invalid, please try again")
                continue
            else:
                return data