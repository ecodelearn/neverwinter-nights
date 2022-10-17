from tkinter import *

janela_principal = Tk()

# define titulo
janela_principal.title("Título")
largura = 800
altura = 500

# resolução do nosso sistema
largura_monitor = janela_principal.winfo_screenwidth()
altura_monitor = janela_principal.winfo_screenheight()

# Posição da janela
posx = largura_monitor/2 - largura/2
posy = altura_monitor/2 - altura/2

print(largura_monitor, altura_monitor)

# define tamanho inicial
janela_principal.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# define backgrund color
janela_principal['bg'] = "lightblue"

def cmd_Click():
  print("py pocao.py")

# cria botão
cmd = Button(janela_principal, text = "Executar",
            fg="#000000",
            bg="#ffaaaa",
            command=lambda: cmd_Click())

#cria um label de texto
label_1 = Label(janela_principal,
                text="Este é o Label text=texto",
                font="Verdana 12 bold",
                fg="#ff9900")

#mostra o Label
label_1.pack()

# mostra botão
cmd.pack()


# mantem em execução a aplicação
janela_principal.mainloop()

