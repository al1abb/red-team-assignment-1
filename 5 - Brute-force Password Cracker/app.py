import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(input_password):
    with open('1M_passwords.txt', 'r') as file:
        wordlist = file.read().splitlines()
        print(wordlist)

        for word in wordlist:
            hashed_input_password = hash_password(input_password)
            hashed_word = hash_password(word)
            if hashed_input_password == hashed_word:
                print(f"Password found: {word}")
                return
            else :
                print(f"Password not found: {word}")
        print("Password not found in wordlist.")

if __name__ == "__main__":
    password_hash = input("Enter password: ")
    brute_force(password_hash)