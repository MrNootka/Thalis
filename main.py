from tkinter import ttk, Tk, Label, Frame, Text
from tkinter.ttk import Button, Style
from ttkthemes import ThemedTk
import subprocess
import uuid
import sys
import os

from features.projects.projects_interface import ProjectTab
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


def create_tab(tab_control, session_manager, feature):
    tab = Frame(tab_control)
    tab_control.add(tab, text=feature)
    tab_control.select(tab)

    close_button = Button(tab, text='X', command=lambda: close_tab(tab_control, tab_control.index(tab)))
    close_button.pack(anchor="nw")  # changed from 'ne' to 'nw'

    if feature == "Query":
        txt = Text(tab)
        txt.insert('1.0', "Output of Query")
    elif feature == "mySystem":
        txt = Text(tab)
        txt.insert('1.0', "Output of mySystem")
    elif feature == "Converse":
        txt = Text(tab)
        txt.insert('1.0', "Output of Converse")
    elif feature == "Project":
        project_tab = ProjectTab(tab)



def main():
    session_manager = SessionManager()
    FEATURES = ["Projects", "Query", "Converse","mySystem" ]

    root = ThemedTk(theme="arc")  # Set the theme to "arc"
    root.state('zoomed')

    button_frame = Frame(root)
    button_frame.pack(pady=20)

    add_button = Button(button_frame,text="Add Widget")
    add_button.grid(row=0, column=len(FEATURES), sticky='ew')
    add_button.grid_remove()

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    for index, feature in enumerate(FEATURES):
        Button(button_frame,text=feature,command=lambda feature=feature: create_tab(tab_control, session_manager, feature)).grid(row=0, column=index, sticky='ew')
        button_frame.grid_columnconfigure(index, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()