import sys
import hashlib

"""
Hashes of somefile.txt
MD5: d5dde22b761dc802fcf173b415a9c50b
SHA1: b00919535429bde4820b97075f80fff6e3e1fe22
SHA256: d9f3fb0ce109cebe053aec20deeff239a13f1a281d8288236afa66941e120545
"""
def calculate_hash(file_path, hash_function, user_provided_hash):
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5hash = hash_function.lower() == "md5"
    sha1hash = hash_function.lower() == "sha1"
    sha256hash = hash_function.lower() == "sha256"

    if md5hash:
        md5 = hashlib.md5()
    if sha1hash:
        sha1 = hashlib.sha1()
    if sha256hash:
        sha256 = hashlib.sha256()

    with open(file_path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            if md5hash:
                md5.update(data)
            if sha1hash:
                sha1.update(data)
            if sha256hash:
                sha256.update(data)
    
    if md5hash:
        print("MD5: {0}".format(md5.hexdigest()))
        if(user_provided_hash == md5.hexdigest()):
            print("File Verified")
        else:
            print("File Verification Failed")
    if sha1hash:
        print("SHA1: {0}".format(sha1.hexdigest()))
        if(user_provided_hash == sha1.hexdigest()):
            print("File Verified")
        else:
            print("File Verification Failed")
    if sha256hash:
        print("SHA256: {0}".format(sha256.hexdigest()))
        if(user_provided_hash == sha256.hexdigest()):
            print("File Verified")
        else:
            print("File Verification Failed")

def main():
    file_path = input("Enter File Path: ")
    hash_function = input("Enter Hash Function (MD5, SHA1, SHA256): ")
    hash_function = hash_function.lower()

    user_provided_hash = input("Enter Your Hash: ")

    calculate_hash(file_path, hash_function, user_provided_hash)
        

if __name__ == "__main__":
    main()