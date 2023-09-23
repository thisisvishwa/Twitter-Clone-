```python
import tkinter as tk
from tkinter import ttk

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title('Twitter Clone')
        self.create_widgets()

    def create_widgets(self):
        self.loginForm = ttk.Frame(self.root)
        self.loginForm.pack()

        ttk.Label(self.loginForm, text="Username:").grid(row=0, column=0, sticky='W')
        ttk.Entry(self.loginForm).grid(row=0, column=1)

        ttk.Label(self.loginForm, text="Password:").grid(row=1, column=0, sticky='W')
        ttk.Entry(self.loginForm, show="*").grid(row=1, column=1)

        ttk.Button(self.loginForm, text="Login").grid(row=2, column=1, sticky='E')

        self.tweetForm = ttk.Frame(self.root)
        self.tweetForm.pack()

        ttk.Label(self.tweetForm, text="New Tweet:").grid(row=0, column=0, sticky='W')
        ttk.Entry(self.tweetForm).grid(row=0, column=1)

        ttk.Button(self.tweetForm, text="Post").grid(row=1, column=1, sticky='E')

def main():
    root = tk.Tk()
    UserInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```