import pandas as pd
import re


file_path = "../../../../Downloads/PosicaoDistribuidor (1).txt"
xml_file = "../../../../Downloads/ArquivoCotistaContaOrdem_20210505_212222_Retorno.xml"
df = pd.read_csv(file_path, sep="\t")

position_date = 'DT_POSICAO'
quota_date = 'DT_COTA_FUNDO'
ditributer = 'DISTRIBUIDOR'
operator = 'OPERADOR'
code = 'CODIGO DO FUNDO'
fund = 'FUNDO'
client = 'CLIENTE' #	esse é o cotista vitreo
cpf = 'CPF/CGC'
quota_quantity = 'QUANTIDADE DE COTAS'
valor_bruto = 'VALOR BRUTO'
imposto_renda = 'I.R.'
iof = 'I.O.F.'
valor_liquido = 'VALOR LIQUIDO'
_patrim = '%PATRIMONIO'
sn_block = 'SN_BLOQUEIO'
rend_due_date = 'RENDIMENTO CARENCIA'
client_code = 'CODIGO DO CLIENTE' # esse é o cod fo cliente 


lista_tenho = [11342, 48691, 153198, 153198, 130077, 128096, 155088, 
149309, 144171, 159216, 112278, 2114, 91630]

#print(df.head()[client_code])
lista_quero = []
lista_tenho_quero = []
#print(df[client].head())
#print()
#print(df.head()[client].replace('VITREO ',''))


client_obj = {}
for i in range(len(df[client])):
  #print(df[client][i].replace('VITREO ', ''))
  for j in range(len(lista_tenho)):
    #print(str(lista_tenho[j]))
    if df[client][i].replace('VITREO ', '') == str(lista_tenho[j]):
      #print('{}   {}'.format(df[client_code][i], lista_tenho[j]))
      lista_quero.append(df[client_code][i])
      i_lista = []
      i_lista.append(df[client_code][i])
      i_lista.append(lista_tenho[j])
      lista_tenho_quero.append(i_lista)
      pass

print(lista_tenho_quero)


for i in range(len(lista_tenho_quero)):
  print(lista_tenho_quero[i])


df_xml = pd.read_csv(xml_file)
print(df_xml.head())