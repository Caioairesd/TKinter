from tkinter import*

i = Tk()
i.title("Programa financeiro")
i.geometry('1980x720+250+30')

lb1 = Label(i,text="LOGIN",bg="yellow")
#componente  .grid serve também para posicionar
#utilizando indicativo de row and columns
lb1.pack(anchor='w')

lb2 = Label(i,text="SENHA",bg="red")
lb2.grid(row=4,column=2)

ed1 = Entry(i)
ed1.grid(row=2,column=3)

ed2 = Entry(i)
ed2.grid(row=4,column=3)

bt1 = Button(i,text='Login')
bt1.pack(side=BOTH)

i.mainloop()