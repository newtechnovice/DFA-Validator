import tkinter as tk
from tkinter import *
import re
from PIL import Image,ImageTk

#Window
root = tk.Tk()
root.title("GROUP 3 - Automata Theory")
root.geometry('800x620')
root.resizable(width=FALSE, height=FALSE)
root.configure(bg='#4C4C6D') #343A40

#for CFG page
def nextPage():
    root.destroy()
    import cfg_page

#for Frame
frame1=Frame(root, width=1350, height=50, bd=16, relief="ridge", bg='#69698e')
frame1.pack(side=TOP)

Labelinfo= Label(frame1, font=('Arial', 26, 'bold'), fg='white',  text= "DFA VALIDATOR",
                  bg="#4C4C6D", bd=16).pack(side=TOP) #cyan3

Radiobut=Frame(root, width=650, height=300, bd=10, relief="ridge", bg="#F9F9F9")
Radiobut.pack(side=TOP)

Textb=Frame(root, width=650, height=300, bd=5, relief="raise",bg='#4C4C6D')
Textb.pack(side=TOP)

Ansbut= Frame(root, width=650, height=400, bd=5, relief="raise",bg='#4C4C6D')
Ansbut.pack(side=TOP)

Ans= Frame(root, width=650, height=400, bd=5, relief="flat",bg='#4C4C6D')
Ans.pack(side=TOP)


#RE pattern
validRE = '(aa|bb)'
invalidChars = set('cdefghijklmnopqrstuvwxyz1234567890-=[];/.,!@#$%^&*()_+')

validRE2 = '111|000|101|100|110'
invalidNums = set('23456789abcdefghijklmnopqrstuvwxyz-=[];/.,!@#$%^&*()_+')


