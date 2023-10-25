def encode(number):
    result = ""
    for i in str(number):
        num = int(i) + 3
        result += str(num)
    return result


def main():
    x = 1
    while x:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = int(input("Please enter your password to encode:"))
            encode(password)
            print("Your password has been encoded and stored!")
        if user_input == 2:
            pass
        if user_input == 3:
            x = 0


if __name__ == '__main__':
    main()
