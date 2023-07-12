from tkinter import ttk, Tk, Label, Frame, Text
from tkinter.ttk import Button, Style
from tkinter.font import Font 
from ttkthemes import ThemedTk
import subprocess
import uuid
import sys
import os
from features.mySystem.mySystem_interface import MySystemInterface
from features.projects.projects_interface import ProjectsInterface
from features.thalis_aio.aio import AIOInterface   


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_new_session(self):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = None
        return session_id

    def remove_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def is_valid_session(self, session_id):
        return session_id in self.sessions


def close_tab(tab_control, index):
    frame = tab_control.nametowidget(tab_control.tabs()[index])
    tab_control.forget(frame)


def create_tab(tab_control, button_frame, session_manager, feature):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=feature)
    tab_control.select(tab)

    if feature == "mySystem":
        MySystemInterface(tab).pack(fill='both', expand=True)
    elif feature == "Query":
        print("Output of Query")
    elif feature == "Converse":
        print("Output of Converse")
    elif feature == "Projects":
        ProjectsInterface(parent=tab, tab=tab, tab_control=tab_control, button_frame=button_frame).pack(expand=1, fill='both')
    elif feature == "AIO":
        AIOInterface(tab).pack(fill='both', expand=True) 
    
    # Move to select newly created tab
    tab_control.select(tab)


def main():
    session_manager = SessionManager()
    FEATURES = ["Projects", "Query", "Converse","mySystem"]

    root = ThemedTk(theme="arc") 
    root.state('zoomed')

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    # Set default font
    default_font = Font(name='Arial', size=15)
    Style().configure('.', font=default_font)

    create_tab(tab_control, button_frame, session_manager, "AIO")
    
    for index, feature in enumerate(FEATURES):
        Button(
            button_frame, 
            text=feature, 
            style='myButtons.TButton', 
            command=lambda feature=feature: create_tab(tab_control, button_frame, session_manager, feature)
        ).grid(row=0, column=index, sticky='ew')
        
        button_frame.grid_columnconfigure(index, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
