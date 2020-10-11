from tkinter import *
from sqlite3 import *
from datetime import date
import database_handling


# Method to populate the add projects frame
def add_new_projects(text_frame):

    # String variables for entry
    name_var = StringVar(text_frame)
    name_var.set("")
    description_var = StringVar(text_frame)

    # Add project_name
    project_name_label = Label(text_frame, text="Enter your project name here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)
    project_name_entry = Entry(text_frame, textvar=name_var, width=50, font="Helvetica 20 italic")
    project_name_entry.pack(pady=10)

    # Add description of project
    add_description_label = Label(text_frame, text="Enter your project description here", font="Helvetica 16 italic")
    add_description_label.pack(pady=10)
    project_description_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    project_description_text.pack(pady=10)

    # Submit functionality
    button_submit = Button(text_frame, text="SUBMIT\n ALL THE BEST !!", font="Helvetica 16 italic", relief=RAISED,
            bg="white",command=lambda: database_handling.create_project(project_name_entry, project_description_text))
    button_submit.pack(pady=10)