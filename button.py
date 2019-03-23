

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
file1= open("int","w+")


root = Tk(  )

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    file1.write(name)
    file1.close()
Title = root.title( "File Opener")



c1 = Button(root, text="BROWSE",command=lambda : OpenFile()).grid(row=0,column=0)


root.mainloop()
