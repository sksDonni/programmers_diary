from tkinter import *
from tkinter import ttk

def add_new_issues(text_frame):
    options = ["Sensei", "programmer's diary"]
    project_name_label = Label(text_frame, text="Choose your project here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)

    variable = StringVar(text_frame)
    variable.set(options[0])

    opt = OptionMenu(text_frame, variable, *options)
    opt.config(width=60, font=('Helvetica', 16, "italic"))
    opt.pack(pady=10)

    issue_name_label = Label(text_frame, text="Name the issue", font="Helvetica 16 italic")
    issue_name_label.pack(pady=10)

    issue_name_entry = Entry(text_frame, font="Helvetica 16 italic", width=60)
    issue_name_entry.pack(pady=10)

    issue_state_frame = Frame(text_frame)
    issue_state_frame.pack(pady=10)

    issue_bool_state_label = Label(issue_state_frame, text="The state of the issue", font="Helvetica 16 italic")
    issue_bool_state_label.pack(pady=10)

    active_state_button = ttk.Radiobutton(issue_state_frame, text="Active", variable="state", value="active",
                                          )
    inactive_state_button = ttk.Radiobutton(issue_state_frame, text="In-Active", variable="state", value="inactive",
                                            )
    active_state_button.pack(pady=10, padx=10, side=LEFT)
    inactive_state_button.pack(pady=10, padx=10, side=LEFT)

    describe_issue_label = Label(text_frame, text="Describe The Issue", font="Helvetica 16 italic")
    describe_issue_label.pack(pady=10)
    issue_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    issue_text.pack(pady=10)

    button_post_issue = Button(text_frame, text="POST ISSUE", font="Helvetica 16 italic", bg="white")
    button_post_issue.pack()


def add_new_issue_button(frame):
    frame.tkraise()