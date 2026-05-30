import tkinter as tk
from tkinter import messagebox
import sqlite3

# -----------------------------
# Database Setup
# -----------------------------
conn = sqlite3.connect("miniblog.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    title TEXT,
    content TEXT
)
""")
conn.commit()

# -----------------------------
# Save Post Function
# -----------------------------
def save_post():
    username = username_entry.get()
    title = title_entry.get()
    content = content_text.get("1.0", tk.END)

    if username == "" or title == "" or content.strip() == "":
        messagebox.showwarning("Warning", "All fields required!")
        return

    try:
        cursor.execute("INSERT INTO posts (username, title, content) VALUES (?, ?, ?)",
                       (username, title, content))
        conn.commit()

        messagebox.showinfo("Success", "Post Saved!")

        load_posts()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# -----------------------------
# Load Posts in Listbox
# -----------------------------
def load_posts():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, title FROM posts")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

# -----------------------------
# View Post
# -----------------------------
def view_post():
    try:
        selected = listbox.get(listbox.curselection())
        post_id = selected.split(" - ")[0]

        cursor.execute("SELECT username, title, content FROM posts WHERE id=?", (post_id,))
        post = cursor.fetchone()

        display_text.delete("1.0", tk.END)
        display_text.insert(tk.END, f"Author: {post[0]}\n")
        display_text.insert(tk.END, f"Title: {post[1]}\n\n")
        display_text.insert(tk.END, post[2])

    except:
        messagebox.showerror("Error", "Select a post!")

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("MiniBlog App")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Title").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Content").pack()
content_text = tk.Text(root, height=5)
content_text.pack()

tk.Button(root, text="Save Post", command=save_post).pack()

tk.Label(root, text="Saved Posts").pack()
listbox = tk.Listbox(root)
listbox.pack()

tk.Button(root, text="View Post", command=view_post).pack()

display_text = tk.Text(root, height=10)
display_text.pack()

# Load existing posts
load_posts()

root.mainloop()