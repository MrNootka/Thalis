from tkinter import Frame, Button, Label, Entry, font
from features.projects.create_project import CreateProjectForm

class ProjectsInterface(Frame):
    def __init__(self, parent, tab, tab_control, button_frame):
        Frame.__init__(self, parent)
        self.button_frame = button_frame
        self.tab = tab
        self.tab_control = tab_control

        self.pack(fill="both", expand=True)

        self.close_button_frame = Frame(self)
        self.close_button_frame.pack(side='top', fill='x')
        
        self.close_button = Button(self.close_button_frame, text='X', command=lambda: self.close_tab(tab_control.index(self.tab)), font=("Arial", 15))

        self.close_button.pack(side='right')

        self.rest_frame = Frame(self)
        self.rest_frame.pack(side="top")

        self.new_project_button = Button(self.rest_frame, text="New project", command=self.new_project, font=("Arial", 15))
        self.or_label = Label(self.rest_frame, text="OR", font=font.Font(size=25, family="Arial"))
        self.open_project_button = Button(self.rest_frame, text="Open project", command=self.open_project, font=("Arial", 15))

        self.new_project_button.grid(row=0, column=0, padx=(20, 10))
        self.or_label.grid(row=0, column=1)
        self.open_project_button.grid(row=0, column=2, padx=(10, 20))

        self.create_project_form = CreateProjectForm(self)
        self.create_project_form.pack(fill='x')
        self.create_project_form.pack_forget()

    def close_tab(self, tab_index):
        self.tab_control.forget(tab_index)
    
    def hide_buttons(self):  
        self.new_project_button.grid_remove()
        self.or_label.grid_remove()
        self.open_project_button.grid_remove()
    
    def show_buttons(self):
        self.new_project_button.grid()
        self.or_label.grid()
        self.open_project_button.grid()

    def new_project(self):  
        self.hide_buttons()
        self.create_project_form.pack()

    def open_project(self):
        print("Open project clicked")

    def display_frame(self, frame_class):
        new_frame = frame_class(self.container, self)
        self.current_frame = new_frame
        self.current_frame.pack(fill='both', expand=True)

    def go_back(self):
        self.current_frame.destroy()
        self.display_frame(ProjectsInterface)
