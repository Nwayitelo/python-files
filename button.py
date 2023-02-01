from tkinter import*
window = Tk()

text1= Label(window,text='username',bg='white',fg='black',padx=10,pady=10)
text1.grid(column=0,row=0)

text2= Label(window,text='password',bg='orange',fg='black',padx=10,pady=10)
text2.grid(column=0,row=1)

ent=Entry(window)
ent.grid(column=1,row=0)

ent2=Entry(window)
ent2.grid(column=1,row=1)

but =Button(window,text='Login',bg='pink',fg='black',padx=10,pady=10)
but.grid(column=1,row=2)

window.mainloop()
