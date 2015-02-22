from tkinter import *
# Initialize Tk and get a reference to the top-level window it 
# automatically creates.
main_window = Tk()
# Create a label which displays the text "Count: 0", and place it into the 
# top-level window.
count_label = Label(main_window, text="Count: 0") 
count_label.grid(row=0, column=1)
# The value of the counter starts at 0.
count_value = 0
# This function is called whenever the "Increment" button 
# (defined below) is clicked
def increment_count():
    global count_value, count_label
    # Increment the counter.
    count_value = count_value + 1
    # Configure the counter label so that the text displayed in it is the 
    # string "Count: " followed by the number in the counter.
    count_label.configure(text = 'Count: ' + str(count_value))
# Make a button displaying the text "Increment". 
# Whenever the button is clicked, it executes as a
# command the function 'incrementCount'.
incr_button = Button(main_window, text="Increment", 
                      command=increment_count) 
# Place the button into its parent window (which is "mainWindow").
incr_button.grid(row=0, column=0)
# Make a button displaying the text "Quit":. 
# Whenever it is clicked, it destroys the top level window.
quit_button = Button(main_window, text="Quit", 
                   command=main_window.destroy)
# Place the button into its parent window (which is "mainWindow").
quit_button.grid(row=1, column=0)

mainloop()
