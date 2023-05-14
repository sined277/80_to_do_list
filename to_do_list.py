from tkinter import *
from tkinter import messagebox

# Initialize the Tkinter window
window = Tk()
window.title("To-Do List App")

bg_color = "#ececec"
fg_color = "#333333"
window.config(bg=bg_color)

# Setting up the fonts
font_title_text = ('Comic Sans MS', 24, 'bold')

# Create a list to store to-do items
to_do_list = []


# Function to add item to the list
def add_item():
    item = input_box.get()
    if item == "":
        messagebox.showwarning("Warning", "Please enter an item to add to the list!")
    else:
        to_do_list.append(item)
        input_box.delete(0, END)
        list_box.insert(END, item)


# Function to remove selected item from the list
def remove_item():
    try:
        item_index = list_box.curselection()[0]
        item = list_box.get(item_index)
        confirm = messagebox.askquestion("WARNING", f"You want to delete '{item}'?")
        if confirm == 'yes':
            list_box.delete(item_index)
            to_do_list.remove(item)
    except IndexError:
        messagebox.showwarning("WARNING", "Please select an item to remove from the list!")


# Creating the label for the test title and text
label_title = Label(window, text="To-Do List", font=font_title_text)
label_title.grid(row=0, column=0)

# Create and position input box
input_box = Entry(window, width=30, font=font_title_text)
input_box.grid(row=1, column=0, padx=10, pady=10)

# Create and position 'Add Item' button
add_button = Button(window, text="Add Item", command=add_item, font=font_title_text, bg="#4CAF50", fg="white", borderwidth=0)
add_button.grid(row=1, column=1, padx=10, pady=10)

# Create and position list box
list_box = Listbox(window, width=30, height=3, font=font_title_text)
list_box.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

# Create and position 'Remove Item' button
remove_button = Button(window, text="Remove Item", command=remove_item, font=font_title_text, bg="#f44336", fg="white", borderwidth=0)
remove_button.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
