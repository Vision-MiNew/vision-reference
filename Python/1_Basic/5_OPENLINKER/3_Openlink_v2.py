from tkinter import *
import webbrowser
import tkinter.messagebox as msgbox
import csv
import os

save_path = os.path.dirname(__file__)

with open(f"{save_path}/save.csv", 'r') as f:
    reader = csv.reader(f)
    for c in reader:
        links = c

f.close()

target_url = links[0]
now_url = target_url

root = Tk()
root.title('[MINEW] TOP 7 DIRECT LINK')
root.geometry("+2300+300")

# Infomation Section

info = """
----------------------------------
     Minsoo's Top 7 Bookmark
----------------------------------
        """

label_frame = Frame(root, padx=5, pady=5)
label_frame.pack(fill="x")

info_label = Label(label_frame, text=info)
info_label.pack(fill= 'both')

# Radiobutton Section

link_frame = Frame(root, padx=5, pady=5)
link_frame.pack()

def path_change():
    global target_url
    global now_url

    now_url = links[select_link.get()]

    path_label.config(text=now_url)
    target_url = now_url

select_link = IntVar()
link1 = Radiobutton(link_frame, pady=10,
                    text = "Google", value = 0, variable=select_link,
                    command=path_change)
link2 = Radiobutton(link_frame, pady=10,
                    text = "Naver", value = 1, variable=select_link,
                    command=path_change)
link3 = Radiobutton(link_frame, pady=10,
                    text = "Youtube", value = 2, variable=select_link,
                    command=path_change)
link4 = Radiobutton(link_frame, pady=10,
                    text = "Nate", value = 3, variable=select_link,
                    command=path_change)
link5 = Radiobutton(link_frame, pady=10,
                    text = "Amazon", value = 4, variable=select_link,
                    command=path_change)
link6 = Radiobutton(link_frame, pady=10,
                    text = "Portfolio", value = 5, variable=select_link,
                    command=path_change)
link7 = Radiobutton(link_frame, pady=10,
                    text = "Gongsaemi", value = 6, variable=select_link,
                    command=path_change)
link3.select()
link1.grid(row=1 ,column=1)
link2.grid(row=1 ,column=2)
link3.grid(row=2 ,column=1)
link4.grid(row=2 ,column=2)
link5.grid(row=3 ,column=1)
link6.grid(row=3 ,column=2)
link7.grid(row=4 ,column=1)

# Path Section

path_frame = LabelFrame(root, padx=5, pady=10, text="Link Path")
path_frame.pack()

path_label = Label(path_frame, padx=5, pady=5, text=links[2])
path_label.pack()

# Button Section

btn_frame = Frame(root, padx=5, pady=10)
btn_frame.pack()

def openlink():
    global target_url
    webbrowser.open(target_url)

def changelink():

    sub_win = Toplevel(root)
    sub_win.title('Change Link As...')
    sub_win.geometry("300x100")

    e_frame = Frame(sub_win, padx=5, pady=5)
    e_frame.pack()

    e = Entry(e_frame)
    e.pack()
    e.insert(0, now_url)

    sub_btn_frame = Frame(sub_win, padx=5, pady=5)
    sub_btn_frame.pack()

    def apply():
        global target_url
        global now_url

        links[select_link.get()] = e.get()
        now_url = links[select_link.get()]
        target_url = now_url
        path_label.config(text=now_url)

        msgbox.showinfo("Notice", "Link is changed Successfully")

        e.delete(0, END)
        e.insert(0, now_url)

    btn_apply = Button(sub_btn_frame, text="Apply", command=apply)
    btn_apply.pack(side="right", padx=5, pady=5)

    btn_done = Button(sub_btn_frame, text="done", command=sub_win.withdraw)
    btn_done.pack(side="right", padx=5, pady=5)

btn_open = Button(btn_frame, text="Open link", command=openlink)
btn_open.pack(side="left", padx=5, pady=5)

btn_change_link = Button(btn_frame, text="Change link ..", command=changelink)
btn_change_link.pack(side="right", padx=5, pady=5)

# Save and Exit button
s_btn_frame = Frame(root, padx=5, pady=10)
s_btn_frame.pack()

def save_exit():
    global save_path
    # Save
    with open(f"{save_path}/save.csv", 'w', newline='') as f:
        linkst = csv.writer(f)
        linkst.writerow(links)
    f.close()

    # Quit
    root.quit()

btn_save_link = Button(s_btn_frame, text="Save & Exit", command=save_exit)
btn_save_link.pack(side="right", padx=5, pady=5)

root.mainloop()