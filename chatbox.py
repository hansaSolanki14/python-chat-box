import tkinter as tk
from tkinter import scrolledtext

# ---------------- Chatbot Logic ----------------
def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    elif "your name" in user_input:
        return "I am SimpleChat 🤖"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😄"

    elif "age" in user_input:
        return "I don't have an age. I'm just code 🧠"

    elif "bye" in user_input:
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that 😅"


# ---------------- Button Function ----------------
def send_message():
    user_text = entry.get()

    if user_text.strip() == "":
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_text + "\n")

    bot_reply = get_response(user_text)
    chat_window.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

    entry.delete(0, tk.END)


# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Simple Python Chat Box")
root.geometry("420x500")
root.resizable(False, False)

# Chat Area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_window.pack(pady=10)

# Input Box
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Send Button
send_btn = tk.Button(root, text="Send", width=10, command=send_message)
send_btn.pack()

# Run App
root.mainloop()
