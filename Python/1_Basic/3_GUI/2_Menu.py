from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('MINEW GUI')
root.geometry('640x640+1800+300')
root.resizable(True, True)      # X, Y

# Menu Section
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)

def create_new_file():
    pass

# file menu
menu_file.add_command(label= "New File", command=create_new_file)
menu_file.add_command(label= "New Window")
menu_file.add_separator()
menu_file.add_command(label= "Open")
menu_file.add_command(label= "Save")
menu_file.add_separator()
menu_file.add_command(label= "Exit", command=root.quit())
menu.add_cascade(label="File", menu=menu_file)

# edit menu (Empty)
menu.add_cascade(label="Edit")

# PL menu (radio btn)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="P_Language", menu=menu_lang)

# View menu (check btn)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label = "Show minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)

# Button Section

def btncmd() :
    print("Clicked")
    change = txt.get("1.0", END)
    label.config(text=f'{change}')
    txt.delete("1.0", END)

# btn1 = Button(root, text='Button')
# btn1.pack()

# btn2 = Button(root, padx=10, pady=5, text='Button')
# btn2.pack()

# btn3 = Button(root, width=10, height=5, text='Button')
# btn3.pack()

btn4 = Button(root, fg='red', bg='green', text='Button', command=btncmd)
btn4.pack()

# Frame Section
frame = Frame(root, relief="solid", bd=1)   # border type / thickness
frame.pack(fill="x")

# btn5 = Button(frame, fg='red', bg='green', text='Button', command=btncmd)
# btn5.pack(side="right")

# btn6 = Button(frame, fg='red', bg='green', text='Button', command=btncmd)
# btn6.pack(side="left")

# Scrollbar Section
scr = Scrollbar(frame)
scr.pack(side="right", fill='y')

# Text Section
txt = Text(frame, width=30, height=10, yscrollcommand=scr.set)
txt.pack(fill="both")
scr.config(command=txt.yview)

# Label Section
label = Label(root, text="hello")       # fg : font-color       bg : background color
label.pack()

# Entry Section
e = Entry(root, width=30)
e.pack()
e.insert(0, "Plz write only a line")

# Listbox Section
listbox = Listbox(root, selectmode="single", height=0)
# listbox = Listbox(root, selectmode="extended|single", height=show_max // 0 = all)

listbox.insert(0, "Frozen")
listbox.insert(1, "Cinderella")
listbox.insert(2, "Maid")
listbox.insert(END, "BAB")
listbox.insert(END, "Aladin")
listbox.pack()

def lbbtncmd() :
    #listbox.delete(0) # delete first item
    #print("List have ", listbox.size(), " items") # Counting
    #print("first to 3rd items : ", listbox.get(0.2)) # item check
    print("selected items: ", listbox.curselection()) # Selected item check

lbbtn = Button(root, text="ListBtn", command=lbbtncmd)
lbbtn.pack()

# Checkbox Section
ch1 = IntVar()
chkbox1 = Checkbutton(root, text="Orange", variable=ch1)
chkbox1.select()    # checked default
chkbox1.pack()

ch2 = IntVar()
chkbox2 = Checkbutton(root, text="Melon", variable=ch2)
chkbox2.pack()

def cbbtncmd() :
    print(ch1.get())
    print(ch2.get())

cbbtn = Button(root, text="CheckBtn", command=cbbtncmd)
cbbtn.pack()

# Radiobutton Section
drink_var = IntVar()
drink1 = Radiobutton(root, text="Cola", value=1, variable=drink_var)
drink1.select()
drink2 = Radiobutton(root, text="Cider", value=2, variable=drink_var)

drink1.pack()
drink2.pack()

def rdbtncmd() :
    print(drink_var.get())

rdbtn = Button(root, text="RadioBtn", command=rdbtncmd)
rdbtn.pack()

# Combobox Section
month = [str(i) + "month" for i in range(1,13)]
cmbbox = ttk.Combobox(root, height=5, values=month, state="readonly")
cmbbox.pack()
cmbbox.set("MONTH")

def cmbbtncmd() :
    print(cmbbox.get())

cmbbtn = Button(root, text="ComboBtn", command=cmbbtncmd)
cmbbtn.pack()

root.mainloop()