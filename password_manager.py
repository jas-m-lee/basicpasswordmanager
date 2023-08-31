def main():
    while True:
        select = input("Please enter your selecion: ")

        if select == '1':
            add_password()
        elif select == '2':
            view_passwords()
        elif select == '0':
            print("Exiting...")
            break
        else:
            print("Your selection is invalid. Please try again.")

    
def show_selection_menu():
    print("Welcome to Password Manager.")
    print("Begin by adding a password (1) or viewing a password (2)")
    print("Press the number of your selection. To quit please select 0.")

def add_password():
    website = input("Enter a website: ")
    password = input("Enter a password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"Website: {website}, Password: {password}\n")
    
    print("Password is now saved.")

def view_passwords():
    try:
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
            for password in passwords:
                print(password.strip())
    except FileNotFoundError:
        print("There are no passwords saved.")

if __name__ == "__main__":
    main()
