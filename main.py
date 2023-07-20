# Nicholas Pfister
def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)  # making sure to not go above 9 and create extra digits
        encoded_password += new_digit
    return encoded_password

def passwordDecoder(password):
    decodedPassword = None
    digitList = []
    for digit in password:
        newDigit = ((int(digit) - 3) % 10)
        digitList.append(str(newDigit))
    decodedPassword = "".join(digitList)
    return decodedPassword

password = None
encoded_password = None
if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":  # Encode Password
            if password is None:  # In order to make main work for decoder file
                password = (input("Please enter your password to encode: "))
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print(f"The encoded password is {encoded_password}, and the original password is {password}.")
        elif option == "2": # Decode
            if encoded_password is not None:  # Setting up main for decoder file
                print(f"The encoded password is {encoded_password}, and the original password is {password}.")
            else:
                encoded_password = str(input("Please enter your password to decode: "))
                password = passwordDecoder(encoded_password)
                print("Your password has been decoded and stored!")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")


