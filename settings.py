from tkinter import *
from tkcalendar import Calendar
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyodbc


def __printar_banco_de_dados__():
    dados_de_conexao = (
        "Driver={SQLite3 ODBC Driver};"
        "Server=localhost;"
        "Database=Serviços.db"
    )

    conexao = pyodbc.connect(dados_de_conexao)
    cursor = conexao.cursor()

    for a in cursor.execute('''SELECT * FROM Clientes'''):
        print(a)




class JanelaDeRegistros:

    def __int__(self):
        # Janela de Registro
        janela_de_registro = Tk()
        janela_de_registro.title('Registro de Clientes')
        janela_de_registro.config(bg='#12152f')

        # Variables
        fonte = 'Arial 20'
        fonte_2 = 'Arial 15'
        texto = 'Registro de Clientes'

        cor1 = '#4288c4'
        cor2 = '#0f2039'
        cor3 = '#93e0d6'
        # Widgets
        self.frame_borda_titulo_de_registros = Frame(janela_de_registro, background=cor1, width=560, height=60,
                                                     relief='raised',
                                                     borderwidth=5)
        self.label_titulo_de_registros = Label(self.frame_borda_titulo_de_registros, text=texto, bg=cor3,
                                               borderwidth=4,
                                               font=fonte,
                                               fg=cor2,
                                               relief='sunken',
                                               width=44, height=0)

        self.label_nome = Label(janela_de_registro, text='Nome: ', font=fonte_2, bg=cor1, relief='solid')
        self.entry_nome = Entry(janela_de_registro, font=fonte_2, width=40, relief='solid', borderwidth=2)

        self.label_telefone = Label(janela_de_registro, text='Telefone: ', font=fonte_2, relief='solid', bg=cor1)
        self.entry_telefone = Entry(janela_de_registro, font=fonte_2, width=10, relief='solid', borderwidth=2)

        self.label_numero_do_envelope = Label(janela_de_registro, text='Envelope: ', font=fonte_2, relief='solid',
                                              bg=cor1)
        self.entry_numero_do_envelope = Entry(janela_de_registro, font=fonte_2, width=10, relief='solid', borderwidth=2)

        self.label_data_de_inicio = Label(janela_de_registro, text='Data de início', font=fonte_2, relief='solid',
                                          bg=cor1)
        self.calendar_inicio = Calendar(janela_de_registro, font='Arial 12', locale='pt_BR', date_pattern='d/m/yyyy')

        self.label_data_de_final = Label(janela_de_registro, text='Data de entrega', font=fonte_2, relief='solid',
                                         bg=cor1)

        self.calendar_final = Calendar(janela_de_registro, font='Arial 12', locale='pt_BR', date_pattern='d/m/yyyy')

        self.text_descricao = Text(janela_de_registro, font='Arial 13', height=4, relief='solid', borderwidth=2)

        self.label_valor_total = Label(janela_de_registro, text='Valor R$: ', font=fonte_2, relief='solid',
                                       bg=cor1)
        self.entry_valor_total = Entry(janela_de_registro, font=fonte_2, width=9, relief='solid', borderwidth=2,
                                       justify='center')

        self.label_valor_sinal = Label(janela_de_registro, text='Sinal R$: ', font=fonte_2, relief='solid',
                                       bg=cor1)
        self.entry_valor_sinal = Entry(janela_de_registro, font=fonte_2, width=9, relief='solid', borderwidth=2,
                                       justify='center', )

        self.label_valor_restante = Label(janela_de_registro, text='Restante R$: ', font=fonte_2, relief='solid',
                                          bg=cor1)
        self.button_valor_restante = Button(janela_de_registro, font=fonte_2, relief='solid', borderwidth=2,
                                            command=self.calcular_restante, text='Calcular')

        self.button_finalizar = Button(janela_de_registro, font=fonte_2, relief='solid', borderwidth=2,
                                       command=self.finalizar, text='Finalizar', bg=cor1, height=3)

        # Grid
        self.frame_borda_titulo_de_registros.grid(columnspan=4, column=0, row=0, padx=20, pady=5, sticky=EW)
        self.label_titulo_de_registros.grid(columnspan=4, column=0, row=0, padx=20, pady=10)

        self.label_nome.grid(column=0, row=1, pady=15, padx=25, sticky=EW, ipadx=2)
        self.entry_nome.grid(column=1, columnspan=4, row=1, pady=15, sticky=EW, padx=25)

        self.label_telefone.grid(column=0, row=2, pady=6, sticky=EW, padx=25)
        self.entry_telefone.grid(column=1, row=2, pady=15, padx=25, sticky=EW)

        self.label_numero_do_envelope.grid(column=2, row=2, pady=6, sticky=EW)
        self.entry_numero_do_envelope.grid(column=3, row=2, pady=15, sticky=EW, padx=25, ipadx=5)

        self.label_data_de_inicio.grid(row=3, column=0, columnspan=2, pady=6, sticky=EW, padx=25)
        self.calendar_inicio.grid(columnspan=2, column=0, row=4, pady=6, padx=25)

        self.label_data_de_final.grid(row=3, column=2, columnspan=2, pady=6, sticky=EW, padx=25)
        self.calendar_final.grid(columnspan=2, column=2, row=4, pady=6, padx=25)

        self.text_descricao.grid(column=0, row=5, columnspan=4, sticky=EW, padx=25, pady=6)

        self.label_valor_total.grid(column=0, row=6, sticky=EW, padx=25, pady=6)
        self.entry_valor_total.grid(column=0, row=7, sticky=EW, padx=25, pady=6)

        self.label_valor_sinal.grid(column=1, row=6, sticky=EW, padx=25, pady=6)
        self.entry_valor_sinal.grid(column=1, row=7, sticky=EW, padx=25, pady=6)

        self.label_valor_restante.grid(column=2, row=6, sticky=EW, padx=25, pady=6)
        self.button_valor_restante.grid(column=2, row=7, sticky=EW, padx=25, pady=6)

        self.button_finalizar.grid(column=3, row=6, rowspan=2, sticky=EW, padx=25, pady=6)

        # Menu
        menubar = Menu(janela_de_registro)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Printar banco de dados", command=__printar_banco_de_dados__)
        menubar.add_cascade(label="Help", menu=helpmenu)
        janela_de_registro.config(menu=menubar)

    def calcular_restante(self):
        valor_restante = float(self.entry_valor_total.get()) - float(self.entry_valor_sinal.get())
        self.button_valor_restante['text'] = f'{valor_restante}'

    def finalizar(self):
        dados_de_conexao = (
            "Driver={SQLite3 ODBC Driver};"
            "Server=localhost;"
            "Database=Serviços.db"
        )

        conexao = pyodbc.connect(dados_de_conexao)

        cursor = conexao.cursor()

        nome_do_cliente = self.entry_nome.get()
        telefone_do_cliente = self.entry_telefone.get()
        servico = self.text_descricao.get('1.0', 'end-1c')
        valor_total = self.entry_valor_total.get()
        valor_de_entrada = self.entry_valor_sinal.get()
        valor_restante = self.button_valor_restante['text']
        data_de_inicio = self.calendar_inicio.get_date()
        data_de_entrega = self.calendar_final.get_date()
        numero_do_envelope = self.entry_numero_do_envelope.get()

        # Adicionar no banco de dados
        cursor.execute(f"""INSERT Into Clientes(Nome, Telefone, TipoDoServiço, ValorTotal, ValorDeEntrada, 
        ValorRestante, DataDeInicio, DataDeEntrega, NumeroDoEnvelope) VALUES('{nome_do_cliente}', 
        '{telefone_do_cliente}', '{servico}', {valor_total}, {valor_de_entrada}, 
            {valor_restante}, '{data_de_inicio}', '{data_de_entrega}', {numero_do_envelope})""")
        cursor.commit()
        # Printar tudo
        cursor.execute("""SELECT * FROM Clientes""")

        dados = cursor.fetchall()

        for cliente in dados:
            print(f'{cliente}\n')

        # Fechar tudo
        cursor.close()
        conexao.close()
        # Limpar todas as entrys
        self.entry_nome.delete(0, END)
        self.entry_numero_do_envelope.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_valor_total.delete(0, END)
        self.entry_valor_sinal.delete(0, END)
        self.button_valor_restante['text'] = 'Calcular'
        self.text_descricao.delete('1.0', END)


