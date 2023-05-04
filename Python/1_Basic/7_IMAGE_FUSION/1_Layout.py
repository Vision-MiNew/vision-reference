import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("MINEW IMAGE FUSION")
root.geometry("+2000+300")




def browse_dest_path() :
    pass

# File Frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="Add Files")
btn_add_file.pack(side="left", padx=5, pady=5)

btn_del_file = Button(file_frame, text="Delete")
btn_del_file.pack(side="right", padx=5, pady=5)

# List Frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scr = Scrollbar(list_frame)
scr.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scr.set)
list_file.pack(side="left", fill="both", expand=True)
scr.config(command=list_file.yview)

# Save path Frame
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="Browse..", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Option Frame
# 1. Width
# 2. Space
# 3. File format

# Progress Bar
frame_progress = LabelFrame(root, text="Progress state")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Excute Frame
frame_run = Frame(root)
frame_run.pack(side="right", padx=5, pady=5, ipady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()