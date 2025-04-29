users = []

def add_user():
    name = input("Enter your name: ")
    user_id = input("Enter your user ID: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    users.append({
        "name": name,
        "user_id": user_id,
        "age": age,
        "email": email
    })
    print("user added successfully!")

def view_users():
    if not users:
        return "No users found."
    for user in users:
        print(f"Name: {user['name']}, user_id: {user['user_id']}, age: {user['age']}, email: {user['email']}")

def delete_user():
    user_id = input("enter user id if you want for delate:")
    for users in users:
        if users [user_id] == user_id:
            users.remove(users)
            print("user deleted successfully!")
            
            return
def balance():
    value = input("Enter your balance: ")   
    if value.isdigit():
        print(f"Your balance is: {value}")
    else:
        print("Invalid input. Please enter a number.")

def transfer():
    amount = input("Enter the amount to transfer: ")
    if amount.isdigit():
        return "Transferring {amount}..."
    else:
        return "Invalid input. Please enter a number."

def deposit():
    amount = input("Enter the amount to deposit: ")
    if amount.isdigit():
        return "Depositing {amount}..."
    else:
        return "Invalid input. Please enter a number."
    
def output(
    message):
    print(message)

while True:
        print("1. Add User")
        print("2. View Users")
        print("3. Delete User")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Deposit Money")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            balance("your balance is:")
        elif choice == '5':
            transfer("transfer is successfully!")
        elif choice == '6':
            deposit("deposit is successfully!")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")