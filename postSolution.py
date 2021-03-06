from tkinter import *
from tkinter import ttk
from sqlite3 import *
import database_handling
import create_widgets


def update_list(project_name, text_frame):

    global issue_options_from_database, issue_options, issue_name_for_dropdown, issue_opt, issue_name_label

    issue_options_from_database = database_handling.get_issues_from_database(project_name)
    issue_options = []
    for issue in issue_options_from_database:
        issue_options.append(issue[0])

    issue_name_label = Label(text_frame, text="Name the issue", font="Helvetica 16 italic")
    issue_name_label.pack(pady=10)

    issue_name_for_dropdown = StringVar()
    issue_name_for_dropdown.set(issue_options[0])

    issue_opt = OptionMenu(text_frame, issue_name_for_dropdown, *issue_options)
    issue_opt.config(width=60, font=('Helvetica', 16, "italic"))
    issue_opt.pack(pady=10)


def destroy_widgets(project_name, text_frame, frame=None):
    issue_opt.destroy()
    issue_name_label.pack_forget()
    update_list(project_name, text_frame)


def post_solution(text_frame):

    project_options_from_database = database_handling.get_projects_from_database()
    project_options = []
    for option_from_database in project_options_from_database:
        a = option_from_database[0]
        project_options.append(a)

    project_name_for_dropdown = StringVar(text_frame)
    project_name_for_dropdown.set(project_options[0])

    project_options_frame = Frame(text_frame)
    project_options_frame.pack(pady=10)

    project_name_label = Label(project_options_frame, text="Choose your project here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)

    project_opt = OptionMenu(project_options_frame, project_name_for_dropdown, *project_options)
    project_opt.config(width=60, font=('Helvetica', 16, "italic"))
    project_opt.pack(pady=10)

    issue_frame = Frame(text_frame)
    issue_frame.pack(pady=10)

    fetch_issues_button = Button(project_options_frame, text="Fetch active issues", font="Helvetica 12 italic",
                                 command=lambda: destroy_widgets(project_name_for_dropdown.get(), issue_frame))
    fetch_issues_button.pack(side=LEFT, anchor=NE, padx=100)


    global issue_options_from_database, issue_options, issue_name_for_dropdown, issue_opt, issue_name_label

    issue_options_from_database = database_handling.get_issues_from_database(project_name_for_dropdown.get())
    issue_options = []
    for issue in issue_options_from_database:
        issue_options.append(issue[0])

    issue_name_label = Label(issue_frame, text="Name the issue", font="Helvetica 16 italic")
    issue_name_label.pack(pady=10)

    issue_name_for_dropdown = StringVar()
    issue_name_for_dropdown.set(issue_options[0])

    issue_opt = OptionMenu(issue_frame, issue_name_for_dropdown, *issue_options)
    issue_opt.config(width=60, font=('Helvetica', 16, "italic"))
    issue_opt.pack(pady=10)

    describe_solution_label = Label(text_frame, text="Update steps", font="Helvetica 16 italic")
    describe_solution_label.pack(pady=10)
    solution_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    solution_text.pack(pady=10)

    button_post_solution = Button(text_frame, text="UPDATE SOLUTION!!\nGOOD GOING", font="Helvetica 16 italic",
                                  bg="white"
                                  , command=lambda: database_handling.post_solution_to_database(project_name_for_dropdown.get(),
                                    issue_name_for_dropdown.get(), solution_text.get("1.0", "end")))
    button_post_solution.pack()