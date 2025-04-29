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

while True:
        print("1. Add User")
        print("2. View Users")
        print("3. Delete User")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")