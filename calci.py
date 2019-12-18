from tkinter import *
val=""
def click(n):
    global val
    val=val+str(n)
    pr.set(val)
def fin(val):
    try:
        final=str(eval(val))
        pr.set(final)
        val=""
    except:
        val=""
        pr.set(val)
def cl():
    global val
    val=""
    pr.set("")
def backspace():
    global val
    try:
        l=list(val)
        x=len(l)
        l.pop(x-1)
        val=''.join(l)
        pr.set(val)
    except:
        pr.set("")
root=Tk()
root.title("Calci")
pr=StringVar()
Entry(root,textvariable=pr).grid(rowspan=2,columnspan=3)
b1=Button(root,text="7",command=lambda:click(7),width=4).grid(row=2,column=0)
b2=Button(root,text="8",command=lambda:click(8),width=4).grid(row=2,column=1)
b3=Button(root,text="9",command=lambda:click(9),width=4).grid(row=2,column=2)
b4=Button(root,text="4",command=lambda:click(4),width=4).grid(row=3,column=0)
b4=Button(root,text="5",command=lambda:click(5),width=4).grid(row=3,column=1)
b6=Button(root,text="6",command=lambda:click(6),width=4).grid(row=3,column=2)
b7=Button(root,text="1",command=lambda:click(1),width=4).grid(row=4,column=0)
b8=Button(root,text="2",command=lambda:click(2),width=4).grid(row=4,column=1)
b9=Button(root,text="3",command=lambda:click(3),width=4).grid(row=4,column=2)
b10=Button(root,text="0",command=lambda:click(0),width=4).grid(row=5,column=1)
b11=Button(root,text="%",command=lambda:click('%'),width=4).grid(row=2,column=3)
b12=Button(root,text="/",command=lambda:click('/'),width=4).grid(row=3,column=3)
b13=Button(root,text="+",command=lambda:click('+'),width=4).grid(row=4,column=3)
b14=Button(root,text="-",command=lambda:click('-'),width=4).grid(row=5,column=3)
b15=Button(root,text="=",command=lambda:fin(val),width=4).grid(row=5,column=2)
b16=Button(root,text="AC",command=cl,width=4).grid(row=5,column=0)
b17=Button(root,text="del",command=backspace,width=4).grid(row=0,column=3)
root.mainloop()
