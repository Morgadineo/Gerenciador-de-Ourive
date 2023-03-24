from tkinter import *
from settings import JanelaDeRegistros, JanelaDeCotacoes, JanelaDeClientes

# Janela
largura, altura = '600', '600'
resolucao_da_janela = f'{altura}x{largura}'

janela_principal = Tk()
janela_principal.geometry(resolucao_da_janela)
janela_principal.config(background='#12152f')
janela_principal.title('Gerenciamento De Ourive')

janela_de_registros = JanelaDeRegistros()
janela_de_clientes = JanelaDeClientes()
janela_de_cotacao = JanelaDeCotacoes()

# Variaveis
fonte = 'Arial 20'
titulo = 'Gerenciamento do Ourive'

cor1 = '#4288c4'
cor2 = '#0f2039'
cor3 = '#93e0d6'

# Widgets
frame_borda_do_titulo = Frame(janela_principal, background=cor1, width=560, height=60, relief='raised',
                              borderwidth=5)

label_titulo = Label(janela_principal, text=titulo, bg=cor3, borderwidth=4, font=fonte, fg=cor2,
                     relief='sunken', width=33, height=0)

button_janela_de_registros = Button(janela_principal, text='Registrar Clientes', background=cor3, width=20,
                                    height=1, fg=cor2, font=fonte, relief='solid', borderwidth=2,
                                    command=janela_de_registros.__int__)

button_vizualizar_registros = Button(janela_principal, text='Clientes', background=cor3, width=20,
                                    height=1, fg=cor2, font=fonte, relief='solid', borderwidth=2,
                                    command=janela_de_clientes.__int__)

button_janela_de_cotacao = Button(janela_principal, text='Cotação de Metais', background=cor3, width=20,
                                   height=1, fg=cor2, font=fonte, relief='solid', borderwidth=2,
                                   command=janela_de_cotacao.__int__)

# Grid
frame_borda_do_titulo.grid(columnspan=2, column=0, row=0, padx=20, pady=5)

label_titulo.grid(columnspan=2, column=0, row=0, padx=20, pady=1)

button_janela_de_registros.grid(columnspan=2, column=0, row=2, padx=50, pady=50)
button_vizualizar_registros.grid(columnspan=2, column=0, row=3, padx=50, pady=50)
button_janela_de_cotacao.grid(columnspan=2, column=0, row=4, padx=50, pady=50)

# Mainloop
mainloop()
