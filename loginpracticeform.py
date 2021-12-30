from tkinter import *
root=Tk()
s=StringVar()
label1=Label(root,text="Enter Name:",font=("Arial",20))
label1.grid(row=0,column=0,sticky=W,pady=20)
entry1=Entry(root,font=("Arial",20))
entry1.grid(row=0,column=1,pady=20)
label2=Label(root,text="Enter Password:",font=("Arial",20))
label2.grid(row=1,column=0,sticky=W,pady=20)
entry2=Entry(root,show="*",font=("Arial",20))
entry2.grid(row=1,column=1,pady=20)
def show():
    s=entry1.get()
    print("Hello", s ," ur form has been selected")

button1=Button(root,text="Login",font=("Arial",15),command=show)
button1.grid(row=2,column=0,columnspan=2)
root.mainloop()