from tkinter import *
from tkinter import messagebox
import os



class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def filename(self):
      
        safe_user = self.user.replace(" ", "_")
        safe_title = self.title.replace(" ", "_")
        return f"{safe_user}_{safe_title}.txt"

    def save_to_file(self):
        try:
            file = self.filename()
            with open(file, "w", encoding="utf-8") as f:
                f.write(f"Author: {self.user}\n")
                f.write(f"Title: {self.title}\n\n")
                f.write(self.content)
            return file

        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")



def save_post():
    name = name_entry.get().strip()
    title = title_entry.get().strip()
    content = content_text.get("1.0", END).strip()

    if not name or not title or not content:
        messagebox.showwarning("Validation Error", "All fields are required!")
        return

    user = User(name)
    post = Post(user.name, title, content)
    file = post.save_to_file()

    if file:
        messagebox.showinfo("Success", f"Post saved as {file}")
        load_saved_posts()


def load_saved_posts():
    listbox_posts.delete(0, END)

    for file in os.listdir():
        if file.endswith(".txt") and "_" in file:
            listbox_posts.insert(END, file)


def view_post():
    try:
        selected = listbox_posts.get(ACTIVE)

        if not selected:
            messagebox.showwarning("Error", "Please select a post to view.")
            return

        with open(selected, "r", encoding="utf-8") as f:
            content = f.read()

        view_window = Toplevel(root)
        view_window.title(selected)
        view_window.geometry("500x400")

        Label(view_window, text=selected, font=("Arial", 14, "bold")).pack(pady=10)

        text_area = Text(view_window, width=60, height=20)
        text_area.pack()
        text_area.insert(END, content)

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))




root = Tk()
root.title("MiniBlog App")
root.geometry("600x550")

Label(root, text="MiniBlog - Create & View Posts", font=("Arial", 16, "bold")).pack(pady=10)


Label(root, text="Your Name:").pack()
name_entry = Entry(root, width=40)
name_entry.pack(pady=5)


Label(root, text="Post Title:").pack()
title_entry = Entry(root, width=40)
title_entry.pack(pady=5)


Label(root, text="Post Content:").pack()
content_text = Text(root, width=50, height=10)
content_text.pack(pady=5)


Button(root, text="Save Post", width=20, bg="green", fg="white", command=save_post).pack(pady=10)


Label(root, text="Your Saved Posts:").pack()
listbox_posts = Listbox(root, width=50, height=10)
listbox_posts.pack()

Button(root, text="View Selected Post", width=20, bg="blue", fg="white", command=view_post).pack(pady=10)


load_saved_posts()

root.mainloop()
