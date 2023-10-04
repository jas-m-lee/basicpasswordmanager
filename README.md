## Project Resources

### Basic Password Manager

#### Using the while loop for User Input

The first part of this program involved mimicking a menu with selectable options. The while loop allows you to output a message and let the user respond.

Example from this project:
```py
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
```
[While Loops and Input](http://introtopython.org/while_input.html)

#### Using a try and except Block 

To ensure the program runs appropriately, it is necessary to anticipate errors. Python has a language feature to execute code when no error occurs (try block) and execute another option if an error does occur (except block).

Example from this project:
```py
def view_passwords():
    try:
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
            for password in passwords:
                print(password.strip())
    except FileNotFoundError:
        print("There are no passwords saved.")
```

[Chapter 10: Files and Exceptions](https://nostarch.com/python-crash-course-3rd-edition)
