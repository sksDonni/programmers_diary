from tkinter import *
from tkinter import ttk
from sqlite3 import *


def get_projects_from_database():
    conn = connect("projects.db")
    cursor = conn.cursor()
    query = """SELECT * FROM project_name_tables"""
    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    conn.close()
    return records


def get_issues_from_database(project_name):
    conn = connect("projects.db")
    cursor = conn.cursor()
    query = """SELECT * FROM issues_in_projects WHERE project_name """


def post_solution(text_frame):

    project_options = ["Sensei", "programmer's diary"]
    issue_options = ["dummy"]
    project_name_label = Label(text_frame, text="Choose your project here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)

    variable = StringVar(text_frame)
    variable.set(project_options[0])

    project_opt = OptionMenu(text_frame, variable, *project_options)
    project_opt.config(width=60, font=('Helvetica', 16, "italic"))
    project_opt.pack(pady=10)

    issue_name_label = Label(text_frame, text="Name the issue", font="Helvetica 16 italic")
    issue_name_label.pack(pady=10)

    variable = StringVar(text_frame)
    variable.set(issue_options[0])

    issue_opt = OptionMenu(text_frame, variable, *issue_options)
    issue_opt.config(width=60, font=('Helvetica', 16, "italic"))
    issue_opt.pack(pady=10)

    describe_solution_label = Label(text_frame, text="Describe the solution", font="Helvetica 16 italic")
    describe_solution_label.pack(pady=10)
    solution_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    solution_text.pack(pady=10)

    button_post_solution = Button(text_frame, text="POST SOLUTION!!\nGOOD GOING", font="Helvetica 16 italic", bg="white"
                                  , command=lambda: post_solution_to_database())
    button_post_solution.pack()


def post_solution_button(frame):
    frame.tkraise()