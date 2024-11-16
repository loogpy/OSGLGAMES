import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Hello World App")

# Create a label with the text "Hello, World!"
label = tk.Label(root, text="Hello, World!")

# Pack the label onto the window
label.pack()

# Run the application
root.mainloop()
