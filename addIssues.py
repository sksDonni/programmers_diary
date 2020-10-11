from tkinter import *
from tkinter import ttk
import database_handling
import create_widgets


# Method to populate the add new issues frame
def add_new_issues(text_frame):

    # Creates an array from the database to be used for the drop down
    options_from_database = database_handling.get_projects_from_database()
    index = 0
    options = create_widgets.make_array(options_from_database, index)

    # Drop down to choose project name
    project_name_label = Label(text_frame, text="Choose your project here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)
    project_name_for_dropdown = StringVar(text_frame)
    project_name_for_dropdown.set(options[0])
    create_widgets.create_options_menu(text_frame, options, project_name_for_dropdown)

    # Entering the new issue that has come up
    issue_name_label = Label(text_frame, text="Name the issue", font="Helvetica 16 italic")
    issue_name_label.pack(pady=10)
    issue_name_entry = Entry(text_frame, font="Helvetica 16 italic", width=60)
    issue_name_entry.pack(pady=10)

    # State of the issue i.e - either active or inactive
    issue_state_frame = Frame(text_frame)
    issue_state_frame.pack(pady=10)
    issue_bool_state_label = Label(issue_state_frame, text="The state of the issue", font="Helvetica 16 italic")
    issue_bool_state_label.pack(pady=10)
    state_of_button = StringVar()
    state_of_button.set("active")
    active_state_button = ttk.Radiobutton(issue_state_frame, text="Active", variable=state_of_button, value="active")
    inactive_state_button = ttk.Radiobutton(issue_state_frame, text="In-Active", variable=state_of_button,
                                            value="inactive")
    active_state_button.pack(pady=10, padx=10, side=LEFT)
    inactive_state_button.pack(pady=10, padx=10, side=LEFT)

    # Text box to describe the issue
    describe_issue_label = Label(text_frame, text="Describe The Issue", font="Helvetica 16 italic")
    describe_issue_label.pack(pady=10)
    issue_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    issue_text.pack(pady=10)

    # Submit button
    button_post_issue = Button(text_frame, text="POST ISSUE", font="Helvetica 16 italic", bg="white",
                               command=lambda: database_handling.create_new_issue(project_name_for_dropdown.get(),
                                    state_of_button.get(), issue_name_entry.get(), issue_text.get("1.0", "end")))
    button_post_issue.pack()