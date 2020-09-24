from tkinter import *

root = Tk()
root.title("Programmer's Diary")

title_frame = Frame(root, width=500)
title_frame.grid(row=0, column=0)

title_label = Label(title_frame, text="Programmer's diary", font="Helvetica 20 bold")
title_label.pack(fill="x", expand=1, padx=30, pady=30)

button_frame = Frame(root)
button_frame.grid(row=1, column=0)

button_add_project = Button(button_frame, text="Add new project", font="Helvetica 16 italic")
button_add_project.pack(side=LEFT)

button_add_issue = Button(button_frame, text="Add new issue", font="Helvetica 16 italic")
button_add_issue.pack(side=LEFT, padx=20)

button_view_issues = Button(button_frame, text="View issues", font="Helvetica 16 italic")
button_view_issues.pack(side=LEFT, padx=20)

button_post_solution = Button(button_frame, text="Solution", font="Helvetica 16 italic")
button_post_solution.pack(side=LEFT, padx=20)


text_frame = Frame(root)
text_frame.grid(row=2, column=0, padx=20)

project_name_label = Label(text_frame, text="Enter your project name here", font="Helvetica 16 italic")
project_name_label.pack(pady=10)

project_name_entry = Entry(text_frame, width=50, font="Helvetica 20 italic")
project_name_entry.pack(pady=10)

issue_name_label = Label(text_frame, text="Enter your issue here", font="Helvetica 16 italic")
issue_name_label.pack(pady=10)

issue_name_entry = Entry(text_frame, width=50, font="Helvetica 20 italic")
issue_name_entry.pack(pady=10)

tried_description_label = Label(text_frame, text="Describe methods tried", font="Helvetica 16 italic")
tried_description_label.pack(pady=10)

tried_description_entry = Entry(text_frame, width=50, font="Helvetica 20 italic")
tried_description_entry.pack(pady=10)

root.mainloop()