from tkinter import*

i = Tk()
i.title("Programa financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1',bg ='yellow')
lb1.place(x = 230,y = 200)

lb2 = Label(i,text='Label 2',bg ='pink')
lb2.place(x  = 230,y = 200)

lb3 = Label(i,text='Label 3',bg ='green')
lb3.place(x = 230,y = 200)

lb4 = Label(i,text='Label 4',bg ='red')
lb4.place(x = 230,y = 200)

"""lb1.pack(side=TOP,fill=X) #Comando fill é responsável
#do preenchimento 100%, deve usar X para horizontal e
#deve ser maiusculo

lb2.pack(side=LEFT,fill=Y) #Comando fill é responsável
#do preenchimento 100%, deve usar Y para vertical e
#deve ser maiusculo

lb3.pack(side=RIGHT,fill=Y) #Comando fill é responsável
#do preenchimento 100%, deve usar Y para vertical e
#deve ser maiusculo


lb4.pack(side=BOTTOM,fill=X) #Comando fill é responsável
#do preenchimento 100%, deve usar X para horizontal e
#deve ser maiusculo"""

lb1.pack(side=TOP,fill=BOTH,expand=10)
lb2.pack(side=TOP,fill=BOTH,expand=20)
lb3.pack(side=TOP,fill=BOTH,expand=30)
lb4.pack(side=TOP,fill=BOTH,expand=40)

i.mainloop()