class JanelaDeClientes:
    def __int__(self):
        self.janela_de_clientes = Tk()
        self.janela_de_clientes.title('Clientes')
        self.janela_de_clientes.config(background='#12152f')

        cor1 = '#4288c4'
        cor2 = '#0f2039'
        cor3 = '#93e0d6'
        fonte = 'Arial 20'

        # Widgets
        self.frame_titulo = Frame(self.janela_de_clientes, background=cor1, width=560, height=60, relief='raised',
                                  borderwidth=5)
        self.label_titulo_de_clientes = Label(self.frame_titulo, text='Clientes', bg=cor3, borderwidth=4, font=fonte,
                                              fg=cor2, relief='sunken', width=44, height=0)

        self.textbox_clientes = Text(self.janela_de_clientes, bg=cor3, borderwidth=4, font='Arial 12',
                                     fg=cor2, relief='sunken', width=80, height=10)

        # Grid dos widgets
        self.frame_titulo.grid(columnspan=4, row=0, column=0, padx=20, pady=10)
        self.label_titulo_de_clientes.grid(columnspan=4, row=0, column=0, padx=20, pady=10)

        self.textbox_clientes.grid(column=0, row=1, padx=20, pady=10)

        mainloop()

        def __pegar_tudo_da_tabela__():
            dados_de_conexao = (
                "Driver={SQLite3 ODBC Driver};"
                "Server=localhost;"
                "Database=Serviços.db"
            )

            conexao = pyodbc.connect(dados_de_conexao)
            cursor = conexao.cursor()

            for i in cursor.execute('''SELECT * FROM Clientes'''):
                self.textbox_clientes.insert('end', i)
                print(i)
