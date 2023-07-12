from tkinter import Frame

class AIOInterface(Frame):
    def __init__(self, tab, *args, **kwargs):
        super().__init__(tab, *args, **kwargs)
        # Initialize what you need here
        print("Output of AIO")