import tkinter as tk
from tkinter import *

#window
root = tk.Tk()
root.title("GROUP 3 - Automata Theory")
root.geometry('800x620')
root.resizable(width=FALSE, height=FALSE)
root.configure(bg='#4C4C6D') #343A40

#for main page
def prevPage():
    root.destroy()
    import main

#for Frame
frame2=Frame(root, width=1350, height=50, bd=16, relief="ridge", bg='#69698e')
frame2.pack(side=TOP)

Labelinfo2= Label(frame2, font=('Arial', 26, 'bold'), fg='white',  text= "CFG",
                  bg="#4C4C6D", bd=16).pack(side=TOP) #cyan3

Displaybut= Frame(root, width=650, height=400, bd=5, relief="raise",bg='#4C4C6D')
Displaybut.pack(side=TOP)

Displaybut1= Frame(root, width=650, height=400, bd=5, relief="raise",bg='#4C4C6D')
Displaybut1.pack(side=TOP)

Displaybut2= Frame(root, width=650, height=400, bd=5, relief="raise",bg='#4C4C6D')
Displaybut1.pack(side=TOP)

Anscfg= Frame(root, width=650, height=400, bd=5, relief="flat",bg='#4C4C6D')
Anscfg.pack(side=TOP)


def display(args):
    if args == 1:
        output1.config(text="S--> ABCDE \n\nA--> aa | bb \n\nB--> aB | bB | a | b | ab | ba\n\nC--> aC | bC | abC | baC | λ\n\nD--> aaD | babD | a | b | aa\n\nE--> aE | bE | λ")

    elif args == 2:
        output1.config(text="S--> ABCDE | BACDE\n\nA--> 101 | 111A | 100 | λ\n\nB-->  1B | 0B |  11B | λ\n\nC--> 1C | 0C | 01C | λ\n\nD--> 111 | 000 | 101\n\nE--> 1E | 0E | λ")


#Label Output CFG1
output1 = tk.Label(Anscfg,font=('Arial', 15, 'bold'), text="", bg="#4C4C6D", fg="white") #cyan3
output1.grid(row=6, column=0)

#Button
displaycfg1 = tk.Button(Displaybut, font=('Arial', 10, 'bold'), text="CFG1", width=12, height=1, bg='#71719e', fg='white', command=lambda:display(1))
displaycfg1.grid(row=5, column=0)

displaycfg2 = tk.Button(Displaybut1, font=('Arial', 10, 'bold'), text="CFG2", width=12, height=1, bg='#71719e', fg='white', command=lambda:display(2))
displaycfg2.grid(row=5, column=0)

#Menubar
menubar = Menu(root)

file = tk.Menu(menubar, tearoff=0)
file.add_command(label="Regular Expressions", command=prevPage)
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Regular Expressions", menu=file)

cfg = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Context-Free Grammar", menu=cfg)

root.config(menu=menubar)
root.mainloop()