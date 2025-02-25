from tkinter import*

i = Tk()
i.title("Programa financeiro")
i.geometry('1980x720+250+30')

lb1 = Label(i,text="LOGIN",bg="yellow")
#componente  .grid serve também para posicionar
#utilizando indicativo de row and columns
lb1.place(x=1490,y=140)

lb2 = Label(i,text="SENHA",bg="red")
lb2.place(x=1490,y=220)

ed1 = Entry(i)
ed1.place(x=1450,y=200)

ed2 = Entry(i)
ed2.place(x=1450,y=120)

bt1 = Button(i,text='Login')
bt1.place(x=990,y=600)

i.mainloop()