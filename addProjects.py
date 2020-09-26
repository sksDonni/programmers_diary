from tkinter import *
from sqlite3 import *
from datetime import date


def create_project(name_of_the_project, project_description):
    name_of_the_project_init = name_of_the_project.get()
    project_description_init = project_description.get("1.0", "end")
    today = date.today()
    date_of_creation = today.strftime("%d/%m/%Y")
    name_of_the_project.delete(0, 'end')
    project_description.delete("1.0", "end")
    conn = connect("projects.db")
    cursor = conn.cursor()
    print("db initiated successfully")
    cursor.execute("""CREATE TABLE IF NOT EXISTS project_names(
                    id INT PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    date_of_creation DATE TIME
                    );""")
    print("table created")
    query = """INSERT INTO project_names(name, description, date_of_creation)
                        VALUES(?,?,?)"""
    list_to_be_passed = (name_of_the_project_init, project_description_init, date_of_creation)
    cursor.execute(query, list_to_be_passed)
    conn.commit()
    print("Done")

def add_new_projects(text_frame):

    name_var = StringVar(text_frame)
    name_var = "india"
    description_var = StringVar(text_frame)
    project_name_label = Label(text_frame, text="Enter your project name here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)

    project_name_entry = Entry(text_frame, textvar=name_var, width=50, font="Helvetica 20 italic")
    project_name_entry.pack(pady=10)

    add_description_label = Label(text_frame, text="Enter your project description here", font="Helvetica 16 italic")
    add_description_label.pack(pady=10)

    project_description_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    project_description_text.pack(pady=10)

    button_submit = Button(text_frame, text="SUBMIT\n ALL THE BEST !!", font="Helvetica 16 italic", relief=RAISED, bg="white",
                            command=lambda: create_project(project_name_entry, project_description_text))
    button_submit.pack(pady=10)


def add_new_project_button(frame):

    frame.tkraise()