from tkinter import *
from addProjects import *
from addIssues import *
from postSolution import *
from tkinter import ttk

root = Tk()
root.title("Programmer's Diary")
root.geometry("800x600")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1, padx=20, pady=20)

main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1, padx=10, pady=10)

myscrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
myscrollbar.pack(side=RIGHT, fill=Y)

main_canvas.configure(yscrollcommand=myscrollbar)
main_canvas.bind("<Configure>", lambda e:main_canvas.configure(scrollregion=main_canvas.bbox("all")))

second_frame = Frame(main_canvas)
main_canvas.create_window((0,0), window=second_frame, anchor=NW)

title_frame = Frame(second_frame, width=500)
title_frame.grid(row=0, column=0)

title_label = Label(title_frame, text="Programmer's diary", font="Helvetica 20 bold")
title_label.pack(fill="x", expand=1, padx=30, pady=30)

button_frame = Frame(second_frame)
button_frame.grid(row=1, column=0, padx=20)

button_add_project = Button(button_frame, text="Add new project", font="Helvetica 16 italic",
                            command=lambda:add_new_project_button(add_project_frame))
button_add_project.pack(side=LEFT)

button_add_issue = Button(button_frame, text="Add new issue", font="Helvetica 16 italic",
                          command=lambda:add_new_issue_button(add_new_issues_frame))
button_add_issue.pack(side=LEFT, padx=20)

button_view_issues = Button(button_frame, text="View issues", font="Helvetica 16 italic")
button_view_issues.pack(side=LEFT, padx=20)

button_post_solution = Button(button_frame, text="Solution", font="Helvetica 16 italic",
                              command=lambda :post_solution_button(post_solution_frame))
button_post_solution.pack(side=LEFT, padx=20)


add_project_frame = Frame(second_frame, width=400, height=800)
add_new_issues_frame = Frame(second_frame, width=400, height=800)
view_issues_frame = Frame(second_frame, width=400, height=800)
post_solution_frame = Frame(second_frame, width=400, height=800)


frames = [add_project_frame, add_new_issues_frame, view_issues_frame, post_solution_frame]

for frame in frames:
    frame.grid(row=2, column=0, padx=10, pady=10)
    frame.propagate(0)

add_new_projects(add_project_frame)
add_new_issues(add_new_issues_frame)
post_solution(post_solution_frame)

root.mainloop()