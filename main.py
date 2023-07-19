# Nicholas Pfister
def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)  # making sure to not go above 9 and create extra digits
        encoded_password += new_digit
    return encoded_password

password = None
encoded_password = None
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")

    if option == "1":  # Encode Password
        if password is None:
            password = (input("Please enter your password to encode: "))  # Original Password
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        else:  # Setting up for decoder file
            pass
    elif option == "2":
        if encoded_password is not None:
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
        else: #Set up for decoder
            pass
    elif option == "3":
        break
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
