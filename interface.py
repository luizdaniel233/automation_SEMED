#!/usr/bin/python3.6

import PySimpleGUI as sg

from  convert_csv import work_csv

all_data_filter = []

class interface:


    def select_row(option_filter):
        
        sg.change_look_and_feel('Reddit')
        #layout 
        layout = [  [sg.Text('Conteudo Lecionado:',size=(50,1), font='Arial',justification='left')],
                    [sg.Listbox(values=option_filter, select_mode='extended', key='selected',size=(50, 15))],
                    [sg.Button('confirm')],[sg.Button('Sair')],[sg.Button('Voltar')]
                    ]
        #janela
        return sg.Window("Selected Row",layout = layout,finalize=True)


    def main():
        periodo,ano,componente,turma = work_csv.o_csv(work_csv,"new_plan.csv")
        
        sg.change_look_and_feel('Reddit')
        #layout 
        layout = [  [sg.Text('Período Aluno:',size=(50,1), font='Arial',justification='left')],
                    [sg.Combo(periodo,key ='periodo')],
                    [sg.Text('Ano Aluno:',size=(50,1), font='Arial',justification='left')],
                    [sg.Combo(ano,key ='ano')],
                    [sg.Text('Turma Aluno:',size=(50,1), font='Arial',justification='left')],
                    [sg.Combo(turma,size=(20,1),key ='turma')],
                    [sg.Text('Componente Aluno:',size=(50,1), font='Arial',justification='left')],
                    [sg.Combo(componente,key ='componente')],
                    [sg.Text('Conteudo Lecionado:',size=(50,1), font='Arial',justification='left')],
                    [sg.Multiline(size=(30, 5), key='textbox')],
                    [sg.Button('check')],[sg.Button('Sair')],[sg.Button('Printar')]
                    ]
        #janela
        return sg.Window("Preenchimento",layout = layout,finalize=True)
    
    
    def plan():
        sg.change_look_and_feel('Reddit')
        #layout 
        layout = [[sg.Text("Choose a file: "), sg.FileBrowse()],
                  [sg.Button('Sair')],[sg.Button('OK')]]

        #janela
        return sg.Window("Selected Plan",layout = layout,finalize=True)
    
    def tela_main():
        sg.theme('Reddit')
        layout = [[sg.Button('Escolha a Planilha',size=(60,2))],
            [sg.Button('Preencher',size=(60,2))],
                    [sg.Button('Sair',size=(60,2))]]
        
        return sg.Window("Excel",layout = layout,finalize = True)


    janela1,janela2 = tela_main(),None

    while True:
        window,event,values = sg.read_all_windows()
        if window == janela1  and event == sg.WIN_CLOSED:
            break

        if window == janela1  and event == "Sair":
            break
        
        if window == janela2  and event == "Sair":
            break
            
        if window == janela1 and event == "Escolha a Planilha":
            janela2 = plan()
            janela1.hide()
        
        if window == janela1 and event == "Preencher":
            janela2 = main()
            janela1.hide()
            df = work_csv.o_excel(work_csv)
        
        if window == janela1 and event == 'Voltar':
            janela1.hide()
        
        if window == janela2 and event == 'Voltar':
            janela2.hide()
            janela1.un_hide()
        
        if window == janela2 and event == "OK":
            way_file = values['Browse']
            work_csv.__init__(work_csv,way_file)
            work_csv.c_csv(way_file,"new_plan.csv")
            janela2.hide()
            janela1.un_hide()
        
        if window == janela2 and event == 'Menu':     
            janela2.hide()
            janela1.un_hide()

        if window == janela2 and event == 'Printar':
            print(values)
            
        if window == janela2 and event == "check":
            if values['turma'] == '':
                sg.Popup('Turma Vazio!', keep_on_top=True)
            
            if values['textbox'] == '':
                sg.Popup('Conteudo Lecionado Vazio!', keep_on_top=True)
            else:
                #passar os dados por parametro,filtrados do csv
                data_windows = values
                
                option_filter,all_data_filter = work_csv.filter_csv(work_csv,values)
                #option_filter params
                if len(option_filter) == 0:
                    sg.Popup('Conteudo Não achado,dica procure palavras chaves,ou mude o componente!', keep_on_top=True)
                
                else:
                    janela1 = select_row(option_filter)
            #print(values) -> {'periodo': '3º BIMESTRE', 'ano': '1º ANO', 'componente': 'CIÊNCIAS', 'textbox': 'etre'}
        
        if window == janela1 and event == "confirm":
            #print(values) -> {'selected': ['Blanket']}
            v_selected = str(values['selected']).replace("[","").replace("]","")
            
            if v_selected == '':
                sg.Popup('Não marcou nenhum campo!,Tente "Voltar" ou "Sair"', keep_on_top=True)
            else:
                        
                for i in range(len(all_data_filter)):
                    str_v = str(all_data_filter[i])
                    if v_selected in str_v:
                        found = all_data_filter[i]
                #print(found,data_windows)
                #print({'data_all':found,"selected":v_selected,"data_st":option_filter})
                df = work_csv.register_csv(work_csv,found,data_windows,df)
                            
                janela1.hide()
                #preencher csv 

