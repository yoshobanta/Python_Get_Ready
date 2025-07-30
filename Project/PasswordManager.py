from cryptography.fernet import Fernet

# One-time key generation
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load key from file
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# You only need to run this once to create the key
# Uncomment the next line once to generate the key
# write_key()

key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f:
            user, encrypted_pwd = line.strip().split(" | ")
            decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
            print(f"Account name - {user}")
            print(f"Password - {decrypted_pwd}")
            print("-------------------------------------------")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {encrypted_pwd}\n")

while True:
    mode = input("To add password type 'add', to view passwords type 'view', or 'q' to quit: ").lower()
    if mode in ("q", "quit"):
        break
    elif mode in ("view", "v"):
        view()
    elif mode in ("add", "a"):
        add()
    else:
        print("Invalid input. Please type 'add', 'view', or 'q'.")
