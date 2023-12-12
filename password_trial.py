def login(user_name, password):

    users_dict = {}

    file = open("users.txt", "r")

    for line in file:

        split_users = line.strip().split(", ")
        users_dict[split_users[0]] = split_users[1]


    if user_name not in users_dict:
        print("Username not available!")
        choice = input("\nDo you wish to create an account?(yes/no): ")

        if choice == "yes":
            new_user(user_name, password)

        else:
            print("Closing program!")
            exit()

    elif password != users_dict[user_name]:
        print("Invalid Password!")

    else:
        print(f"Welcome {user_name}!")


def new_user(user_name, password):
    with open("users.txt", "a") as file:

        while True:

            user_name = input("\nPlease enter new username: ")
            password = input("\nPlease enter new password: ")

            if user_name == password:
                print("Please make sure your username does not match your password!")
                continue

            else:
                file.write(f"\n{user_name}, {password}")
                break


print("\n\t\t\tWelcome!\n")

print("Please press 'exit' to exit!\n")


while True:

    user_name = input("\nPlease enter username: ")
    if user_name == "exit":
        print("Exiting the program")
        exit()

    password = input("\nPlease enter password: ")
    if password == "exit":
        print("Exiting the program")
        exit()

    login(user_name, password)
