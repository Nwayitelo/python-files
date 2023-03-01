from tkinter import *

calc=Tk()
calc.title("nwayitelos's Calculator")
op=""

def click(num):
    global op
    op=op+str(num)
    iptext.set(op)

def equal():
    global op
    output=str(eval(op))
    iptext.set(output)

def clearbtn():
    global op
    op=""
    iptext.set(op)



iptext=StringVar()
iparea=Entry(calc,font=('large,_font',15,'bold'),bd=10,justify="right",insertwidth=4,textvariable=iptext).grid(columnspan=10)

bt7=Button(calc,font=('arial',15,'bold'),command=lambda:click(7),bg="pink",text="7",bd=5,padx=15,pady=10).grid(row=1,column=0)

bt8=Button(calc,font=('arial',15,'bold'),command=lambda:click(8),bg="pink",text="8",bd=5,padx=15,pady=10).grid(row=1,column=1)

bt9=Button(calc,font=('arial',15,'bold'),command=lambda:click(9),bg="pink",text="9",bd=5,padx=15,pady=10).grid(row=1,column=2)

add=Button(calc,font=('arial',15,'bold'),command=lambda:click('+'),bg="pink",text="+",bd=5,padx=15,pady=10).grid(row=1,column=3)

bt4=Button(calc,font=('arial',15,'bold'),command=lambda:click(4),bg="pink",text="4",bd=5,padx=15,pady=10).grid(row=2,column=0)

bt5=Button(calc,font=('arial',15,'bold'),command=lambda:click(5),bg="pink",text="5",bd=5,padx=15,pady=10).grid(row=2,column=1)

bt6=Button(calc,font=('arial',15,'bold'),command=lambda:click(6),bg="pink",text="6",bd=5,padx=15,pady=10).grid(row=2,column=2)

sub=Button(calc,font=('arial',15,'bold'),command=lambda:click('-'),bg="pink",text="-",bd=5,padx=15,pady=10).grid(row=2,column=3)

bt1=Button(calc,font=('arial',15,'bold'),command=lambda:click(1),bg="pink",text="1",bd=5,padx=15,pady=10).grid(row=3,column=0)

bt2=Button(calc,font=('arial',15,'bold'),command=lambda:click(2),bg="pink",text="2",bd=5,padx=15,pady=10).grid(row=3,column=1)

bt3=Button(calc,font=('arial',15,'bold'),command=lambda:click(3),bg="pink",text="3",bd=5,padx=15,pady=10).grid(row=3,column=2)

mul=Button(calc,font=('arial',15,'bold'),command=lambda:click('*'),bg="pink",text="*",bd=5,padx=15,pady=10).grid(row=3,column=3)

bt0=Button(calc,font=('arial',15,'bold'),command=lambda:click(0),bg="pink",text="0",bd=5,padx=15,pady=10).grid(row=4,column=0)

btC=Button(calc,font=('arial',15,'bold'),command=clearbtn,bg="pink",text="C",bd=5,padx=15,pady=10).grid(row=4,column=1)

eql=Button(calc,font=('arial',15,'bold'),command=equal,bg="pink",text="=",bd=5,padx=15,pady=10).grid(row=4,column=2)

div=Button(calc,font=('arial',15,'bold'),command=lambda:click('/'),bg="pink",text="/",bd=5,padx=15,pady=10).grid(row=4,column=3)

calc.mainloop(),
