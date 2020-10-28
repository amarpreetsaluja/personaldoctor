from tkinter import *
import random
import time
from tkinter.simpledialog import askstring
from tkinter import scrolledtext
import xlrd
b0=xlrd.open_workbook('b.xlsx')
a0=xlrd.open_workbook('a.xlsx')
c0=xlrd.open_workbook('c.xlsx')
b=b0.sheet_by_index(0)
a=a0.sheet_by_index(0)
c=c0.sheet_by_index(0)


def goto(line) :
    global lineNumber
    line = lineNumber
def diseaselist(sym):
     colno=0
     x0=[]
     for i in range(0,317):
          if(a.cell_value(0,i)==sym):
               colno=i
               break
     for i in range(1,66):
          if(a.cell_value(i, colno)==1):
               x0.append(a.cell_value(i,0))
     return(x0)

    
    
class App:

    def Encrypt1(self):
         global x
         symp1=self.contents1.get()
         symp1=symp1.lower()
         x=diseaselist(symp1)
         
         
         

    def Encrypt(self):
        
        global symp2
        global x
        symp2 = self.contents.get()             
        symp2 = symp2.lower()
        flag=0
        for i in range(0,317):
          if(a.cell_value(0,i)==symp2):
              flag=1
              break
        if(flag==1):
            y=diseaselist(symp2)
            x1=set(x)
            y1=set(y)
            f=x1.intersection(y)
            if(len(f)<=3):
                f=list(f)
                ctr=1
                for i in range(0,len(f)):
                    lbl=Label(root, text=f[i], font=("Arail", 10))
                    lbl.grid(column=0, row=10+i+ctr)
                    for j in range(0,18):
                        if(c.cell_value(j,0)==f[i]):
                            txt=scrolledtext.ScrolledText(root, width=40, height=10)
                            txt.grid(column=2, row=10+i+ctr)
                            txt.insert(INSERT, c.cell_value(j, 1))
                            break
                    ctr=ctr+1
                exit()
                      
                
            else:
                lbl=Label(root, text="Enter the next symptom.", font=("Arail", 10))
                lbl.grid(column=0, row=5)
                x=list(f)
        else:
            lbl=Label(root, text="Enter the next symptom.", font=("Arail", 10))
            lbl.grid(column=0, row=5)
            
        
            
    def __init__(self, master,x):
        frame = Frame(master)
        frame.grid()
        lbl=Label(frame, text="Welcome to your personal doctor.", font=("Arail Bold", 20))
        lbl.grid(column=0, row=0)
        lbl1=Label(frame, text="Enter your symptoms or click on the suggested symptoms.", font=("Arial", 10))
        lbl1.grid(column=0, row=1)
        lbl2=Label(frame, text="We will together predict the disease that you might have to treat you as soon as possible.", font=("Arial", 10))
        lbl2.grid(column=0, row=2)
        #create a button with the quit command, and tell it where to go
        quitbutton = Button(frame, text = "quit", fg ="red",                
                            command = root.quit, width = 10)
        quitbutton.grid(row = 0, column =10)

        #create an entry box, tell it where it goes, and how large it is
        entry1 = Entry(frame, width = 100)
        entry1.grid(column = 0, row=3)
 
        #set initial content of the entry box
        self.contents1 = StringVar()
        self.contents1.set("Enter the first symptom here")
        entry1["textvariable"] = self.contents1
 
        encrypt1 = Button(frame, text="Add this symptom", fg = "blue",
                         command = self.Encrypt1)
        encrypt1.grid(row =3, column =2)
   
 
        #create an entry box, tell it where it goes, and how large it is
        entry = Entry(frame, width = 100)
        entry.grid(column = 0, row=4)
 
        #set initial content of the entry box
        self.contents = StringVar()
        self.contents.set("Enter the next symptom here")
        entry["textvariable"] = self.contents
 
        encrypt = Button(frame, text="Add this symptom", fg = "blue",
                         command = self.Encrypt)
        encrypt.grid(row =4, column =2)
   
 
root = Tk()
root.title("Personal Doctor")
root.geometry('900x500')
flag=0
k=0
app = App(root,[])
root.mainloop()

