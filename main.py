# import statements goes here!
from tkinter import *
from addProjects import *
from addIssues import *
from postSolution import *
from viewIssues import *
import create_widgets

# Basic initialisation of tkinter window
root = Tk()
root.geometry("800x700")
root.title("programmer's diary")

# Creating a main frame and a main canvas to add scrollbar to frames
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1, padx=20, pady=20)
main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
main_canvas.pack_propagate("1")
second_frame = create_widgets.create_scrollbar(main_canvas, main_frame) # Creates a scrollbar

# Title frame and label -->
title_frame = Frame(second_frame, width=500)
title_frame.grid(row=0, column=0)
title_label = Label(title_frame, text="Programmer's diary", font="Helvetica 20 bold")
title_label.pack(fill="x", expand=1, padx=30, pady=30)

# button frame to add all buttons in a row
button_frame = Frame(second_frame)
button_frame.grid(row=1, column=0, padx=20)

# Button to raise frame to add new projects and project description
button_add_project = Button(button_frame, text="Add new project", font="Helvetica 16 italic",
                            command=lambda:create_widgets.frame_raise(add_project_frame))
button_add_project.pack(side=LEFT)

# Button to raise frame to add new issues
button_add_issue = Button(button_frame, text="Add new issue", font="Helvetica 16 italic",
                          command=lambda:create_widgets.frame_raise(add_new_issues_frame))
button_add_issue.pack(side=LEFT, padx=20)

# Button to raise frame to view issues and progress and contemplate on it
button_view_issues = Button(button_frame, text="View issues", font="Helvetica 16 italic",
                            command=lambda:create_widgets.frame_raise(view_issues_frame))
button_view_issues.pack(side=LEFT, padx=20)

# Button to raise frame to update steps that have been done
button_post_steps = Button(button_frame, text="Update Steps", font="Helvetica 16 italic",
                              command=lambda:create_widgets.frame_raise(post_solution_frame))
button_post_steps.pack(side=LEFT, padx=20)


# Frames to add functionality
add_project_frame = Frame(second_frame, width=400, height=800)
add_new_issues_frame = Frame(second_frame, width=400, height=800)
view_issues_frame = Frame(second_frame, width=400, height=800)
post_solution_frame = Frame(second_frame, width=400, height=800)

# Stack frames on top of each other
frames = [add_project_frame, add_new_issues_frame, view_issues_frame, post_solution_frame]
create_widgets.place_frame(frames, 2, 0)

# Methods to populate frames
add_new_projects(add_project_frame)
add_new_issues(add_new_issues_frame)
post_solution(post_solution_frame)
view_issues(view_issues_frame)

root.mainloop()