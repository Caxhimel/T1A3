# Separate file to store functions to use across the program

# Validate numerical input
def validate_num(min: int, max: int):
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
def make_type_list(list: dict, x: str):
     print("\nWhich type would you like to know more about? ")
     num = 1
     for key in list:
        if key.find(x):
            print(f"  {num}  {key}")
            num += 1