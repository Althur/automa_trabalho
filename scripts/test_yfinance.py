import json
import yfinance as yf
import pandas as pd
import os
import requests
import psycopg2
import math


"""
data = yf.Ticker('{}.SA'.format(company))
data_id = pd.DataFrame(data.history(period='max',
                                    actions = False,
                                    auto_adjust = False))

"""

# abrindo arquivo com todos os ativos negociados na b3
#path_ref = "C:\Users\ForpusCapital\Box\FORPUS"

#main_path = "../../../../../ForpusCapital/Box/FORPUS/Operacional/Trading/Boletagem/"
#main_path = "../../../../Downloads/"

main_path = "../../../../../ForpusCapital/Desktop/Arquivos teste/"
arquivo = "InstrumentsConsolidatedFile_20210423_1.csv"


full_path = main_path+arquivo

data = pd.read_csv(full_path, sep=';')

#print(data["TckrSymb"])

all_tickers = data["TckrSymb"].copy()

#for i in range(len(all_tickers)):
#  print(all_tickers[i])

start_date = "03/31/2021"
# pegar todos os dados da data start
all_tickers_yf_data = pd.DataFrame()

for i in range(len(all_tickers)):
  stock_data = yf.Ticker('{}.SA'.format(all_tickers[i]))
  stock_dataframe = pd.DataFrame(stock_data.history(period=start_date))
  print(stock_dataframe["Close"])
  all_tickers_yf_data.append(stock_dataframe)


# tentar printar apenas o closing price de uma ação

print(all_tickers_yf_data)
# bater as posições da forpus com os preços 