#for Button
def checkRE():
    choice = var.get()
    result = RE.get(1.0, "end-1c")
    if choice == 1:
        if any((c in invalidChars) for c in result):
            output.config(text="INVALID.\nThis RE only accepts a or b as input.")

            im = Image.open(r"DFA1\1\1\aOrb.png")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif len(result) < 4:
            output.config(text="INVALID.\nStopped at _ node. Not an end state.")
            #first node
            if len(result) == 1 and result[0] == 'a': #a
                im = Image.open(r"DFA1\1\1\A.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 1 and result[0] == 'b': #b
                im = Image.open(r"DFA1\1\1\B.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 2 and (result[0] == 'a' and result[1] == 'b'): #ab
                im = Image.open(r"DFA1\1\1\Trap.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 2 and (result[0] == 'b' and result[1] == 'a'): #ba
                im = Image.open(r"DFA1\1\1\Trap.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 2:  # aa, bb
                im = Image.open(r"DFA1\1\1\AA.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 3 and (result[0] == 'a' and result[1] == 'b'): #abb
                im = Image.open(r"DFA1\1\1\Trap.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 3 and (result[0] == 'b' and result[1] == 'a'): #baa
                im = Image.open(r"DFA1\1\1\Trap.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 3:                  #up until the third node
                im = Image.open(r"DFA1\1\1\AAA.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test


        elif re.match(validRE,result):
            output.config(text="VALID")

            im = Image.open(r"DFA1\1\1\Valid .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test


        else:
            if len(result) > 1 and result[1] == 'a': #strings that exceeds 4 but invalid, baaabba
                output.config(text="INVALID.\nThe second letter is 'a'. This RE only accepts aa or bb at the beginning of the string.")

                #trap node
                im = Image.open(r"DFA1\1\1\Trap.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) > 1 and result[1] == 'b': #abbabba
                output.config(text="INVALID.\nThe second letter is 'b'. This RE only accepts aa or bb at the beginning of the string.")

                #trap
                im = Image.open(r"DFA1\1\1\Trap.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            else:
                output.config(text="INVALID")


    elif choice == 2:
        if any((c in invalidNums) for c in result):
            output.config(text="INVALID.\nThis RE only accepts 1 or 0 as input.")

            im = Image.open(r"DFA2\2\2\1Or2.png")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif re.match(validRE2, result):
            output.config(text="VALID")

            im = Image.open(r"DFA2\2\2\Valid .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif len(result) < 3:
            output.config(text="INVALID.\nStopped at _ node. Not an end state.")

            if len(result) == 1 and result[0] == '0': #0
                im = Image.open(r"DFA2\2\2\0.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 1 and result[0] == '1': #1
                im = Image.open(r"DFA2\2\2\1.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test


            elif len(result) == 2 and (result[0]=='1' and result[1]=='0'): #10
                im = Image.open(r"DFA2\2\2\11.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 2 and result[1] == '0': #00
                im = Image.open(r"DFA2\2\2\00.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 2 and (result[0]=='1' and result[1] == '1'): #11
                im = Image.open(r"DFA2\2\2\11.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 2 and (result[0]=='0' and result[1]=='1'): #01
                im = Image.open(r"DFA2\2\2\Trap .jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test

            elif len(result) == 2 and result[1] == '0': #00
                im = Image.open(r"DFA2\2\2\00.jpg")
                im = im.resize((387, 200), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(im)
                dfaDisplay = tk.Label(image=test)
                dfaDisplay.place(x=210, y=320)
                dfaDisplay.image = test



        elif len(result) == 3 and (result[2] == '1' and result[1] == '0' and result[0] == '0'):  # 001 <-- INVALID
            output.config(text="INVALID.\nThis RE only accepts 111,000,110,101,100 at the beginning.")

            im = Image.open(r"DFA2\2\2\Trap .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif len(result) == 3 and (result[2] == '1' and result[1] == '1' and result[0] == '1'):  # 111 <-- VALID
            output.config(text="VALID")

            im = Image.open(r"DFA2\2\2\Valid .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif len(result) == 3 and (result[2] == '0' and result[1] == '0' and result[0] == '0'):  # 000 <-- VALID
            output.config(text="VALID")

            im = Image.open(r"DFA2\2\2\Valid .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif len(result) == 3 and (result[2] == '0' and result[1] == '0' and result[0] == '1'):  # 100 <-- VALID
            output.config(text="VALID")

            im = Image.open(r"DFA2\2\2\Valid .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif len(result) == 3 and (result[2] == '1' and result[1] == '0' and result[0] == '1'):  # 101 <-- VALID
            output.config(text="VALID")

            im = Image.open(r"DFA2\2\2\Valid .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        elif len(result) == 3 and (result[2] == '0' and result[1] == '1' and result[0] == '1'):  # 110 <-- VALID
            output.config(text="VALID")

            im = Image.open(r"DFA2\2\2\Valid .jpg")
            im = im.resize((387, 200), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(im)
            dfaDisplay = tk.Label(image=test)
            dfaDisplay.place(x=210, y=320)
            dfaDisplay.image = test

        else:
            output.config(text="INVALID")

    else:
        output.config(text="INVALID SELECTION")



#Radio Button Options
var = IntVar()
option1 = Radiobutton(Radiobut,font=('Arial', 12, 'bold'), text="(aa+bb)(a+b)*(a+b+ab+ba)(a+b+ab+ba)*(aa+bab)*(a+b+aa)(a+b+bb+aa)*",
                      variable=var, value=1, background="#F9F9F9")
option1.grid(row=2, column=0)

option2 = Radiobutton(Radiobut, font=('Arial', 12, 'bold'), text="((101+(111)*+100)+(1+0+11)*)(1+0+01)*(111+000+101)(1+0)*",
                      variable=var, value=2, background="#F9F9F9")
option2.grid(row=4, column=0)

#Textbox Input
RE = tk.Text(Textb,font=('Arial', 12, 'italic'), height=2, width=20)
RE.grid(row=4, column=0)


#Button
btnCheck = tk.Button(Ansbut, font=('Arial', 10, 'bold'), text="Check", width=12, height=1, command=checkRE,
                     bg='#71719e', fg='white')
btnCheck.grid(row=5, column=0)

#Label Output
output = tk.Label(Ans,font=('Arial', 10, 'bold'), text="", bg="#4C4C6D", fg="white") #cyan3
output.grid(row=6, column=0)

#Menubar
menubar = Menu(root)

file = tk.Menu(menubar, tearoff=0)
file.add_command(label="RE")
file.add_separator()
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Regular Expressions", menu=file)

cfg = tk.Menu(menubar,tearoff=0)
cfg.add_command(label="CFG", command=nextPage)
menubar.add_cascade(label="Context-Free Grammar", menu=cfg)

root.config(menu=menubar)
root.mainloop()