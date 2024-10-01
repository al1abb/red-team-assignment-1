import string

all_chars = string.ascii_letters

# print(all_chars)

def encrypt(text, shift):
    data = []
    for i in text:
        if i in all_chars: 
            data.append(all_chars[(all_chars.index(i) + shift) % 52])    
        else:
            data.append(i)
    output = ''.join(data)
    return output

def decrypt(text, shift):
    data = []
    for i in text:
        if i in all_chars: 
            data.append(all_chars[(all_chars.index(i) - shift) % 52])    
        else:
            data.append(i)
    output = ''.join(data)
    return output

def main():
    encrypt_or_decrypt = input("Would you like to encrypt or decrypt? E/D: ")
    if encrypt_or_decrypt.lower() == "e":
        text = input("Enter text: ")
        shift = int(input("Enter shift: "))
        print("Encrypted text: " + encrypt(text, shift))
    elif encrypt_or_decrypt.lower() == "d":
        text = input("Enter text: ")
        shift = int(input("Enter shift: "))
        print("Decrypted text: " + decrypt(text, shift))
    else:
        print("Invalid input. Please try again.")
        main()
    # text = input("Enter text: ")
    # shift = int(input("Enter shift: "))

    # # print("Encrypted text: " + encrypt(text, shift))
    # print("Decrypted text: " + decrypt(text, shift))


if __name__ == "__main__":
    main()