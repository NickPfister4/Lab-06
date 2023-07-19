def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)  # Making sure to not go above 9 and create extra digits in the password
        encoded_password += new_digit
    return encoded_password


def decode(password):
    decoded_password = ""
    for digit in password:
        new_digit = str((int(digit) - 3) % 10)  # Making sure to not go below 0
        decoded_password += new_digit
    return decoded_password


password = None
encoded_password = None

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")

    if option == "1":
        if password is not None:  # So program doesn't re-ask for password if it has already been given
            print(f"The the original password is {password}, and the encoded password is {encoded_password}.")
        else:
            password = input("Please enter your password to encode: ")  # Entering original password
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

    elif option == "2":
        if encoded_password is not None:  # Same as above
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
        else:
            encoded_password = input("Please enter your encoded password: ")  # Entering changed password
            password = decode(encoded_password)
            print("Your encoded password has been decoded and stored!")
    elif option == "3":
        break
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
