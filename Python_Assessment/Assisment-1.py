import datetime   

users = {}        
posts = []        

def register():
    username = input("Enter username: ").strip()
    if username in users:                     
        print(" Username already exists!")
        return
    if not username:                          
        print(" Username cannot be blank!")
        return
    password = input("Enter password: ").strip()
    users[username] = password
    print(f" User '{username}' registered successfully!")


def login():
    for attempt in range(3):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if users.get(username) == password:   
                print(f" Welcome {username}!")
                return username
        else:
            print(" Invalid credentials!")
    print(" Too many attempts. Exiting...")
    return None


def create_post(author):
    title = input("Enter post title: ").strip()
    desc = input("Enter description: ").strip()
    if not title or not desc:                 
        print(" Title and Description cannot be blank!")
        return
    date_choice = input("Enter date manually? (y/n): ").lower()
    if date_choice == "y":
        date = input("Enter date (YYYY-MM-DD): ").strip()
    else:
        date = datetime.date.today().strftime("%Y-%m-%d")
    post = {"author": author, "title": title, "description": desc, "date": date}
    posts.append(post)                        
    print(" Post created successfully!")


def view_posts():
    if not posts:
        print(" No posts available.")
        return
    print("\n All Posts")
    for post in posts:
        print(f" Author: {post['author']}")
        print(f" Title : {post['title']}")
        print(f" Date  : {post['date']}")
        print(f" Desc  : {post['description']}\n{'-'*30}")

def search_posts():
    username = input("Enter username to search: ").strip()
    found = [p for p in posts if p['author'] == username]
    if not found:
        print(" No posts found for this user.")
        return
    print(f"\n Posts by {username}")
    for post in found:
        print(f" {post['title']} ({post['date']}) - {post['description']}")


def main():
    while True:
        print("\n--- PostBoard ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n--- Dashboard ---")
                    print("1. Create Post")
                    print("2. View Posts")
                    print("3. Search Posts")
                    print("4. Logout")
                    ch = input("Enter choice: ").strip()

                    if ch == "1":
                        create_post(user)
                    elif ch == "2":
                        view_posts()
                    elif ch == "3":
                        search_posts()
                    elif ch == "4":
                        print(" Logged out.")
                        break
                    else:
                        print(" Invalid option!")
        elif choice == "3":
            print(" Exiting program.")
            break
        else:
            print(" Invalid option!")


if __name__ == "__main__":
    main()
