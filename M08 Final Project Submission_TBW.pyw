import tkinter as tk

def order_pizza():
    # Your pizza ordering logic here
    print("Pizza ordered!")

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")

# Add labels and buttons
label = tk.Label(root, text="Welcome to Pizza Heaven!")
label.pack()

order_button = tk.Button(root, text="Order Pizza", command=order_pizza)
order_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack()

root.mainloop()
