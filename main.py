def encode(number):
    result = ""
    for i in number:
        num = int(i) + 3
        result += str(num)
    print(result)
    return result


def decode(password):
    final = ""
    for i in str(password):
        num = int(i) - 3
        final += str(num)
    return final


def main():
    x = 1
    while x:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to encode:")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        if user_input == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        if user_input == 3:
            x = 0


if __name__ == '__main__':
    main()
