from tkinter import *
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


def fetch_issues(project_name, text_frame, frame=None):
    issue_opt.destroy()
    issue_name_label.pack_forget()
    update_list(project_name, text_frame)


# Method to populate the view issues frame
def view_issues(text_frame):
    
    # Creating a string variable for the drop down
    project_name_for_dropdown = StringVar(text_frame)
    project_options_from_database = database_handling.get_projects_from_database()
    index = 0
    project_options = create_widgets.make_array(project_options_from_database, index)
    project_name_for_dropdown.set(project_options[0])

    # Creates a projects option menu in the project_options_frame
    project_options_frame = Frame(text_frame)
    project_options_frame.pack(pady=10)
    project_name_label = Label(project_options_frame, text="Choose your project here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)
    create_widgets.create_options_menu(text_frame, project_options, project_name_for_dropdown)
    issue_frame = Frame(text_frame)
    issue_frame.pack(pady=10)
    
    # Button to fetch the issues of the project
    fetch_issues_button = Button(project_options_frame, text="Fetch active issues", font="Helvetica 12 italic",
                                 command=lambda: fetch_issues(project_name_for_dropdown.get(), issue_frame))
    fetch_issues_button.pack(side=LEFT, anchor=NE, padx=100)

    # Global variables to destroy the widgets in order to refresh them
    global issue_options_from_database, issue_options, issue_name_for_dropdown, issue_opt, issue_name_label

    # Creates an array from the database for the options menu
    index = 0
    issue_options_from_database = database_handling.get_issues_from_database(project_name_for_dropdown.get())
    issue_options = create_widgets.make_array(issue_options_from_database, index)

    # Creates an options menu to choose issues
    issue_name_label = Label(issue_frame, text="Name the issue", font="Helvetica 16 italic")
    issue_name_label.pack(pady=10)
    issue_name_for_dropdown = StringVar()
    issue_name_for_dropdown.set(issue_options[0])
    issue_opt = OptionMenu(issue_frame, issue_name_for_dropdown, *issue_options)
    issue_opt.config(width=60, font=('Helvetica', 16, "italic"))
    issue_opt.pack(pady=10)

    view_progress_button = Button(text_frame, text="View Progress !!", font="Helvetica 12 italic",
                                  command=lambda: database_handling.view_solution(issue_name_for_dropdown.get(), text_frame))
    view_progress_button.pack(pady=10)