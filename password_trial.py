def login(user_name, password):
    with open("users.txt", "r") as file:

        users_dict = {}

        for line in file:

            split_users = line.strip().split(", ")
            users_dict[split_users[0]] = split_users[1]


        if user_name not in users_dict:
            print("Username not in our database!")

            while True:
                choice = input("\nDo you wish to create an account?(yes/no): ").lower().strip()

                if choice == "yes":
                    new_user(user_name, password)
                    break

                elif choice == "no":
                    print("Closing program!")
                    exit()

                else:
                    print("Please choose between 'yes' or 'no'.")
                    continue


        elif password != users_dict[user_name]:
            print("Invalid Password!")

        else:
            print(f"Welcome back {user_name}!")
            exit()


def new_user(new_username, new_password):
    with open("users.txt", "a+") as file:

        users_dict = {}
        
        file.seek(0)

        for line in file:

            split_users = line.strip().split(", ")
            users_dict[split_users[0]] = split_users[1]

        while True:

            new_username = input("\nPlease enter new username: ")

            if new_username in users_dict.keys():

                print("That username already exists! Please enter a different one. Please try again")
                continue

            elif " " in new_username:
                print("Spaces aren't allowed for username. Please try again")
                continue

            elif len(new_username) == 0:
                print("You can't have an empty username. Please try again")
                continue


            new_password = input("\nPlease enter new password: ")

            if new_username == new_password:
                print("Please make sure your username does not match your password!")
                continue

            elif " " in new_password:
                print("Spaces aren't allowed for password. Please try again")
                continue

            elif len(new_password) == 0:
                print("You can't have an empty password. Please try again")
                continue

            elif len(new_password) <= 2:
                print("Your password is too short. Please try again")
                continue

            confirm_password = input("\nPlease confirm password: ")

            if new_password != confirm_password:
                print("Your passwords don't match! Please try again.")

            else:
                print(f"Welcome {new_username}! Thank you for creating an account with us.")
                file.write(f"\n{new_username}, {new_password}")
                break


print("\n\t\t\tWelcome!\n")
print("\tPlease enter user credentials to login!\n")


while True:

    user_name = input("\nPlease enter your username: ")
    if user_name == "exit":
        print("Exiting the program")
        exit()

    password = input("\nPlease enter your password: ")
    if password == "exit":
        print("Exiting the program")
        exit()

    login(user_name, password)
