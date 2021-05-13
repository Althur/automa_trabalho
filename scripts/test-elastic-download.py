import os
import sys 
import csv
import ndjson
import json
import boto3
import requests

import numpy as np
import pandas as pd

from datetime import timedelta, datetime, date
from elasticsearch import Elasticsearch, helpers

sys.path.append('.')
#from functions import *
from funcoes import *

es = Elasticsearch(
    cloud_id = "abalustre-3:dXMtZWFzdC0xLmF3cy5mb3VuZC5pbyQxZTAzYTMwOTViMTY0M2UyYTEyOTdhODE5MmNkMmJkZiQ1OWZiYjVmZTRiOTE0MTI0ODFjM2ZkYWE0MDFiMzc5NQ==",
    http_auth = ("elastic","zFPGnd9MRWtY33NElX3v9RQK")
)

query_body = {'query':{'match_all':{}}}
qb_ix = {}
qb_iv = {}
i = "indicators"
ix = "btc-contracts"
iv = "daily-position"
res_btc_contracts = es.search(index=ix, body=query_body, size=10000)
all_btc_contracts = res_btc_contracts['hits']['hits']
res_daily_position = es.search(index=iv, body=query_body, size=10000)
all_daily_position = res_daily_position['hits']['hits'] 

today = date.today().strftime("%Y-%m-%d")
yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

position_day = '2021-05-10'
print(type(position_day))
def print_btc(btc_contracts):
    for i in range(len(btc_contracts)):
        if btc_contracts[i]['_source']['position_date'] == position_day:
            print(btc_contracts[i]['_source'])
        else:
            print("other date")

def fund_cnpj():
    acoes_master = 21917206000150
    tech = 40212681000176
    multi = 37887638000104
    prev = 38281419000131
    cnpj_dict = {
        "acoes-master": str(acoes_master),
        "tech-fia-bdr": str(tech), 
        "multi": str(multi),
        "prev-master": str(prev)
    }
    return cnpj_dict

#print(all_daily_position)

def print_wallet(daily_p):
    position_day = '2021-05-03'
    for i in range(len(daily_p)):
        print(len(daily_p))
        if daily_p[i]['_source']['date'] == position_day:
            print(daily_p[i]['_source']['fund'])
            print(type(daily_p[i]['_source']['fund']))
        else:
            print("other date")
            
#print_wallet(all_daily_position)
def short_position(d_position, fund, p_day):
    #p_day = '2021-05-03'
    fund_position = []
    for i in range(len(d_position)):
        if d_position[i]['_source']['fund'] == fund:
            if d_position[i]['_source']['date'] == p_day:
                if d_position[i]['_source']['quantity'] < 0:
                    #print(d_position[i]['_source'])
                    obj = {
                        'symbol': d_position[i]['_source']['symbol'],
                        'quantity': d_position[i]['_source']['quantity']
                    }
                    fund_position.append(obj)
    return fund_position
def fund_btc_contracts(btc_contracts, fund, p_day): # retorna lista de dicts contendo a soma dos contratos de aluguel por ticker em determinado fundo e dia 
    #p_day = '2021-05-03'
    btc_contracts_position = []
    bulk = []
    for i in range(len(btc_contracts)):
        if btc_contracts[i]['_source']['fund_nickname'] == fund:
            if btc_contracts[i]['_source']['position_date'] == p_day:
                if btc_contracts[i]['_source']['net_present_quantity'] > 0:
                    obj = {
                        "symbol": btc_contracts[i]['_source']['ticker_symbol'],
                        "net_quantity": btc_contracts[i]['_source']['net_present_quantity']
                    }
                    bulk.append(obj)
                    #i_list = [btc_contracts[i]['_source']['ticker_symbol']]
                    btc_contracts_position.append(btc_contracts[i]['_source']['ticker_symbol'])
                    #print(btc_contracts[i]['_source']['net_present_quantity'])

    btc_contracts_tickers = list(set(btc_contracts_position))
    net_contracts = []
    for i in range(len(btc_contracts_tickers)):
        i_list = [btc_contracts_tickers[i], 0]
        net_contracts.append(i_list)
        
    for i in range(len(btc_contracts_tickers)):
        for j in range(len(bulk)):
            if net_contracts[i][0] == bulk[j]['symbol']:
                net_contracts[i][1] += bulk[j]['net_quantity']
    return net_contracts#btc_contracts_tickers #net_contracts

def btc_needed(short_p, fb_contracts): # retorna lista de quantidade de btc para tomar (caso numero positivo) e quantidade para liquidar (caso numero negativo)
    need_btc = []
    for i in range(len(short_p)):
        for j in range(len(fb_contracts)):
            i_list = []
            if short_p[i]['symbol'] == fb_contracts[j][0]:
                i_list.append(short_p[i]['symbol'])
                i_list.append(fb_contracts[j][1]+short_p[i]['quantity'])
                need_btc.append(i_list)
    return need_btc

print(len(res_btc_contracts['hits']))
print(len(all_btc_contracts))
print(len(res_daily_position['hits']))
print(len(all_daily_position))
#print(res_btc_contracts)
#print(all_daily_position)
#print(all_btc_contracts)
fund_cnpjs = fund_cnpj()
master_cnpj = fund_cnpjs['acoes-master']


fund_short_position = short_position(all_daily_position, master_cnpj, p_day = '2021-05-10')

f = 'acoes-master' # fund na funcao abaixo

n = fund_btc_contracts(all_btc_contracts, f, p_day = '2021-05-10')
print("sum btc")
for i in range(len(n)):
    print('{}   {}'.format(n[i][0],n[i][1]))
print(n)
print()
print("fund-short positions")
for i in range(len(fund_short_position)):
    print('{}   {}'.format(fund_short_position[i]['symbol'], fund_short_position[i]['quantity']))

print()
nbtc = btc_needed(fund_short_position, n)
print("btc needed")
for i in range(len(nbtc)):
    print('{}   {}'.format(nbtc[i][0],nbtc[i][1]))
print(nbtc)