from tkinter import Canvas, Entry, Frame, Text, Toplevel, Tk
import tkinter as tk
from tkinter.ttk import Button, Style

class MoveableFrame(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_propagate(0)

        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)

        self.text_widget = Text(self, height=5, width=20)
        self.text_widget.pack(side="left", fill="both")
        self.text_widget.bind("<ButtonPress-1>", self.start_move)
        self.text_widget.bind("<ButtonRelease-1>", self.stop_move)
        self.text_widget.bind("<B1-Motion>", self.do_move)

        self.close_button = Button(self, text="Close", command=self.close)
        self.close_button.pack(side="left")

        self.send_button = Button(self, text="Send", command=self.send)  
        self.send_button.pack(side="left") 

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        delta_x = event.x - self.x
        delta_y = event.y - self.y
        x = self.winfo_x() + delta_x
        y = self.winfo_y() + delta_y
        self.place(x=x, y=y)

    def close(self):
        self.destroy()

    def send(self):  # Renamed pin to send
        pass

class ProjectTab:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent)
        self.canvas.pack(fill="both", expand=True)
        
        self.style = Style()
        self.style.configure('Add.TButton', font=('calibri', 11, 'bold'), borderwidth='1') 

        self.add_button = Button(self.canvas, text="Add Widget", command=self.add_widget, style='Add.TButton')
        self.add_button.pack(anchor="nw")

    def add_widget(self):
        widget = self.create_widget()
        widget.place(x=100, y=100)

    def create_widget(self):
        text_box = MoveableFrame(self.canvas, width=200, height=100, bg='#1A1C23')
        text_box.text_widget.delete(1.0, "end")
        text_box.text_widget.insert(1.0, "Describe the widget")
        return text_box

class MessageInputPopup(Toplevel):
    def __init__(self, title, callback):
        super().__init__()
        self.title(title)
        self.geometry("+{}+{}".format(self.winfo_screenwidth() // 2, self.winfo_screenheight() // 2))
        self.callback = callback
        self.entry = Entry(self)
        self.entry.pack(side="top", fill="Close")
        self.entry.bind('<Return>', self.send)
        self.entry.focus_set()

    def send(self, event=None):
        self.callback(self.entry.get())
        self.destroy()

def main():
    root = Tk()
    root.state('zoomed')
    button_frame = Frame(root)
    button_frame.pack(pady=20)
    ProjectTab(button_frame)
    root.mainloop()

if __name__ == "__main__":
    main()