class JanelaDeCotacoes:

    def __int__(self):
        # Janela de Registro
        self.janela_de_cotacao = Tk()
        self.janela_de_cotacao.title('Cotação de Metais')
        self.janela_de_cotacao.config(bg='#12152f')

        # Variables
        self.fonte = 'Arial 20'
        self.fonte_2 = 'Arial 15'
        self.titulo = 'Cotação de Metais'
        self.cor1 = '#4288c4'
        self.cor2 = '#0f2039'
        self.branco = '#93e0d6'

        self.frame_borda_titulo = Frame(self.janela_de_cotacao, background=self.cor1, height=60,
                                        relief='raised', borderwidth=5)
        self.label_titulo_de_registros = Label(self.frame_borda_titulo, text=self.titulo, bg=self.branco,
                                               borderwidth=4, font=self.fonte, fg=self.cor2, relief='sunken',
                                               width=22, height=0)
        self.button_pegar_cotacao = Button(self.janela_de_cotacao, text='Pegar cotações', font=self.fonte_2,
                                           relief='solid',
                                           bg=self.cor1, command=lambda: JanelaDeCotacoes.pegar_cotacao(self))

        self.label_aluminio = Label(self.janela_de_cotacao, text='Aluminío: ???', font=self.fonte_2, relief='solid',
                                    bg=self.branco)
        self.label_chumbo = Label(self.janela_de_cotacao, text='Chumbo: ???', font=self.fonte_2, relief='solid',
                                  bg=self.branco)
        self.label_cobre = Label(self.janela_de_cotacao, text='Cobre: ???', font=self.fonte_2, relief='solid',
                                 bg=self.branco)
        self.label_cobre_londres = Label(self.janela_de_cotacao, text='Cobre Londres: ???', font=self.fonte_2,
                                         relief='solid',
                                         bg=self.branco)
        self.label_estanho = Label(self.janela_de_cotacao, text='Estanho: ???', font=self.fonte_2, relief='solid',
                                   bg=self.branco)
        self.label_niquel = Label(self.janela_de_cotacao, text='Níquel: ???', font=self.fonte_2, relief='solid',
                                  bg=self.branco)
        self.label_ouro = Label(self.janela_de_cotacao, text='Ouro: ???', font=self.fonte_2, relief='solid',
                                bg=self.branco)
        self.label_paladio = Label(self.janela_de_cotacao, text='Paládio: ???', font=self.fonte_2, relief='solid',
                                   bg=self.branco)
        self.label_platina = Label(self.janela_de_cotacao, text='Platina: ???', font=self.fonte_2, relief='solid',
                                   bg=self.branco)
        self.label_prata = Label(self.janela_de_cotacao, text='Prata: ???', font=self.fonte_2, relief='solid',
                                 bg=self.branco)
        self.label_zinco = Label(self.janela_de_cotacao, text='Zinco: ???', font=self.fonte_2, relief='solid',
                                 bg=self.branco)

        # Grid
        self.frame_borda_titulo.grid(columnspan=4, column=0, row=0, padx=20, pady=5, sticky=EW)
        self.label_titulo_de_registros.grid(columnspan=4, column=0, row=0, padx=20, pady=10)

        self.button_pegar_cotacao.grid(column=0, row=7, pady=15, padx=25, sticky=EW, ipadx=2)

        self.label_aluminio.grid(column=0, row=1, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_chumbo.grid(column=1, row=1, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_cobre.grid(column=0, row=2, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_cobre_londres.grid(column=1, row=2, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_estanho.grid(column=0, row=3, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_niquel.grid(column=1, row=3, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_ouro.grid(column=0, row=4, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_paladio.grid(column=1, row=4, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_platina.grid(column=0, row=5, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_prata.grid(column=1, row=5, pady=15, padx=25, sticky=EW, ipadx=2)
        self.label_zinco.grid(column=0, row=6, pady=15, padx=25, sticky=EW, ipadx=2)

    def pegar_cotacao(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        # Abre o site do Google
        driver.get("https://br.investing.com/commodities/metals")

        # Encontra o elemento de pesquisa na página
        aluminio = driver.find_element(By.XPATH, '//*[@id="pair_49768"]/td[4]')
        chumbo = driver.find_element(By.XPATH, '//*[@id="pair_959207"]/td[4]')
        cobre = driver.find_element(By.XPATH, '//*[@id="pair_8831"]/td[4]')
        cobre_londres = driver.find_element(By.XPATH, '//*[@id="pair_959211"]/td[4]')
        estanho = driver.find_element(By.XPATH, '//*[@id="pair_959209"]/td[4]')
        niquel = driver.find_element(By.XPATH, '//*[@id="pair_959208"]/td[4]')
        ouro = driver.find_element(By.XPATH, '//*[@id="pair_8830"]/td[4]')
        paladio = driver.find_element(By.XPATH, '//*[@id="pair_8883"]/td[4]')
        platina = driver.find_element(By.XPATH, '//*[@id="pair_8910"]/td[4]')
        prata = driver.find_element(By.XPATH, '//*[@id="pair_8836"]/td[4]')
        zinco = driver.find_element(By.XPATH, '//*[@id="pair_956470"]/td[4]')

        valor_aluminio = aluminio.text
        valor_chumbo = chumbo.text
        valor_cobre = cobre.text
        valor_cobre_londres = cobre_londres.text
        valor_estanho = estanho.text
        valor_niquel = niquel.text
        valor_ouro = ouro.text
        valor_paladio = paladio.text
        valor_platina = platina.text
        valor_prata = prata.text
        valor_zinco = zinco.text

        self.label_titulo_de_registros.config(text='Cotação de Metais', width=25)
        self.label_aluminio.config(text=f'Alumínio: {valor_aluminio}', bg='lightgreen')
        self.label_chumbo.config(text=f'Chumbo: {valor_chumbo}', bg='lightgreen')
        self.label_cobre.config(text=f'Cobre: {valor_cobre}', bg='lightgreen')
        self.label_cobre_londres.config(text=f'Cobre Londres: {valor_cobre_londres}', bg='lightgreen')
        self.label_estanho.config(text=f'Estanho: {valor_estanho}', bg='lightgreen')
        self.label_niquel.config(text=f'Níquel: {valor_niquel}', bg='lightgreen')
        self.label_ouro.config(text=f'Ouro: {valor_ouro}', bg='lightgreen')
        self.label_paladio.config(text=f'Paládio: {valor_paladio}', bg='lightgreen')
        self.label_platina.config(text=f'Platina: {valor_platina}', bg='lightgreen')
        self.label_prata.config(text=f'Prata: {valor_prata}', bg='lightgreen')
        self.label_zinco.config(text=f'Zinco: {valor_zinco}', bg='lightgreen')
