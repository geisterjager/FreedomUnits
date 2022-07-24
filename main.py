# Printing the Flag
print("")
print("|* * * * * * * * * *oooooooooooooooooooooooooo|")
print("| * * * * * * * * * ::::::::::::::::::::::::::|")
print("|* * * * * * * * * *oooooooooooooooooooooooooo|")
print("| * * * * * * * * * ::::::::::::::::::::::::::|")
print("|* * * * * * * * * *oooooooooooooooooooooooooo|")
print("| * * * * * * * * * ::::::::::::::::::::::::::|")
print("|* * * * * * * * * *oooooooooooooooooooooooooo|")
print("|:::::::::::::::::::::::::::::::::::::::::::::|")
print("|ooooooooooooooooooooooooooooooooooooooooooooo|")
print("|:::::::::::::::::::::::::::::::::::::::::::::|")
print("|ooooooooooooooooooooooooooooooooooooooooooooo|")
print("|:::::::::::::::::::::::::::::::::::::::::::::|")
print("|ooooooooooooooooooooooooooooooooooooooooooooo|")
print("")

# Greeting the User
print("Welcome to Freedom Units, Patriotic Citizen!")
print("Let's convert your useless metric measurements into")
print("patriotic Freedom Units, used by all Americans!")
print("")

# Choosing the Conversion
def unit_chooser():
    print("Which unit conversion do you want to do?")
    user_choice = int(input("1 for Temperature, 2 for Lengths, 3 for Distances"))
    if user_choice == 1:
        temperature_convert()
    elif user_choice == 2:
        feet_to_meters()
    elif user_choice == 3:
        miles_to_km()
    else:
        print("ERROR!  Try Again!")
        unit_chooser()

# Temperature Function
def temperature_convert():
    print("What Temperature Unit Are You Starting With?")
    temp_unit = int(input("Choose 1 for Celsius, Choose 2 for FREEDOM UNITS!"))
    if temp_unit == 2:
        f_temp = float(input("What is the Temperature in FREEDOM UNITS?"))
        converted_c_temp = (f_temp - 32) / 1.8
        print("The Temperature in Celsius is:", converted_c_temp)
        rerun()
    elif temp_unit == 1:
        c_temp = float(input("What is the Temperature in Celsius?"))
        converted_f_temp = (c_temp * 1.8) + 32
        print("The Temperature in FREEDOM UNITS is:", converted_f_temp)
        rerun()
    else:
        print("ERROR!  Try Again!")
        temperature_convert()

# Feet/Inches to Meters Function
def feet_to_meters():
    print("Are you starting with Meters or FREEDOM UNITS?")
    short_distance = int(input("Choose 1 for Meters, Choose 2 for FREEDOM UNITS!"))
    if short_distance == 2:
        feet = int(input("How many feet?"))
        inches = int(input("How many inches?"))
        total_inches = int((feet * 12) + inches)
        converted_meters = total_inches / 39.37
        print("Your distance in meters is:", round(converted_meters, 2), "meters!")
        rerun()
    elif short_distance == 1:
        meters = float(input("What is the distance in Meters?"))
        converted_inches = meters * 39.37
        converted_feet = int(converted_inches / 12)
        inch_remainder = int(converted_inches % 12)
        print("Your distance in FREEDOM UNITS is:", converted_feet, "feet and", inch_remainder, "inches!")
        rerun()
    else:
        print("ERROR!  Try Again!")
        feet_to_meters()

# Miles to Kilometers Function
def miles_to_km():
    print("Are you starting with Kilometers or FREEDOM UNITS?")
    long_distance = int(input("Choose 1 for Kilometers, Choose 2 for FREEDOM UNITS!"))
    if long_distance == 2:
        miles = float(input("How many miles?"))
        converted_km = miles * 1.61
        print("Your distance in kilometers is", round(converted_km, 2), "km")
        rerun()
    elif long_distance == 1:
        km = float(input("How many kilometers?"))
        converted_miles = km / 1.61
        print("Your distance in FREEDOM UNITS is", round(converted_miles, 2), "miles")
        rerun()
    else:
        print("ERROR!  Try Again!")
        miles_to_km()

# Rerun Function
def rerun():
    print("")
    print("Would you like to convert something else?")
    rerun_choice = int(input("1 for Yes, 2 for No."))
    if rerun_choice == 1:
        unit_chooser()
    elif rerun_choice == 2:
        print("Stay Free, Brother/Sister/Enby Sibling!")
        return
    else:
        print("ERROR!  Try Again.")
        rerun()

unit_chooser()