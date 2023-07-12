from tkinter import Entry, Button, StringVar, Label, Frame
from features.projects.project_frame import ProjectFrame


class CreateProjectForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent 
        
        Label(self, text="Create Project", font=("Arial", 30)).grid(row=0,column=0, columnspan=2)

        Label(self, text="Project name:", font=("Arial", 15)).grid(row=1, column=0)

        self.project_name = Entry(self, width=30)
        self.project_name.grid(row=1, column=1)

        Label(self, text="Description:", font=("Arial", 15)).grid(row=2, column=0)
        self.description = Entry(self, width=40)
        self.description.grid(row=2, column=1)

        Label(self, text="Would you like to import:", font=("Arial", 15)).grid(row=3, column=0)
        Button(self, text="Import folder", font=("Arial", 15), command=self.import_folder).grid(row=3, column=1)
        Button(self, text="Nothing", font=("Arial", 15)).grid(row=3, column=2)
        Button(self, text="Import files", font=("Arial", 15), command=self.import_files).grid(row=3, column=3)

        self.back_button = Button(self, text="Back", font=("Arial", 15), command=self.back_to_projects)
        self.back_button.grid(row=4, column=0)

        Button(self, text="Next", font=("Arial", 15), command=self.next).grid(row=4, column=1)


    def import_folder(self):
        print("Importing folder")

    def import_files(self):
        print("Importing files")

    def back_to_projects(self):
        self.parent.show_buttons()
        self.pack_forget()

    def next(self):
        self.pack_forget()
        self.template_project_interface = ProjectFrame(self.parent)
        self.template_project_interface.pack(fill='x')
