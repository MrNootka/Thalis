from tkinter import Frame, Button, Label
from .mySystem_plugins.system_cleaner.space_cleaner import clean_space

class MySystemInterface(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.clean_button = Button(self, text="Clean Space", command=self.clean_space, font=("Arial", 15))
        self.clean_button.pack(pady=20)

        self.status_label = Label(self, text="", font=("Arial", 15))
        self.status_label.pack()

    def clean_space(self):
        self.status_label.config(text="Cleaning...")
        clean_space()   # this is where you call your function to clean space
        self.status_label.config(text="Cleaned Successfully!")
