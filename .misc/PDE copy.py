from tkinter import *
from pathlib import Path
import subprocess
import os

compiler = Tk()
compiler.title('Thalis')
compiler.minsize(width=500,height=700)  
global frames_list 
frames_list = []

def center_window():
    screen_width = compiler.winfo_screenwidth()
    screen_height = compiler.winfo_screenheight()

    position_top = int(screen_height / 24)
    position_right = int(screen_width / 6)

    compiler.geometry("{}x{}+{}+{}".format(1200, 800, position_right, position_top))





def create_new_frame():
    global frames_list
    new_frame_width = 500 # Calculated for 5cm on a standard 96 dpi screen

    for f in frames_list:
        f.config(width=new_frame_width)

    new_frame = Frame(h, width=new_frame_width, bg="white")

    top_frame = Frame(new_frame)
    top_frame.pack(fill=X)

    message_entry = Entry(top_frame, bd=2, relief=SUNKEN)
    message_entry.pack(side=LEFT, fill=BOTH, padx=5, expand=True)

    send_button = Button(top_frame, text="Send")
    send_button.pack(side=LEFT, padx=5)

    left_button = Button(top_frame, text="<<")
    left_button.pack(side=LEFT, padx=5)

    right_button = Button(top_frame, text=">>")
    right_button.pack(side=LEFT, padx=5)

    close_button = Button(top_frame, text="x", command=lambda: delete_frame(new_frame))
    close_button.pack(side=RIGHT, padx=5)

    new_frame.config(width=new_frame_width)
    frames_list.append(new_frame)
    h.add(new_frame)
    h.update_idletasks()
    compiler.update()

def delete_frame(frame):
    frame.destroy()
    frames_list.remove(frame)

    new_frame_width = h.winfo_width() // (len(frames_list) if len(frames_list) != 0 else 1)
    for f in frames_list:
        f.config(width=new_frame_width)


def set_file_path(path):
    global file_path
    file_path = path

def open_file(path=None):
    if path is None: 
        path = askopenfilename(filetypes=[('All Files', '*.*')])
        
    try:
        with open(path, 'r') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
            set_file_path(path)
    except:
        with open(path, 'rb') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
            set_file_path(path)

def create_new_file():
    editor.delete(1.0, "end")
    set_file_path("")

def open_folder():
    global folder_path
    path = askdirectory()
    if path:
        folder_history.append(path)
        folder_path = path
        display_folder_contents(path)

def save_as():
    path = asksaveasfilename(filetypes=[('All Files', '*.*')])
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

######## Top bar
plus_button = Label(compiler, height=1, width=compiler.winfo_screenwidth(), text='+', font=('Arial', 14), bg='gray', fg='white')
plus_button.pack(fill=X)
plus_button.bind("<Button-1>", lambda e: create_new_frame())

#IDK 100%
h = PanedWindow(compiler, orient=HORIZONTAL)
h.pack(fill=BOTH, expand=1)

center_window()
compiler.mainloop()

