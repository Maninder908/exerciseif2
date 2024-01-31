def cruise_cabin_description(cabin_class):
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class. Please enter a valid class.")

# Get user input for cabin class
user_input = input("Enter the cabin class (LUX, A, B, or C): ").upper()

# Call the function with the user's input
cruise_cabin_description(user_input)

