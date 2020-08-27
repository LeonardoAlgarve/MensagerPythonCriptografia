from tkinter import *
import os


class Application:
    def __init__(self, master=None):
        root.geometry('640x480')
        self.img = PhotoImage(file = 'logo2.png')
        self.panel = Label(root, image = self.img)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        self.fonte = ('Arial','14')
        self.container1 = Frame(self.panel)
        self.container1['pady'] = 10
        self.container1.pack()

        self.container2 = Frame(self.panel)
        self.container2['padx'] = 20
        self.container2.pack()

        self.container3 = Frame(self.panel)
        self.container3['padx'] = 20
        self.container3.pack()

        self.container4 = Frame(self.panel)
        self.container4['padx'] = 20
        self.container4.pack()

        self.container5 = Frame(self.panel)
        self.container5['pady'] = 10
        self.container5.pack()
            
        self.titulo = Label(self.container1, text = 'Usuário, insira seus dados para acessar')
        self.titulo['font'] = ('Arial','14','bold')
        self.titulo.pack()

        self.identLabel = Label(self.container2,text = 'Identificação', font = self.fonte)
        self.identLabel.pack(side = LEFT)
        self.identLabel['padx'] = 22

        self.ident = Entry(self.container2)
        self.ident['width'] = 30
        self.ident['font'] = self.fonte
        self.ident.pack(side = LEFT)

        self.senhaLabel = Label(self.container3, text = 'Senha de Acesso', font = self.fonte)
        self.senhaLabel.pack(side = LEFT)

        self.senha = Entry(self.container3)
        self.senha['width'] = 30
        self.senha['font'] = self.fonte
        self.senha['show'] = '*'
        self.senha.pack(side = LEFT)

        self.iplabel = Label(self.container4, text = 'IP do servidor', font = self.fonte )
        self.iplabel['padx'] = 17
        self.iplabel.pack(side = LEFT)
        
        self.ip = Entry(self.container4)
        self.ip['width'] = 30
        self.ip['font'] = self.fonte
        self.ip.pack(side = LEFT)

        self.autenticar = Button(self.container5)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Arial','12')
        self.autenticar['width'] = 15
        self.autenticar['command'] = self.verificarSenha
        self.autenticar.pack()

        self.mensagem = Label(self.container5, text = '', font = self.fonte)
        
            
    def verificarSenha(self):
        self.mensagem.pack()   
        usuario = self.ident.get()
        senha = self.senha.get()
        ip = self.ip.get()                
        if ((usuario == 'Inspetor') and (senha == '12345') or ((usuario == 'Agente') and (senha == '67890'))):
        
            arq = open('ip.txt','w')
            arq.write(ip)  
            arq.close()  
            self.mensagem['text'] = 'Autenticado'
            #ATENÇÃO: TROCAR CAMINHO DO METODO STARTFILE DEPENDENDO DA MÁQUINA
            os.startfile('C:\\Users\\Familia\\Documents\\APS - Grupo 8\\ClienteTkinter_1.8_Criptando.py')
            root.destroy()     
        else:
            self.mensagem['text'] = 'Erro na autenticação'
            self.autenticar['text'] = 'Reiniciar'
            self.autenticar['command'] = self.reiniciar
    
    def reiniciar(self):
        # ATENÇÃO: TROCAR CAMINHO DO METODO STARTFILE DEPENDENDO DA MÁQUINA
        os.startfile('C:\\Users\\Familia\\Documents\\APS - Grupo 8\\Login.py')
        root.destroy()
          
                    
             
            
root = Tk()
Application(root)
root.mainloop()
