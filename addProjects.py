from tkinter import *


def add_new_projects(text_frame):

    project_name_label = Label(text_frame, text="Enter your project name here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)

    project_name_entry = Entry(text_frame, width=50, font="Helvetica 20 italic")
    project_name_entry.pack(pady=10)

    add_description_label = Label(text_frame, text="Enter your project description here", font="Helvetica 16 italic")
    add_description_label.pack(pady=10)

    project_description_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    project_description_text.pack(pady=10)

    button_submit = Button(text_frame, text="SUBMIT\n ALL THE BEST !!", font="Helvetica 16 italic", relief=RAISED,
                           bg="white")
    button_submit.pack(pady=10)


def add_new_project_button(frame):

    frame.tkraise()