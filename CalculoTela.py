from tkinter import*

def btClick():
    num1= int(ed1.get())
    num2= int(ed2.get())
    lb["text"] = num1 + num2

def btClickSubtracao():
    num1= int(ed1.get())
    num2= int(ed2.get())
    lb2["text"] = num1 - num2

def btClickMultipliacacao():
    num1= int(ed1.get())
    num2= int(ed2.get())
    lb3["text"] = num1 * num2

def btClickDivisao():
    num1= int(ed1.get())
    num2= int(ed2.get())
    lb4["text"] = num1 / num2
    


i = Tk()
i.title('Programa financeiro')
i.geometry('980x720+250+30')
i['bg'] = 'orange'

btsoma = Button(i,width='20',text="Soma",command=btClick)
btsoma.place(x=260,y=240)

lb = Label(i,text="0")
lb.place(x=450,y=240)


btsub = Button(i,width='20',text="Subtração",command=btClickSubtracao)
btsub.place(x=260,y=260)

lb2 = Label(i,text="0")
lb2.place(x=450,y=260)

btMulti = Button(i,width='20',text="Multiplicação",command=btClickMultipliacacao)
btMulti.place(x=260,y=280)

lb3 = Label(i,text="0")
lb3.place(x=450,y=280)

btDiv = Button(i,width='20',text="Divisão",command=btClickDivisao)
btDiv.place(x=260,y=300)

lb4 = Label(i,text="0")
lb4.place(x=450,y=300)

lbNome = Label(i,text="Caio Vinicius Aires da Silva")
lbNome.place(x=260,y=360)

ed1 = Entry(i)
ed1.place(x= 270,y= 200)

ed2 = Entry(i)
ed2.place(x= 270,y= 180)

i.mainloop()