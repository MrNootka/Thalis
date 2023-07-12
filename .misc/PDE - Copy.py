from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename, askdirectory
from tkinter import PanedWindow, VERTICAL
from tkinter.messagebox import showinfo
from tkinter import ttk
import subprocess
import os

compiler = Tk()
compiler.title('My Fantastic IDE')

global is_folder_visible
is_folder_visible = False


global folder_path
folder_path = ''
file_path = ''

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


from pathlib import Path
root_path = Path(__file__).parent.absolute()  
folder_symbol = "\uD83D\uDCC1"  
file_symbol = "\uD83D\uDCC4"  

folder_history = []


def open_folder():
    global folder_path
    path = askdirectory()
    if path:
        folder_history.append(path)
        folder_path = path
        display_folder_contents(path)

def open_file_from_list(event):
    global folder_path
    index = files_list.curselection()[0]
    filename = files_list.get(index)[2:]    
    filepath = os.path.join(folder_path, filename)

    if os.path.isdir(filepath): 
        folder_history.append(filepath)
        folder_path = filepath
        display_folder_contents(filepath)
    else:
       
        open_file(filepath)

def display_folder_contents(path):
    files_list.delete(0, END) 
    for filename in os.listdir(path):  
        filepath = os.path.join(folder_path, filename)
        if os.path.isdir(filepath):
           
            files_list.insert(END, folder_symbol + " " + filename)
        else:
            
            files_list.insert(END, file_symbol + " " + filename)
    set_file_path(path)
        

folder_future = []

def go_back():
    global folder_path
    if len(folder_history) > 1:
        folder_future.append(folder_history.pop())  
        folder_path = folder_history[-1] 
        display_folder_contents(folder_path)

def go_forward():
    global folder_path
    if folder_future:  
        folder_path = folder_future.pop()  
        folder_history.append(folder_path) 
        display_folder_contents(folder_path)



def toggle_folder_view():
    global is_folder_visible

    is_folder_visible = not is_folder_visible

    if is_folder_visible:
        second_frame.pack(side=LEFT)
    else:
        second_frame.pack_forget()

def save_as():
    path = asksaveasfilename(filetypes=[('All Files', '*.*')])
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)



second_frame = Frame(compiler, width=200, bg="white")
# Define chat_display in the second_frame   
chat_display = Text(second_frame, height=10)
chat_display.pack(side=BOTTOM) # Place it at the bottom of the second_frame.

def chat_output():
    message = 'Hello world!'
    chat_display.delete('1.0', END)
    chat_display.insert('1.0', message)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    
    # Get the file extension (without dot)
    ext = os.path.splitext(file_path)[-1][1:]
    
    # Define commands for different file extensions
    cmd_dict = {'py': 'python', 'js': 'node', 'java':'javac', 'rb': 'ruby'}
    
    # Check if specified extension found in our cmd_dict
    if ext in cmd_dict:
        command = f'{cmd_dict[ext]} {file_path}'
    else:  
        chat_display.delete('1.0', END)
        chat_display.insert('1.0', "Sorry! Can't execute this type of file.")
        return
  
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New File', command=create_new_file)
file_menu.add_command(label='Open File', command=open_file)
file_menu.add_command(label='Open Folder', command=open_folder)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)
h = PanedWindow(compiler, orient=HORIZONTAL)
h.pack(fill=BOTH, expand=1)

first_frame = Frame(h, width=200, bg="black")

folder_button = Button(first_frame, text='📁', command=open_folder)
folder_button.pack(side=TOP)

chat_button = Button(first_frame, text='💬', command=chat_output)
chat_button.pack(side=TOP)

h.add(first_frame)


second_frame = Frame(h, width=200, bg="white")  # Initiating the frame here

files_list = Listbox(second_frame)
files_list.pack(side=LEFT, fill=BOTH, expand=True)
files_list.bind('<<ListboxSelect>>', open_file_from_list)

h.add(second_frame)
back_button = Button(first_frame, text='←', command=go_back)
back_button.pack(side=TOP)

forward_button = Button(first_frame, text='→', command=go_forward)
forward_button.pack(side=TOP)

third_frame = Frame(h)
v = PanedWindow(third_frame, orient=VERTICAL)  
v.pack(fill=BOTH, expand=True)

editor = Text(v)
v.add(editor)

code_output = Text(v, height=10)
v.add(code_output)

h.add(third_frame)

compiler.mainloop()
