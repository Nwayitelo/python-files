from tkinter import*

screen=Tk()
ent=Entry(screen,width=20,borderwidth=0)
te=Entry(screen,width=20,borderwidth=0)


telow=Label(screen,text="username")
telow.grid(column=0,row=1)
te.grid(column=1,row=1)

telow=Label(screen,text="password")
telow.grid(column=0,row=2)
ent.grid(column=1,row=2)

telow=Button(screen,text="LogIn")
telow.grid(column=1,row=3)










screen.mainloop()
