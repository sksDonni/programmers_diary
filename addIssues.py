from tkinter import *
from tkinter import ttk
from sqlite3 import *
from datetime import date


def create_new_issue(project_name, issue_state, issue_name, issue_text):
    conn = connect("projects.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    query = """CREATE TABLE IF NOT EXISTS issues_in_projects
    (
            issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT,
            issue_name TEXT,
            issue_description TEXT,
            issue_state TEXT,
            date_of_issue DATE TIME,
            FOREIGN KEY (project_name) REFERENCES project_name_tables(project_name)
    );"""

    today = date.today()
    today = today.strftime("%d/%m/%Y")

    cursor.execute(query)

    list_to_be_inserted = (project_name, issue_name, issue_text, issue_state, today)
    print(list_to_be_inserted)
    insert_query = """INSERT INTO issues_in_projects(project_name, issue_name, issue_description,
                        issue_state, date_of_issue)
                        VALUES(?, ?, ?, ?, ?);"""

    cursor.execute(insert_query, list_to_be_inserted)
    conn.commit()
    cursor.close()
    conn.close()


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


def add_new_issues(text_frame):
    options_from_database = get_projects_from_database()
    options = []
    for option_from_database in options_from_database:
        a = option_from_database[0]
        options.append(a)

    project_name_label = Label(text_frame, text="Choose your project here", font="Helvetica 16 italic")
    project_name_label.pack(pady=10)

    project_name_for_dropdown = StringVar(text_frame)
    project_name_for_dropdown.set(options[0])

    opt = OptionMenu(text_frame, project_name_for_dropdown, *options)
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
    
    state_of_button = StringVar()
    state_of_button.set("active")
    active_state_button = ttk.Radiobutton(issue_state_frame, text="Active", variable=state_of_button, value="active")
    inactive_state_button = ttk.Radiobutton(issue_state_frame, text="In-Active", variable=state_of_button,
                                            value="inactive")
    active_state_button.pack(pady=10, padx=10, side=LEFT)
    inactive_state_button.pack(pady=10, padx=10, side=LEFT)

    describe_issue_label = Label(text_frame, text="Describe The Issue", font="Helvetica 16 italic")
    describe_issue_label.pack(pady=10)
    issue_text = Text(text_frame, font="Helvetica 16 italic", width=60, height=10)
    issue_text.pack(pady=10)

    button_post_issue = Button(text_frame, text="POST ISSUE", font="Helvetica 16 italic", bg="white",
                               command=lambda: create_new_issue(project_name_for_dropdown.get(), state_of_button.get(),
                                                                issue_name_entry.get(), issue_text.get("1.0", "end")))
    button_post_issue.pack()


def add_new_issue_button(frame):
    frame.tkraise()