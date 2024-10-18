import random
import string
import tkinter as tk

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#4B0082")  
root.geometry("500x400")  

def generator_function():
    char = string.ascii_letters + string.digits
    length = lengthEntry.get()
    lengthEntry.delete(0, tk.END)
    lengthEntry.insert(0, length)
    otp = ''.join(random.choice(char) for i in range(int(length)))
    passwordEntry.insert(0, otp)

def clear():
    lengthEntry.delete(0, tk.END)
    passwordEntry.delete(0, tk.END)

mainLabel = tk.Label(root, text="Password Generator", width=20, font=("Arial", 20, "bold"), bg="#4B0082", fg="white")
mainLabel.pack(padx=10, pady=20)

lengthLabel = tk.Label(root, text="Enter Length of Password", width=23, font=("Arial", 13,"bold"), bg="#4B0082", fg="white",borderwidth=0)
lengthLabel.pack(padx=10, pady=10)

lengthEntry = tk.Entry(root, width=10, font=("Arial", 12,"bold"), borderwidth=0, justify="center")
lengthEntry.pack(padx=10, pady=10)

passwordBtn = tk.Button(root, text="Generate Password", width=20, font=("Arial", 12, "bold"), bg="#e20a0a", fg="white", borderwidth=0, relief="raised", command=generator_function)
passwordBtn.pack(padx=10, pady=10)

passwordEntry = tk.Entry(root, width=25, font=("Arial", 12,"bold"),justify="center",borderwidth=0)
passwordEntry.pack(padx=10, pady=10)


clearAll = tk.Button(root, text="Clear", width=12, font=("Arial", 12, "bold"), bg="#6dbff6", fg="white", borderwidth=0, relief="raised", command=clear)
clearAll.pack(padx=10, pady=10)

root.mainloop()
