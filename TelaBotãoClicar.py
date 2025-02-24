from tkinter import*

#CRIANDO uma função para clique no botão

def btnClick():
    #O label que usa propriedade text
    #receberá a mensagem "trocou o texto"
    lbl["text"] = "trocou o texto"

    #Esse print abaixo exibe o texto na tela do console.
    print("O botão foi clicado!")

def btnClicar():
    #Esse prit exibe o texto digitad na caixa de texto e exibe na label da tela
    btn = Button(ed.get())
    lbl = Label["text"] = ed.get()

# i (instanciar) = recebe o objeto TK

i = Tk()
i.title("Programa financeiro")
i.geometry('1980x720+250+30')
i["bg"] = "green"

#i.wm_iconbitmap('icone.icon')
lbl = Label(i,text='Nome do usuário')
lbl.place(x=100,y=100)

btn = Button(i,width="20",text= 'Ok',command=btnClick)
btn.place(x=230,y=100)

#O codígo abaixo cria um botão que posiciona 
#abaixo do botão ok
btn = Button(i,width="20",text= 'Capturar',command=btnClicar)
btn.place(x=230,y=190)

#Cria a caixa de texto para digitar algo dentro
ed = Entry(i)
ed.place(x=230,y=150)

i.mainloop()