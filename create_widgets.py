from tkinter import ttk
from tkinter import *


# Creates a scrollbar and return the frame for further processes
def create_scrollbar(main_canvas, main_frame):
    myscrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
    myscrollbar.pack(side=RIGHT, fill=Y)
    second_frame = Frame(main_canvas)

    second_frame.bind(
        "<Configure>",
        lambda e: main_canvas.configure(
            scrollregion=main_canvas.bbox("all")
        )
    )

    main_canvas.create_window((0, 0), window=second_frame, anchor=NW, tags="inner")
    main_canvas.configure(yscrollcommand=myscrollbar.set)
    return second_frame


# Stacks frames on top of each other.
def place_frame(frame_list, row, column):
    for frame in frame_list:
        frame.grid(row=row, column=column, padx=10, pady=10)
        frame.propagate(0)


# Method to raise frame
def frame_raise(frame):
    frame.tkraise()


# Creates an options menu using the list of options and String var
def create_options_menu(frame, list_of_options, name_for_dropdown):
    opt = OptionMenu(frame, name_for_dropdown, *list_of_options)
    opt.config(width=60, font=('Helvetica', 16, "italic"))
    opt.pack(pady=10)


def make_array(list_to_be_used, index):
    options = []
    for option_from_database in list_to_be_used:
        a = option_from_database[0]
        options.append(a)

    return options


def create_new_window(list_of_steps):

    new_root = Tk()
    new_root.geometry("800x600")
    main_frame = Frame(new_root)
    main_frame.pack(fill=BOTH, expand=1, padx=20, pady=20)

    main_canvas = Canvas(main_frame)
    main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    new_frame = create_scrollbar(main_canvas, main_frame)
    for record in list_of_steps:
        date_of_step = str(record[1])
        text_to_insert = date_of_step + "\n" + record[0]
        print(text_to_insert)
        steps_entry = Text(new_frame, height=8)
        steps_entry.insert(END, text_to_insert)
        steps_entry.pack(pady=5)

    new_root.mainloop()