# First tkinter script
# Create by Ed 11/14

# Import modules
import tkinter

# Create the GUI main window
my_window = tkinter.Tk()

# Add widgets
tkinter.Label(my_window, text="Enter your name:").pack()

name_entry= tkinter.Entry(my_window)
name_entry.pack()


# Enter the main event loop
def hello():
    name = name_entry.get()
    label.config(text="Hello" + name + "\nToday is going to be a great day!")
tkinter.Button(my_window, text="Submit", command=hello).pack()
label = tkinter.Label(my_window, text="")
label.pack()

my_window.mainloop()