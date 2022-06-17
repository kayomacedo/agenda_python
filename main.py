from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from teste import agenda
from setuptools import Command
from bd  import inserir , consultar





root = Tk()
# Class funções
class Funcs():

    def salvar_dado(self):
        self.nome = str(self.entry_nome.get())
        self.telefone = str(self.entry_tel.get())

        # limpando

        self.entry_nome.delete(0,END)
        self.entry_tel.delete(0,END)




        if self.nome != "" and self.telefone != "":
       
            inserir( True,f'{self.nome}',f'{self.telefone}')

    def ver_dados(self):
        self.dados_conts = consultar(True)

    def tela2(self):
        self.ver_dados()
        self.root2 = Toplevel()
        

        

        self.root2.title("Ver Dados")
        #configurando BackGround

        self.root2.configure(background='#E0FFFF')

        self.root2.geometry("500x300")

        # Não responsivo 
        self.root2.resizable(False,False)
        self.lb_nomej2 =Label(self.root2, text = 'Lista de Contatos',bg = '#E0FFFF',font=(8))
        self.lb_nomej2.place(relx = 0.4 , rely = 0.03 )

        #TREEVIEWE 

        self.listaCli = ttk.Treeview(self.root2, height= 3 , columns=('col1','col2','col3'))
        
     
        self.listaCli.heading('#0',text='',)
        self.listaCli.heading('#1',text='ID',)
        self.listaCli.heading('#2',text='Nome',)
        self.listaCli.heading('#3',text='Telefone',)
       

        self.listaCli.column('#0',width = 1)
        self.listaCli.column('#1',width =20)
        self.listaCli.column('#2',width = 200)
        self.listaCli.column('#3',width = 200)

        self.listaCli.place(relx=0.03,rely= 0.1,relwidth= 0.95,relheight=0.8 )

        self.scrooll_lista = Scrollbar(self.root2, orient='vertical')
        self.listaCli.configure(yscroll = self.scrooll_lista.set)
        self.scrooll_lista.place(relx = 0.95,rely = 0.17,relheight=0.73, relwidth= 0.03 )

        # Preenchendo


        for contact in self.dados_conts:
            self.listaCli.insert('', END, values=contact)
            contact =''



       


    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get)

    



        


# Classe de aplicação
class Application(Funcs):


    # Inicialização com Main loop

    def __init__(self) -> None:
        # Equivalência para ele entender as configs 
        self.root = root
  
        self.tela()

        self.frames_da_tela()
    
        self.widgets_frame1()
        self.widgets_janela2()

        root.mainloop()

    def tela(self):
        self.root.title("Salvar no BD")
        #configurando BackGround

        self.root.configure(background='#E0FFFF')

        self.root.geometry("500x300")

        # Não responsivo 
        self.root.resizable(False,False)

    def frames_da_tela(self):
        self.frame1 = Frame(self.root,bd = 4, bg = 'white', 
                            highlightbackground= "#2F4F4F", highlightthickness = 3)
        self.frame1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.96,)




    

    def widgets_frame1(self):

        #================ CRIAÇÃO DE BOTÕES =================

        ##### Criação da Label Nome

        self.lb_nome = Label(self.frame1, text = 'Nome' , font=('verdana',15,'bold'),bg ='white', fg='blue')
        self.lb_nome.place(relx = 0.35 , rely = 0.2)

        self.entry_nome = Entry(self.frame1 )
        self.entry_nome.place(relx = 0.35 ,rely = 0.3)

         ##### Criação da Label Nome

        self.lb_tel = Label(self.frame1, text = 'Telefone' , font=('verdana',15,'bold'),bg ='white', fg='blue')
        self.lb_tel.place(relx = 0.35 , rely = 0.4)

        self.entry_tel = Entry(self.frame1 )
        self.entry_tel.place(relx = 0.35 ,rely = 0.5)
        
        
        
        ##### Criação do botão Salvar

        self.bt_salvar = Button (self.frame1, text= 'Salvar', bd = 2 , fg ='blue' , font =('verdana',9,'bold'),
                                command = self.salvar_dado)
        self.bt_salvar.place(relx = 0.45 , rely = 0.65,  relwidth= 0.15, relheight= 0.1 )

    

        ##### Botão Meus contatos (Nova Janela)

        self.bt_nova_janela = Button (self.frame1, text= 'Meus Contatos', fg ='blue',
                                    command= self.tela2 )
        self.bt_nova_janela.place(relx = 0.7 ,rely = 0.04)

    def widgets_janela2(self):
        pass









Application()