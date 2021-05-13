import os
import sys 
import csv
import pprint
import ndjson
import json
import boto3

import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

from datetime import timedelta, datetime

from xml.dom.minidom import parse, parseString


sys.path.append('.')
#from functions import *
from funcoes import *

#C:\Users\ForpusCapital\Box\FORPUS\Operacional\Carteiras\05-2021\10-05-2021\FD21917184000129_20210510_20210511090906_FORPUSACOES.xml

xml = 'FD21917184000129_20210510_20210511090906_FORPUSACOES.xml'
path = '../../../../Box/FORPUS/Operacional/Carteiras/05-2021/10-05-2021/'
body = path+xml

root = xml_root(body)

header = root.find("fundo").find("header")

isin = header.find("isin")
cnpj_fundo = header.find("cnpj")
nome_fundo = header.find("nome")
position_date = header.find("dtposicao")
nome_adm = header.find("nomeadm")

cnpj_adm = header.find("cnpjadm")
nome_gestor = header.find("nomegestor")
cnpj_gestor = header.find("cnpjgestor")
nome_custodiante = header.find("nomecustodiante") 
cnpj_custodiante = header.find("cnpjcustodiante")
valor_cota = header.find("valorcota") #*
quantidade = header.find("quantidade")
patrimonio_liq = header.find("patliq") #*
valor_ativos = header.find("valorativos")
valor_receber = header.find("valorreceber")
valor_pagar = header.find("valorpagar")
vl_cotas_emitir = header.find("vlcotasemitir")
vl_votas_resgatar = header.find("vlcotasresgatar")
cod_anbi_d = header.find("codanbid")
tipo_fundo = header.find("tipofundo")
nivel_risco = header.find("nivelrsc")


print(valor_cota.text)
print(patrimonio_liq.text)


directory = '../../../../Box/FORPUS/Operacional/Carteiras/05-2021/' # maio

for subdir, dirs, files in os.walk(directory):
  for filename in files:
    filepath = subdir + os.sep + filename

    if filepath.endswith("FORPUSACOES.xml"):
      print(filepath)

def soma_pl(dir, fundo="FORPUSACOES.xml"):
  count = 0
  soma = 0
  for subdir, dirs, files in os.walk(dir):
    #print(subdir)
    for filename in files:
      filepath = subdir + os.sep + filename

      if filepath.endswith(fundo):
        root = xml_root(filepath)
        header = root.find("fundo").find("header")
        patrimonio_liq = float(header.find("patliq").text)
        soma += patrimonio_liq
        count += 1
  #print('soma')
  #print(soma)
  #print()
  #print('count')
  #print(count)
  #print()
  #print('avg')
  #print(soma/count)
  return soma, count 

#sum, count = soma_pl(directory)

def soma_pl_maio_20(dir, fundo="FORPUSACOES.xml"):
  count = 0
  soma = 0
  for subdir, dirs, files in os.walk(dir):
    for filename in files:
      filepath = subdir + os.sep + filename
      if subdir.endswith("04-05-2020"):
        pass
      elif subdir.endswith("05-05-2020"):
        pass
      elif subdir.endswith("06-05-2020"):
        pass
      elif subdir.endswith("07-05-2020"):
        pass
      elif subdir.endswith("08-05-2020"):
        pass
      elif subdir.endswith("11-05-2020"):
        pass
      elif subdir.endswith("12-05-2020"):
        pass
      elif filepath.endswith(fundo):
        print(filepath)
        root = xml_root(filepath)
        header = root.find("fundo").find("header")
        patrimonio_liq = float(header.find("patliq").text)
        soma += patrimonio_liq
        count += 1
  print('soma')
  print(soma)
  print()
  print('count')
  print(count)
  print()
  print('avg')
  print(soma/count)
  return soma, count 

maio_21 = '../../../../Box/FORPUS/Operacional/Carteiras/05-2021/' # maio
abril_21 = '../../../../Box/FORPUS/Operacional/Carteiras/04-2021/' # 
marco_21 = '../../../../Box/FORPUS/Operacional/Carteiras/2021/03-2021/' # 
fev_21 = '../../../../Box/FORPUS/Operacional/Carteiras/2021/02-2021/' # 
jan_21 = '../../../../Box/FORPUS/Operacional/Carteiras/2021/01-2021/' # 
dez_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/12-2020/' # 
nov_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/11-2020/' # 
out_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/10-2020/' # 
set_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/09-2020/' # 
ago_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/08-2020/' # 
jul_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/07-2020/' # 
jun_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/06-2020/' 
maio_20 = '../../../../Box/FORPUS/Operacional/Carteiras/2015-2020/2020/05-2020/' # até o dia tal

sum_maio_21, count_maio_21 = soma_pl(maio_21)
sum_abril_21, count_abril_21 = soma_pl(abril_21)
sum_marco_21, count_marco_21 = soma_pl(marco_21)
sum_fev_21, count_fev_21 = soma_pl(fev_21)
sum_jan_21, count_jan_21 = soma_pl(jan_21)
sum_dez_20, count_dez_20 = soma_pl(dez_20)
sum_nov_20, count_nov_20 = soma_pl(nov_20)
sum_out_20, count_out_20 = soma_pl(out_20)
sum_set_20, count_set_20 = soma_pl(set_20)
sum_ago_20, count_ago_20 = soma_pl(ago_20)
sum_jul_20, count_jul_20 = soma_pl(jul_20)
sum_jun_20, count_jun_20 = soma_pl(jun_20)
sum_maio_20, count_maio_20 = soma_pl_maio_20(maio_20)

sum_all = sum_maio_20+sum_jun_20+sum_jul_20+sum_ago_20+sum_out_20+sum_set_20+sum_nov_20+sum_dez_20+sum_jan_21+sum_fev_21+sum_marco_21+sum_abril_21+sum_maio_21


