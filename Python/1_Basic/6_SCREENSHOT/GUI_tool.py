from tkinter import *

root = Tk()
root.title("MINEW GUI")
root.geometry("640x480+2300+300")
root.resizable(TRUE, TRUE)

# Button Section
def btncmd():
    print("Clicked")
    change = txt.get("1.0", END)
    label.config(text= f"{change}")
    txt.delete("1.0", END)

# btn1 = Button(root, text="button 1")
# btn1.pack()

# btn2 = Button(root, padx=10, pady=5, text="button 2")      # padding: 5px 10px;
# btn2.pack()

# btn3 = Button(root, width=10, height=5, text="button 3")
# btn3.pack()

btn4 = Button(root, fg='red', bg='yellow', text="Active", command=btncmd)
btn4.pack()

# Frame Section
frame_txt = Frame(root, relief="solid", bd=1)
frame_txt.pack(fill="both")

# Scrollbar Section
scr = Scrollbar(frame_txt)
scr.pack(side="right", fill="y")

# Text Section
txt = Text(frame_txt, width=30, height=10, yscrollcommand=scr.set)          # 30 : percentage %
txt.pack(fill="both")
txt.insert(END, "Write Text")
scr.config(command=txt.yview)

# Label Section
label = Label(root, text="Hello")
label.pack()

root.mainloop()