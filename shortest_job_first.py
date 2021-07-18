# ----------------------------- First come first served -------------------------------------------

# usar uma classe defirnir processo pronto
# pid será o identificador para acessar as informações do processo
from tkinter import *
from tkinter import ttk
from time import sleep

janela = Tk()

class processo_pronto:
    def __init__(self, pid, carga, chegada):
        self.pid = pid
        self.carga = carga
        self.chegada = chegada


#adicionar valores específicados 
processo_1 = processo_pronto(1001 ,18 ,0)
processo_2 = processo_pronto(1102 ,4  ,0)
processo_3 = processo_pronto(1003 ,22 ,0)
processo_4 = processo_pronto(1014 ,3  ,3)
processo_5 = processo_pronto(1061 ,8  ,3)
processo_6 = processo_pronto(1002 ,7  ,15)
processo_7 = processo_pronto(1203 ,2  ,15)
processo_8 = processo_pronto(1304 ,13 ,15)


#lista de processos
lista = []
lista.append(processo_1)
lista.append(processo_2)
lista.append(processo_3)
lista.append(processo_4)
lista.append(processo_5)
lista.append(processo_6)
lista.append(processo_7)
lista.append(processo_8)

#tabela de processos prontos
tabela_processos_prontos = ttk.Treeview(janela, selectmode='browse', columns=('column1', 'column2', 'column3'), show ='headings')

tabela_processos_prontos.column('column1', width=100, minwidth=50, stretch=True)
tabela_processos_prontos.heading('#1', text='PID')

tabela_processos_prontos.column('column1', width=30, minwidth=8, stretch=True)
tabela_processos_prontos.heading('#2', text='Carga')

tabela_processos_prontos.column('column1', width=30, minwidth=8, stretch=True)
tabela_processos_prontos.heading('#3', text='Chegada')

tabela_processos_prontos.grid(row=0, column=0)

for i in lista:
    elemento = [i.pid, i.carga, i.chegada]
    tabela_processos_prontos.insert('', END, values=elemento, tag='1')

#lista de itens da tabela para minupular a tabela
lista_tabela_prontos = tabela_processos_prontos.get_children()

#tabela de processos executados
tabela_processos_executados = ttk.Treeview(janela, selectmode='browse', columns=('column1'), show='headings')
tabela_processos_executados.column('column1', width=100, minwidth=8, stretch=True)
tabela_processos_executados.heading('#1', text='Processos Executados')

tabela_processos_executados. grid(row=0, column=0)
tabela_processos_executados.place(x=650, y=0)

#processo executando
titulo_processo_executando = Label(janela, text='Processo Executando', font="Arial 12")
titulo_processo_executando.place(x=460,y=0)

processo_executando = Label(janela, text='', font="Arial 12")
processo_executando.place(x=520,y=30)

#RESULTADOS
#transições
titulo_transicoes = Label(janela, text='Transições:', font="Arial 12")
titulo_transicoes.place(x=0,y=400)

transicoes = Label(janela, text='', font="Arial 12")
transicoes.place(x=80,y=400)

#carga executada
titulo_carga_executada = Label(janela, text='Carga Executada:', font="Arial 12")
titulo_carga_executada.place(x=0,y=430)

carga_executada = Label(janela, text='', font="Arial 12")
carga_executada.place(x=120,y=430)

#Total
titulo_total = Label(janela, text='Total:', font="Arial 12")
titulo_total.place(x=0,y=460)

total = Label(janela, text='', font="Arial 12")
total.place(x=60,y=460)

#Vazão
titulo_vazao = Label(janela, text='Vazão:', font="Arial 12")
titulo_vazao.place(x=0,y=490)

vazao = Label(janela, text='', font="Arial 12")
vazao.place(x=60,y=490)

#Uso da CPU
titulo_uso_cpu = Label(janela, text='Uso da CPU:', font="Arial 12")
titulo_uso_cpu.place(x=0,y=520)

uso_cpu = Label(janela, text='', font="Arial 12")
uso_cpu.place(x=100,y=520)

#Tempo de resposta
titulo_tempo_resposta = Label(janela, text='Tempo de resposta:', font="Arial 12")
titulo_tempo_resposta.place(x=0,y=550)

tempo_resposta = Label(janela, text='', font="Arial 12")
tempo_resposta.place(x=135,y=550)

#função que executa a fila de processos
# percorre a lista de processos pronts
# transição: aumanta em 1 a cada processo movido
# a carga executada: aumenta de acordo com a carga que está sendo executada na vez
# o total: soma da carga com a s transições
# vazão: quandidade de processo / tempo
# a % do uso da CPU é dado pela: quantidade de processo Filizadaos - quanditade de transições / Tempo * 100
# tempo de resposta: Tempo / quantidade de processos
#antes de iniciar ele orderna todos os processos baseado na carga em ordem crescente

def first_come_first_served():
    for i in lista_tabela_prontos:
        tabela_processos_prontos.delete(i)
#ordena lista
    for i in range(int(len(lista))):
        for j in range(int(len(lista))+1):
            if j >= len(lista):
                j = j - 1
            if lista[i].carga < lista[j].carga:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    for k in range(len(lista)):
        elemento = [lista[k].pid, lista[k].carga, lista[k].chegada]
        tabela_processos_prontos.insert('', END, values=elemento, tag='1')

        
#        print(str(elemento)+'\n')
        

#    tabela_processos_prontos.delete(tabela_processos_prontos.get_children('I009'))

    
    v_contador_transicao = 0
    v_total_carga = 0
    v_vazao = 0
    v_total_tempo_execucao = 0 
    v_uso_cpu = 0
    v_tempo_resposta = 0

     

    for linha in tabela_processos_prontos.get_children():
        print('loop')
        count = 0
        for value in tabela_processos_prontos.item(linha)['values']:
            if count == 0:
                v_item_pid = int(value)
            if count == 1:
                v_item_carga = int(value)
            if count == 2:
                v_item_chegada = int(value)
            count = count + 1

#        print(str(v_item_pid))
#        print(' ')
#        print(str(v_item_carga)) 
#        print('\n')


#        sleep(0.1)
        v_contador_transicao   = v_contador_transicao + 1
        v_total_carga          = v_total_carga + v_item_carga
        v_total_tempo_execucao = v_contador_transicao + v_total_carga 
        v_vazao                =  v_contador_transicao / (v_contador_transicao + v_total_carga)
        v_uso_cpu              = ((v_total_tempo_execucao - v_contador_transicao)/v_total_tempo_execucao)*100
        v_tempo_resposta       = v_total_tempo_execucao / v_contador_transicao

        tabela_processos_prontos.delete(linha)
#        print(str(tabela_processos_prontos.get_children()))
#
        processo_executando['text'] = str(v_item_pid)
        carga_executada['text']     = str(v_total_carga)
        transicoes['text']          = str(int(v_contador_transicao-1))
        total['text']               = str(v_total_tempo_execucao)
        vazao['text']               = str(float(v_vazao))
        uso_cpu['text']             = str(float(v_uso_cpu))
        tempo_resposta['text']      = str(float(v_tempo_resposta))
        
        tabela_processos_executados.insert('', END, values=v_item_pid, tag='1')

    processo_executando['text']= ''
            






botao = Button(janela, width=50, text='botao', command=first_come_first_served, background='green')
botao.place(x=300,y=550)

#executando janela
janela.geometry('800x600+0+0')
janela.mainloop()


