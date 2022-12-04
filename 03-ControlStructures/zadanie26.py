def pin_check(pin):
    try_counter = 1
    user_input = ""

    while user_input != pin and try_counter < 4:
        user_input = int(input( "Enter the PIN code:"))
        try_counter += 1
        if user_input == pin:
            print("Access gained")
            exit
        else:
            print("Incorrect...")
    if try_counter >= 4:
        print("Sorry, your payment card has been blocked.")
     

pin_check("0805")