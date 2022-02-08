import csv
import pandas as pd

class work_csv:
    
    def __init__ (self,file_path):
        self.file_path = file_path
        
    
    def save_csv(self,df):
        print(df)

    def register_csv(self,lista,dicionario,df):
        turma  = dicionario['turma']
        #if len(i) == 1 and dicionario['turma'] == i:
        #PERÍODO,ANO,COMPONENTE,HABILIDADE,CONTEÚDO
        '''['3º BIMESTRE', '1º ANO', 'LÍNGUA PORTUGUESA', '(EF12LP09) LER E COMPREENDER, EM COLABORAÇÃO COM OS COLEGAS E COM A AJUDA DO PROFESSOR, SLOGANS, ANÚNCIOS PUBLICITÁRIOS E TEXTOS DE CAMPANHAS DE CONSCIENTIZAÇÃO DESTINADOS AO PÚBLICO INFANTIL, DENTRE OUTROS GÊNEROS DO CAMPO PUBLICITÁRIO, CONSIDERANDO A SITUAÇÃO COMUNICATIVA E O TEMA/ASSUNTO DO TEXTO.', 'COMPREENSÃO EM LEITURA']
        {'periodo': '3º BIMESTRE', 'ano': '1º ANO', 'turma': 'A', 'componente': 'LÍNGUA PORTUGUESA', 'textbox': 'leitura'}'''
        #df = pd.read_excel(self.file_path,sheet_name='BASE_FUND I',header=1, engine='openpyxl')
        for i in range(len(df[turma])):
            #print(df[dicionario['turma']][i] , dicionario['turma'] , df['COMPONENTE'][i] , lista[2] , df['PERÍODO'][i] , lista[0] , df['HABILIDADE'][i] , lista[3] , df['ANO'][i] , lista[1] , df['CONTEÚDO'][i] , lista[4])
            if ((df['COMPONENTE'][i] == lista[2]) and (df['PERÍODO'][i] == lista[0] and df['HABILIDADE'][i] == lista[3]) and (df['ANO'][i] == lista[1] and df['CONTEÚDO'][i] == lista[4])):
                df[turma][i] = 1
                break
        
        '''with pd.ExcelWriter(self.file_path,mode='w',engine = 'openpyxl') as writer:  
            df.to_excel(writer, sheet_name='BASE_FUND I')'''
        
        return df
                    
    
    def filter_csv(self,values):
        print(values)
        options_filter = []
        all_data_filter = []
        
        periodo = values['periodo']
        ano = values['ano']
        componente = values['componente']
        conteudo = str(values['textbox']).upper()
        
        #f_csv = self.o_csv2(self,"new_plan.csv")
        with open('new_plan.csv', newline='',encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                s_row = str(row)
                if ((periodo in s_row and ano in s_row) and (componente in s_row and conteudo in s_row)):
                    all_data_filter.append(row[0:5])
                    options_filter.append(row[4])
                    
        
        return options_filter,all_data_filter                    
                
    
    def o_excel(self):
        df = pd.read_excel(self.file_path,sheet_name='BASE_FUND I',header=1, engine='openpyxl')
        return df
            

    def c_csv(file_path,want_name):
        
        #name_plan = "3º_4º BIMESTRE_NOVA_FERRAMENTA 1º AO 5º _CURRICULO_ AUTOMATIZADA_29.10.21_FINAL (CORRIGIDA) (1).xlsx"
        df = pd.read_excel(file_path,sheet_name='BASE_FUND I',header=1, engine='openpyxl')
        df.to_csv(f"C:/Users/luiz.santos/Desktop/automation_SEMED/{want_name}",index = None,header = True)

    def o_csv2(self,name):
        
        #self.c_csv("3º_4º BIMESTRE_NOVA_FERRAMENTA 1º AO 5º _CURRICULO_ AUTOMATIZADA_29.10.21_FINAL (CORRIGIDA) (1).xlsx",name)
        
        df2 = pd.read_csv(f"C:/Users/luiz.santos/Desktop/automation_SEMED/{name}",sep=',', index_col=0)
        df2 = df2.reset_index()
        df2 = df2.sample(frac=1) #shuffle rows from DF2
        return df2

    def o_csv(self,name):
    
        #self.c_csv("3º_4º BIMESTRE_NOVA_FERRAMENTA 1º AO 5º _CURRICULO_ AUTOMATIZADA_29.10.21_FINAL (CORRIGIDA) (1).xlsx",name)
        
        df2 = pd.read_csv(f"C:/Users/luiz.santos/Desktop/automation_SEMED/{name}",sep=',', index_col=0)
        df2 = df2.reset_index()
        df2 = df2.sample(frac=1) #shuffle rows from DF2

        periodo = []
        ano = []
        componente = []
        turma = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z']
        

        cols = df2[["PERÍODO","ANO","COMPONENTE"]]

        for ind in cols.index:
            
            periodo.append(str(cols.at[ind,"PERÍODO"]))
            ano.append(str(cols.at[ind,"ANO"]))
            componente.append(str(cols.at[ind,"COMPONENTE"]))
            

        #removendo duplicados
        periodo = self.r_csv(periodo)
        ano = self.r_csv(ano)
        componente = self.r_csv(componente)
        #dados para o select no pysimplegui
        return periodo,ano,componente,turma
            
    
    def r_csv(lista):
        l = []
        for i in lista:
            if i not in l and i != "nan":
                l.append(i)
        l.sort()
        return l
    


'''for i in f_csv:
        for x in f_csv[i]:'''

    
    
       