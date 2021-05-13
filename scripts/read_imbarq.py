import os
import sys 
import numpy as np
import pandas as pd
#sys.path.append('.')
from funcoes import *


# C:\Users\ForpusCapital\Box\FORPUS\Operacional\Trading\Boletagem\2021\04-2021\15.04.2021

# main_path = "C:\\Users\\ForpusCapital\\Box\\FORPUS\\Operacional\\Trading\\Boletagem\\" # for jupyter
# C:\Users\ForpusCapital\Projects\autom_ops\automa_trabalho\scripts
# main_path = "C:\\Users\\ForpusCapital\\Box\\FORPUS\\Operacional\\Trading\\Boletagem\\"

#main_path = "C:/Users/ForpusCapital/Box/FORPUS/Operacional/Trading/Boletagem/"
main_path = "../../../../../ForpusCapital/Box/FORPUS/Operacional/Trading/Boletagem/"
ano = "2021/"
mes = "04-2021/"
#dia = "15.04.2021/"
#arquivo = "IMBARQ001_BV000272202104150000039004804033405.txt"
#dia = "16.04.2021/"
#arquivo = "IMBARQ001_BV000272202104160000039004804043912.txt"
#dia = "19-04-2021/"
#arquivo = "IMBARQ001_BV000272202104190000039004804033339.txt"
dia = "20-04-2021/"
arquivo = "IMBARQ001_BV000272202104200000039004804070759.txt"


file_path = main_path+ano+mes+dia+arquivo
"""
print(file_path)
#print("long")
lines = []
line_by_line = []
with open(file_path) as f:
  # o problema aqui foi rodar varios reads num mesmo while. aparentemente trem que rodar um por vez....
  #read_full_text = f.read()
  #print(read_full_text) # funciona
  #read_line_by_line = f.readline()
  #print(read_line_by_line) #-> não imprime nada
  read_lines = f.readlines() # não tá lendo nada.......
  #print(read_lines)
  for l in read_lines:
    lines.append(l)
        """
count = 0 
#print(read_lines)
"""
for l in range(len(read_lines)):
  count += 1
  print(f'line {count}: {read_lines[l][0:10]}')

"""
#print(len(read_lines))
"""
a = []
if not a :
  print("list is empty")

"""
def segmenta_imbarq(lines, target_group_list, target_range=[0,2]):
  target_list = target_group_list[0] # lista com os tipos de registros do arquivo IMBARQ001
  group_list = target_group_list[1]  # lista de listas vazias na quantidade do tipos de registros
  for i in range(len(lines)):
    if lines[i][target_range[0]:target_range[1]] == target_list[0]:
      print("make money")
    for j in range(len(target_list)):
      if lines[i][target_range[0]:target_range[1]] == target_list[j]:
        group_list[j].append(lines[i]) # add à lista de grupos cada segmento do IMBARQ001 separado individualmente  
        #print("pump it up")

  return group_list


read_lines = read_file_lines(file_path) # read text file IMBARQ001, lines into 

#target_list, group_list = create_group_target_list(read_lines) # not working

target_list, group_list = target_and_group_list() # cria as listas de tipo de registros e grupos (lista contendo listas vazias) para cada registro 
#print(target_list, group_list)
t_g_list = target_and_group_list() # mesma coisa de cima, mas em um item só, para simplicidade
#print(t_g_list)

g_list = segmenta_imbarq(read_lines, target_group_list=t_g_list) # retorna a lista de grupos (segregados por tipo de registros) 

file_title = g_list[0]
derivativos_fungiveis = g_list[1]
mercado_a_vista = g_list[2]
entrega_fisica = g_list[3]
recompra = g_list[4]
derivativos_nao_fungiveis = g_list[5]
aluguel_de_ativos = g_list[6]   # dar uma olhada 
termo = g_list[7]
opcoes_flexiveis = g_list[8]
barreiras_opcoes_flexiveis = g_list[9]
swap = g_list[10]
cesta_acoes_swap_sb1_sb2_balcao = g_list[11]
liquidacao_na_data_efetiva_informada = g_list[12]
lancamentos_para_efetivacao_futura = g_list[13]
informacao_das_liquidacoes_renovacoes_termo_aluguel = g_list[14]
liquidacao_antecipada_termo_aluguel = g_list[15]
detalhes_resultados_liquidos_liquidados_dia = g_list[16]
detalhes_resultados_liquidos_liquidado = g_list[17]
garantias_aportadas = g_list[18]
detalhes_acoes_ouro_carteira_garantias_custodian = g_list[31]
margem_requerida = g_list[19] # dar uma olhada importante
ofertas_book = g_list[20]
ofertas_prioritarias = g_list[21]
subscricoes = g_list[22]
eventos_dinheiro = g_list[23]
eventos_acoes = g_list[24]
subscricao = g_list[25]
dividendos = g_list[26]
bonificacao = g_list[27]
saldo_custodia = g_list[28]
saldo_custodia_bloqueado = g_list[29]
id_saldo_analitico = g_list[30]




#print(g_list[19])
#o_btc = organise_btc(aluguel_de_ativos)
#print(o_btc)
"""
for item in range(len(aluguel_de_ativos)):
  org_btc = organise_btc(aluguel_de_ativos, index_test=item)
  print(org_btc)
  if item == 9:
    break
"""

build_btc_list(aluguel_de_ativos)

#sum_net_btc(build_btc_list(aluguel_de_ativos))
# falta somar individualmente os ativos por fundo
"""
d = fund_brokerage_accounts() # fund accounts
for i in d:
  print(i, ':', d[i])

for i in d:
  for c in d[i]:
    print(i, ':', d[i][c])

"""
print()

fund_list = create_fund_list()
btc_list = build_btc_list(aluguel_de_ativos) 
fund_acc = fund_brokerage_accounts() # contas e corretoras de cada fundo por nickname

create_btc_list_for_each_fund(funds_accounts=fund_acc, btc_list=btc_list, fund_list=fund_list)
btc_of_all_funds = create_btc_list_for_each_fund(funds_accounts=fund_acc, btc_list=btc_list, fund_list=fund_list)
#print()
#print(btc_of_all_funds["ac_master_btc"])


#print(build_contract_list(aluguel_de_ativos))
objects = build_btc_contract_info(aluguel_de_ativos)

for i in range(len(objects)):
  jprint(objects[i])

