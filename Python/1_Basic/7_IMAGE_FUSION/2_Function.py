import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import os
from PIL import Image 

root = Tk()
root.title("MINEW IMAGE FUSION")
root.geometry("+2000+300")

# Add/Del
def add_file():
    files = filedialog.askopenfilenames(title="Select Image",
                                        filetypes=(("JPG File", "*.jpg"),("All Files", "*.*")),
                                        initialdir="/Users/vision/academy/python/Python_JJM/ImageFusion/image")
    for file in files:
        list_file.insert(END, file)

def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# Save path
def browse_dest_path() :
    folder_selected = filedialog.askdirectory(initialdir="/Users/vision/academy/python/Python_JJM/ImageFusion/image")
    if folder_selected == "" : 
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, folder_selected)

# Fusion image
def fusion_images() :

    # Option - Width
    img_width = cmb_width.get()
    if img_width == "Original" :
        img_width = -1
    else :
        img_width = int(img_width)

    # Option - Format
    img_format = cmb_format.get().lower()

    # Option - Space
    img_space = cmb_space.get()
    if img_space == "Slim" :
        img_space = 30
    elif img_space == "Normal" :
        img_space = 60
    elif img_space == "Apart" :
        img_space = 90
    else :
        img_space = 0

    images = [Image.open(x) for x in list_file.get(0,END)]

    # Option Apply
    image_sizes = []
    if img_width > -1:
        image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
    else :
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    widths, heights = zip(*(image_sizes))

    max_width, total_height = max(widths), sum(heights)

    if img_space > 0 :
        total_height += (img_space * (len(images) -1))

    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0

    for idx, img in enumerate(images) :
        if img_width > -1:
            img = img.resize(image_sizes[idx])

        result_img.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_space)

        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

        # Option - Format Apply
        file_name = "fusioned_image." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("Notice", "Done")

# Start
def start():
    # Check File List
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add image files")
        return

    # Check Save Path
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Select save path")
        return
    
    # Get Option
    fusion_images()
    # Run






# File Frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="Add Files", command=add_file)
btn_add_file.pack(side="left", padx=5, pady=5)

btn_del_file = Button(file_frame, text="Delete", command=del_file)
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
frame_option = LabelFrame(root, text="Option")
frame_option.pack(fill="x", padx=5, pady=5, ipady=5)

# 1. Width 
lbl_width = Label(frame_option, text="Width(px)", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. File format
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)
                
opt_format = ["JPG", "PNG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 3. Space
lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["None", "Slim", "Normal", "Apart"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# Progress Bar
frame_progress = LabelFrame(root, text="Progress state")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Excute Frame
frame_run = Frame(root)
frame_run.pack(side="right", padx=5, pady=5, ipady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()