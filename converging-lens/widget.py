import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import subprocess
import pickle



root = tk.Tk()
root.geometry("300x250")
root.resizable(False, False)
root.title('Sign In')

f = tk.StringVar()
AB = tk.StringVar()
OA = tk.StringVar()
scale = tk.StringVar()

def submited():
    
    subprocess.run(["python", "main.py"])
    data = [f.get(),AB.get(),OA.get(),scale.get()]
    file = open('data', 'wb')
    pickle.dump(data, file)
    
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)



f_label = ttk.Label(signin, text="OF length : ")
f_label.pack(fill='x', expand=True)

f_entry = ttk.Entry(signin, textvariable=f)
f_entry.pack(fill='x', expand=True)
f_entry.focus()

AB_label = ttk.Label(signin, text="AB size : ")
AB_label.pack(fill='x', expand=True)

AB_entry = ttk.Entry(signin, textvariable=AB)
AB_entry.pack(fill='x', expand=True)

OA_label = ttk.Label(signin, text="OA length : ")
OA_label.pack(fill='x', expand=True)

OA_entry = ttk.Entry(signin, textvariable=OA)
OA_entry.pack(fill='x', expand=True)

scale_label = ttk.Label(signin, text="scale 1 (reality): x (screen)")
scale_label.pack(fill='x', expand=True)

scale_entry = ttk.Entry(signin, textvariable=scale)
scale_entry.pack(fill='x', expand=True)

submit_button = ttk.Button(signin, text="create schematic", command=submited)
submit_button.pack(fill='x', expand=True, pady=10)


root.mainloop()