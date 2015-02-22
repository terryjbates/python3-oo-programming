from tkinter import *
# Initialize Tk and get a reference to the top-level window it 
# automatically creates.
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        # The value of the counter starts at 0.
        self.count_value = 0

    def create_widgets(self):
        # Create a label which displays the text "Count: 0", 
        # and place it into the top-level window.
        self.count_label = Label(self, text="Count: 0") 
        self.count_label.grid(row=0, column=1)
        # Make a button displaying the text "Increment". 
        # Whenever the button is clicked, it executes as a
        # command the function 'incrementCount'.
        self.incr_button = Button(self, text="Increment", 
                              command=self.increment_count) 
        # Place the button into its parent window (which is "mainWindow").
        self.incr_button.grid(row=0, column=0)
        # Make a button displaying the text "Quit":. 
        # Whenever it is clicked, it destroys the top level window.
        self.quit_button = Button(self, text="Quit", 
                          command=self.master.destroy)
        self.quit_button.grid(row=1, column=0)

    def increment_count(self):
        # Increment the counter.
        self.count_value += 1
        # Configure the counter label so that the text displayed in it is 
        # the string "Count: " followed by the number in the counter.
        self.count_label.configure(text = 'Count: ' + str(self.count_value))

app = Application()
app.master.title("Counter")
app.mainloop()
