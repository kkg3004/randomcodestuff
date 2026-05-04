def create_account():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    # Read existing usernames (handle missing file)
    existing = set()
    try:
        with open("users.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",", 1)
                if parts and parts[0]:
                    existing.add(parts[0])
    except FileNotFoundError:
        pass

    if username in existing:
        print("That username is already taken. Please choose another.")
        return

    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        with open("users.txt", "r") as f:
            users = f.readlines()
    except FileNotFoundError:
        print("No users exist yet.")
        return False

    for user in users:
        stored_username, stored_password = user.strip().split(",", 1)
        if stored_username == username:
            if stored_password == password:
                print("Login successful!")
                return True
            else:
                print("Username and password do not match.")
                return False

    print("Username not found.")
    return False

def change_password(username):
    verify = input("Enter your current password: ")
    try:
        with open("users.txt", "r") as f:
            users = f.readlines()
    except FileNotFoundError:
        print("No users exist yet.")
        return
    for user in users:
        stored_username, stored_password = user.strip().split(",", 1)
        if stored_username == username:
            if stored_password != verify:
                print("Current password is incorrect.")
                return
            break
    new_password = input("Enter your new password: ")
    try:
        with open("users.txt", "r") as f:
            users = f.readlines()
    except FileNotFoundError:
        print("No users exist yet.")
        return

    with open("users.txt", "w") as f:
        for user in users:
            stored_username, stored_password = user.strip().split(",", 1)
            if stored_username == username:
                f.write(f"{username},{new_password}\n")
            else:
                f.write(user)
    print("Password changed successfully!")

def content():
    import time
    time.sleep(4)
    print("Accessing protected content...")
    # Placeholder for actual content
    time.sleep(2)
    print("Welcome to the exclusive content area!")
    time.sleep(2)
    print("there is nothing here :(")
    time.sleep(2)
    print("anyways, thank you for giving me your personal data :)")
    time.sleep(1)
    print("i mean, your time.")
    time.sleep(4)
    print("Leave. I don't have time for you to sit here.")
    return True

def main():
    while True:
        choice = input("Do you want to (1) Create an account, (2) Log in, (3) Exit or (4) Change password? ")
        if choice == "1":
            create_account()
        elif choice == "2":
            if login():
                if content():
                    break
        elif choice == "3":
            print("Exiting the program.")
            break
        elif choice == "4":
            username = input("Enter your username to change password: ")
            change_password(username)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()