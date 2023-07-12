from tkinter import *
from tkinter.ttk import Treeview, Button

def center_window():
    screen_width = compiler.winfo_screenwidth()
    screen_height = compiler.winfo_screenheight()
    position_top = int(screen_height / 24)
    position_right = int(screen_width / 6)
    compiler.geometry("{0}x{1}+{2}+{3}".format(1200, 800, position_right, position_top))

compiler = Tk()
compiler.title('Thalis')
compiler.minsize(width=500, height=700)

h = PanedWindow(compiler, orient=HORIZONTAL)
h.pack(fill=BOTH, expand=1)

first_frame = PanedWindow(h, bg="white", bd=2, relief=SUNKEN, orient=VERTICAL)
first_frame_subframe1 = Treeview(first_frame)

def add_items():
    first_frame_subframe1.insert('', 'end', 'head1', text='Heading 1')
    first_frame_subframe1.insert('', 'end', 'head2', text='Heading 2')
    first_frame_subframe1.insert('', 'end', 'head3', text='Heading 3')

add_items() #call this function once at the start

def go_back(frame_to_hide):
    frame_to_hide.pack_forget()
    add_items()
    first_frame_subframe1.pack()

def toggle_textbox(event):
    selected_item = first_frame_subframe1.selection()[0]

    if isinstance(getattr(compiler, selected_item, None), type(None)):
        setattr(compiler, selected_item, Frame(first_frame))
        getattr(compiler, selected_item).pack()

        textbox = Text(getattr(compiler, selected_item))
        textbox.insert(END, 'This is a Text box under Heading {0}'.format(selected_item[-1]))
        textbox.pack()

        Button(getattr(compiler, selected_item), text="Back", command=lambda: go_back(getattr(compiler, selected_item))).pack()  
    else:
        first_frame_subframe1.delete(*first_frame_subframe1.get_children())
        first_frame_subframe1.pack_forget() 
        getattr(compiler, selected_item).pack()

first_frame_subframe1.bind('<<TreeviewSelect>>', toggle_textbox)
first_frame_subframe1.pack()

first_frame_subframe2 = Frame(first_frame, bg="white", bd=1, relief=SUNKEN)
first_frame.add(first_frame_subframe1, minsize=100)
first_frame.add(first_frame_subframe2, minsize=100)
second_frame = Frame(h, bg="light blue", bd=2, relief=SUNKEN)
third_frame = Frame(h, bg="white", bd=2, relief=SUNKEN)

h.add(first_frame, minsize=200)
h.add(second_frame, minsize=200)
h.add(third_frame, minsize=200)

center_window()
compiler.mainloop()
