#Comando abaixo importa tudo da biblioteca que é necessária
#Para a criação de telas.(ASTERISCO significa tudo)
from tkinter import*

#i (instanciar) o objeto tk
i = Tk()

#Gerar título da janela
i.title('Programa financeiro')

#Propriedade que altera o tamanho da janela(980 X 720)
#e distância da direita e topo da tela
i.geometry('980x720+250+30')

#Propriedades gráficas, Cor de fundo da tela (bg) ou (background)
#Não pode passar o i com ponto! Deve ser i[]
i['bg'] = "yellow"

#Cria o ícone na janela, você deve ter a imagem no mesmo local
#do codígo.

#i.wm_iconbitmap('icone.icon')

#cria label e posiciona (place), e posiciona ele em relação a tela.

lbl = Label(i,text="Nome de usuário")
lbl.place(x=100, y=100)

#Cria um botão e posiciona o (place) ele em relação a label.

btn = Button(i,width='20',text='OK')

btn.place(x= 230,y= 100)

#Gera a janela gráfica

i.mainloop()