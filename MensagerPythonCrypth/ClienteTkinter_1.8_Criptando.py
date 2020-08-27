from tkinter import*
from tkinter import messagebox
import socket
from threading import*
from datetime import date


        
class Application:
    def __init__(self, master= None):
        # Janel principal!
        self.principal = Frame(master)
        self.principal.pack(fill=BOTH, expand=1)
        self.principal['bg'] = 'Grey'
        

        # Container Nick
        self.nick_box = Frame(self.principal)
        self.nick_box.pack(side=TOP, ipadx=200)

        # Dentro do container Nick
        self.lbl_nick = Label(self.nick_box)
        self.lbl_nick['text'] = 'Nick: '
        self.lbl_nick.pack( side=LEFT)
        # Criando um Entry para entrada da variavel String para o nick
        nickVar = StringVar
        self.nickinput = Entry(self.nick_box, textvariable=nickVar)
        self.nickinput.pack(side=LEFT)
        self.nickinput.focus_force()
        self.textnick=self.nickinput.get()

        # Container Chave
        self.key_box = Frame(self.principal)
        self.key_box.pack(side=TOP, ipadx=200)
        # Criando label para Entry Chave
        self.lbl_key = Label(self.key_box, text='Chave de Decriptografia: ')
        self.lbl_key.pack(side = LEFT)
        # Criando Uma Entry para a entrada da chave para descriptar e encriptar
        keyVar = IntVar
        self.keyinput = Entry(self.key_box, textvariable=keyVar)
        self.keyinput.pack(side=LEFT)

        def getkey(event):
            try:
                self.keyint = int(self.keyinput.get())
            except ValueError:
                errorkey = messagebox.showerror('Error Key','Digite uma chave de Descriptografia!')
                if errorkey == 'OK':
                    self.keyinput.focus_force
            if self.keyint == None:
                errorkey = messagebox.showerror('Error Key','A chave nunca deve ser um texto, digite um numero válido!')
                if errorkey == 'OK':
                    self.keyinput.focus_force
            else:
                self.keyint = int(self.keyinput.get())
                self.keyinput.delete(0,END)
                self.caixa_mensagem.focus_force()
                # Thread para receber e mandar mensagens com varios clients
                recebe_mensagemThread = Thread(target=recebe_mensagem)
                recebe_mensagemThread.start()




        def change(event):
            # Capturando o NICK
            self.textnick=self.nickinput.get()

            # Destruindo a nick box para após recontruir um com uma label com o nick encluido
            self.nick_box.destroy()

            # Criando uma Frame para a nova label
            self.nick_box2 = Frame(self.principal)
            self.nick_box2.pack(before=self.key_box,ipadx=800)

            # Criando a Label com o cateudo da nick desejado
            self.lbl_nick = Label(self.nick_box2, text='NICK: {0}'.format(self.textnick) )
            self.lbl_nick.pack(side=LEFT)
            self.lbl_nick['font'] = 'Helvetica'
            self.keyinput.focus_force()
        
        def changebtn():
            # Capturando o NICK
            self.textnick=self.nickinput.get()

            # Destruindo a nick box para após recontruir um com uma label com o nick encluido
            self.nick_box.destroy()

            # Criando uma Frame para a nova label
            self.nick_box2 = Frame(self.principal)
            self.nick_box2.pack(before=self.conversa,ipadx=800)

            # Criando a Label com o cateudo da nick desejado
            self.lbl_nick = Label(self.nick_box2, text='NICK: {0}'.format(self.textnick) )
            self.lbl_nick.pack(side=LEFT)
            self.lbl_nick['font'] = 'Helvetica'
            self.caixa_mensagem.focus_force()

        self.btn_nick = Button(self.nick_box)
        self.btn_nick['text'] = 'Ok'
        self.btn_nick['command'] = changebtn
        self.btn_nick.pack(side=LEFT, padx=10)
        
        # FIM NICK

        # Container Conversa
        self.conversa = Frame(self.principal)
        self.conversa.pack(fill=BOTH,expand=1,ipadx=10,ipady=10,padx=20,pady=0)
        self.conversa['bg'] = 'blue'

        # Criando Visualizador da conversa
        self.lista_conversa = Listbox(self.conversa)
        self.lista_conversa.pack(fill=BOTH, expand=1)
        self.lista_conversa['font'] = 'Helvetica'

        #Socket De Conexão ++++++
        arq = open('ip.txt','r')
        ip = arq.read()
        host = ip
        port = 80
        addr = (host, port)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client_socket.connect(addr)

        def recebe_mensagem():
            while True:
                try:
                    mens = client_socket.recv(1024).decode()
                    checaNumero = '1234567890'
                    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáàãäâéèëêíìóôöòúüùÁÀÃÄÂÉÈËÊÍÌÓÖÔÒÚÜÙçÇ!?@#$%¨&*(){}"[]´`^~"/"\"|":;><,.'

                    b = mens

                    key = self.keyint
                    data = str(date.today())
                    nkey = data.replace('-',',')
                    nkey = tuple(nkey)
                    a = ''
                    contador = 0

                    #Esta parte do codigo descriptografa as letras da mensagem de acordo com a chave numerica

                    for i in range(0,len(b),1):
                        cif = ''
                        if b[i] == ' ':
                            a = a + ' '
                        if b[i] in alfabeto:
                            posi = alfabeto.find(b[i])
                            if (posi > len(alfabeto)):
                                 posi = posi - len(alfabeto)
                            elif (posi < 1):
                                posi = posi + len(alfabeto)
                            posikey = posi - key
                            cif = cif = alfabeto[(posikey)%len(alfabeto)]
                            a = a + cif
                    #Esta parte do codigo descriptografa os números da mensagem de acordo com a chave numerica baseada no dia, mes e ano

                        elif b[i] in checaNumero:
                            posi = checaNumero.find(b[i])
                            posikeyn = posi - (int(nkey[0]) + int(nkey[1]) + int(nkey[2]) + int(nkey[3]) + int(nkey[5]) + int(nkey[6]) + int(nkey[8]) + int(nkey[9]))
                            if (posikeyn > len(checaNumero)):
                                posikeyn - len(checaNumero)
                            elif (posikeyn < 1):
                                posikeyn + len(checaNumero)
                            cif = checaNumero[(posikeyn)%len(checaNumero)]
                            a = a + cif
            

                    self.lista_conversa.insert(END,a)
                    if not mens:
                        break

                except OSError:  
                    break

        # Container Caixa De texto
        self.caixa_texto = Frame(self.principal)
        self.caixa_texto.pack(side=BOTTOM,fill=BOTH,ipady=10,padx=10,pady=10)

        #Criando caixa de texto Entry
        msg = StringVar
        self.caixa_mensagem = Entry(self.caixa_texto, textvariable= msg)
        self.caixa_mensagem.pack(side=LEFT,fill=BOTH,expand=1)
        self.caixa_mensagem['font'] = 'Helvetica'


        def Enviar():
            
            mensagem = self.caixa_mensagem.get()
            nickmens = '{0}: {1}'.format(self.textnick,mensagem)
            client_socket.send(nickmens.encode())
            self.caixa_mensagem.delete(0, END)

        def Enter(event):
            
            checaNumero = '1234567890'
            alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáàãäâéèëêíìóôöòúüùÁÀÃÄÂÉÈËÊÍÌÓÖÔÒÚÜÙçÇ!?@#$%¨&*(){}"[]´`^~"/"\"|":;><,.'
            mensagem = self.caixa_mensagem.get()
            nickmens = '{0}: {1}'.format(self.textnick,mensagem)
            b = nickmens
            a = ''
            key = key = self.keyint 
            data = str(date.today())
            nkey = data.replace('-',',')
            nkey = tuple(nkey)

            posikey = 0

            for i in range(0,len(b),1):
                cif = ''
                cifn = ''
                posikey = 0
        
                if b[i] == ' ':
                    a = a + ' '
                if b[i] in alfabeto:
                    posi = alfabeto.find(b[i])
                    if (posi < 1):
                       posi = posi + len(alfabeto)
                    elif (posi > len(alfabeto)):
                        posi = posi - len(alfabeto)
            
                    posikey = posi + key   
                    if((posikey) < 1):
                        posikey = (posikey) + len(alfabeto)
                    elif (posikey) > len(alfabeto):
                        posikey = (posikey)%len(alfabeto)
                           
                    cif = alfabeto[(posikey)%len(alfabeto)]
                    a = a + cif
        
            #Esta parte do codigo criptografa os números da mensagem de acordo com a chave numerica baseada no dia, mes e ano
        
                elif b[i] in checaNumero:
                    posi = checaNumero.find(b[i])
                    if (posi < 1):
                        posi + len(checaNumero)
                    elif (posi > len(checaNumero)):
                        posi % len(checaNumero)
            
                    posikeyn = posi + (int(nkey[0]) + int(nkey[1]) + int(nkey[2]) + int(nkey[3]) + int(nkey[5]) + int(nkey[6]) + int(nkey[8]) + int(nkey[9]))

                    if((posikeyn) < 1):
                        posikeyn = (posikeyn) + len(checaNumero)
                    elif (posikeyn) > len(checaNumero):
                        posikey = (posikey)%len(checaNumero)
             
                    cifn = checaNumero[(posikeyn)%len(checaNumero)]
                    a = a + cifn
            print(a)
            mens = a
            client_socket.send(mens.encode())
            self.caixa_mensagem.delete(0, END)
        
        
        self.btn_enviar = Button(self.caixa_mensagem, text='Enviar', command=Enviar())
        self.btn_enviar.pack(side=RIGHT,fill=Y)
        self.caixa_mensagem.bind('<Return>', Enter)
        self.nickinput.bind('<Return>',change)
        self.keyinput.bind('<Return>',getkey)


        # FIM CAIXA DE TEXTO









root = Tk()
root.title('Sala de Conversa')
root.geometry('612x484')
Application(root)
root.mainloop()
