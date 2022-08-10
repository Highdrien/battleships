import tkinter as tk


def verification(event=None):
    global User
    User = ID.get()
    windows.destroy()


User = 'User'

windows = tk.Tk()
windows.title('Identification required')

Label1 = tk.Label(windows, text='Log in :')
Label1.pack(side=tk.LEFT, padx=5, pady=5)

ID = tk.StringVar()
Champ = tk.Entry(windows, textvariable=ID, font="20", bg='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side=tk.LEFT, padx=5, pady=5)

Button = tk.Button(windows, text='Confirm', command=verification)
Button.pack(side=tk.LEFT, padx=5, pady=5)

windows.bind('<Return>', verification)

windows.mainloop()

if __name__ == "__main__":
    print(User)
