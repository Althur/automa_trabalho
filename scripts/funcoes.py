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
from elasticsearch import Elasticsearch, helpers
from boxsdk import OAuth2, Client
from xml.dom.minidom import parse, parseString

def read_file_lines(file_path): # read txt file
    with open(file_path) as f:
        read_lines = f.readlines()
    print(len(read_lines))

    return read_lines


def posicao_acoes(linhas_arquivo):
    target_1 =['Ação']
    target_2 =['Total']
    index_target_1 = 0
    index_target_2 = 0
    posicao = []
    for i in range(len(linhas_arquivo)):
        if linhas_arquivo[i] == target: 
            index_target_1 = i

    for i in range(len(linhas_arquivo[index_target_1:])):
        posicao.append(linhas_arquivo[index_target_1+i+2])
        if linhas_arquivo[index_target_1+i+2][0] == target_2:
            break

    return posicao
    
def target_and_group_list():
    grupo_00 = []
    target_00 = '00'
    grupo_01 = []
    target_01 = '01'
    grupo_02 = []
    target_02 = '02'
    grupo_03 = []
    target_03 = '03'
    grupo_04 = []
    target_04 = '04'
    grupo_05 = []
    target_05 = '05'
    grupo_06 = []
    target_06 = '06'
    grupo_07 = []
    target_07 = '07'
    grupo_08 = []
    target_08 = '08'
    grupo_09 = []
    target_09 = '09'
    grupo_10 = []
    target_10 = '10'
    grupo_11 = []
    target_11 = '11'
    grupo_12 = []
    target_12 = '12'
    grupo_13 = []
    target_13 = '13'
    grupo_14 = []
    target_14 = '14'
    grupo_15 = []
    target_15 = '15'
    grupo_16 = []
    target_16 = '16'
    grupo_17 = []
    target_17 = '17'
    grupo_18 = []
    target_18 = '18'
    grupo_19 = []
    target_19 = '19'
    grupo_20 = []
    target_20 = '20'
    grupo_21 = []
    target_21 = '21'
    grupo_22 = []
    target_22 = '22'
    grupo_23 = []
    target_23 = '23'
    grupo_24 = []
    target_24 = '24'
    grupo_25 = []
    target_25 = '25'
    grupo_26 = []
    target_26 = '26'
    grupo_27 = []
    target_27 = '27'
    grupo_28 = []
    target_28 = '28'
    grupo_29 = []
    target_29 = '29'
    grupo_30 = []
    target_30 = '30'
    grupo_31 = []
    target_31 = '31'
    grupo_32 = []
    target_32 = '32'
    grupo_33 = []
    target_33 = '33'
    grupo_34 = []
    target_34 = '34'
    grupo_35 = []
    target_35 = '35'
    grupo_36 = []
    target_36 = '36'
    grupo_37 = []
    target_37 = '37'
    grupo_38 = []
    target_38 = '38'
    grupo_39 = []
    target_39 = '39'
    grupo_40 = []
    target_40 = '40'

    group_list = [grupo_00, grupo_01, grupo_02, grupo_03, grupo_04, grupo_05, grupo_06, grupo_07, grupo_08, grupo_09, grupo_10, 
    grupo_11, grupo_12, grupo_13, grupo_14, grupo_15, grupo_16, grupo_17, grupo_18, grupo_19, grupo_20, grupo_21,
    grupo_22, grupo_23, grupo_24, grupo_25, grupo_26, grupo_27, grupo_28, grupo_29, grupo_30, grupo_31, grupo_32, 
    grupo_33, grupo_34, grupo_35, grupo_36, grupo_37, grupo_38, grupo_39, grupo_40]

    target_list = [target_00, target_01, target_02, target_03, target_04, target_05, target_06, target_07, target_08, target_09, target_10, 
    target_11, target_12, target_13, target_14, target_15, target_16, target_17, target_18, target_19, target_20, target_21,
    target_22, target_23, target_24, target_25, target_26, target_27, target_28, target_29, target_30, target_31, target_32, 
    target_33, target_34, target_35, target_36, target_37, target_38, target_39, target_40]

    return target_list, group_list


def create_group_target_list(file_lines, target_size=[0,2]):#not working
    #target_size = target_range
    target_list = []
    group_list = []
    print("empty lists created")
    for i in range(len(file_lines)):
        if not target_list:
            print("must add element to list")
            print("adding element...")
            target_list.append(file_lines[i][target_size[0]:target_size[1]])
        for j in range(len(target_list)):
            print(target_list[j])
            if target_list[j] == file_lines[i][target_size[0]:target_size[1]]:
                pass
            else:
                target_list.append(file_lines[i][target_size[0]:target_size[1]])
                
    for i in range(len(target_list)):
        empty_list = []
        group_list.append(empty_list)

    return target_list, group_list


def organise_btc(btc_data, index_test = 1):

    register_id = btc_data[index_test][0:2]
    participant_id = btc_data[index_test][2:17] # verificar se é fixo ou não
    applicant_investor_id = btc_data[index_test][17:32] # verificar se é fxo
    applicant_participant_id = btc_data[index_test][32:47] 
    required_investor_id = btc_data[index_test][47:62] # verificar
    movement_date = btc_data[index_test][62:72]                               # data da posição/movimentação YYYY-MM-DD
    instrument_id = btc_data[index_test][72:107] # muda
    instrument_origin_id = btc_data[index_test][107:142] # muda
    exchange_code = btc_data[index_test][142:146]                             # ?
    origin = btc_data[index_test][146:158]
    contract_number = btc_data[index_test][159:193]                           # numero do contrato mesmo
    previous_contract_number = btc_data[index_test][193:228]                  # ?
    nature = btc_data[index_test][228:229]
    underlying_asset_id = btc_data[index_test][229:264]
    asset_source_id = btc_data[index_test][264:299]
    exchange_asset_code = btc_data[index_test][299:303]
    asset_isin = btc_data[index_test][303:315]
    underlying_asset_distribution = btc_data[index_test][315:325]
    market = btc_data[index_test][325:328]
    ticker_symbol = btc_data[index_test][328:363]
    trade_date =  btc_data[index_test][363:373]                              # pegar esse
    expire_date = btc_data[index_test][373:383]                              # pegar esse
    due_date = btc_data[index_test][383:393]                                 # ? # data de carência
    portfolio_id = btc_data[index_test][393:428]
    referenc_price_underlying_asset = btc_data[index_test][428:454]
    factor = btc_data[index_test][454:464]
    original_quantity = btc_data[index_test][464:479]                        # ainda não entendi a diff entre essas 7 quantitades
    liquidation_quantity = btc_data[index_test][479:494]                     # ainda não entendi a diff entre essas 7 quantitades
    total_liquidated_quantity = btc_data[index_test][494:520]                # ainda não entendi a diff entre essas 7 quantitades
    quantity_covered = btc_data[index_test][520:535]                         # ainda não entendi a diff entre essas 7 quantitades
    quantity_uncovered = btc_data[index_test][535:550]                       # ainda não entendi a diff entre essas 7 quantitades
    quantity_renewed = btc_data[index_test][550:576]                         # ainda não entendi a diff entre essas 7 quantitades
    present_quantity = btc_data[index_test][576:591]                         # ainda não entendi a diff entre essas 7 quantitades
    volume = btc_data[index_test][591:611]
    type_of_liquidation = btc_data[index_test][611:612]# bruto ou liquido
    early_liquidation_id = btc_data[index_test][612:613]
    opa_early_liquididation_id = btc_data[index_test][613:614]
    contract_interest = btc_data[index_test][614:640]                        # 5 casas decimais. e.g. (..010000 = 0.1%)
    executor_participant = btc_data[index_test][640:650]                     # número da corr. e.g. XP = 3. 
    executor_participant_investor = btc_data[index_test][650:665]            # numero da conta do fundo na corr. e.g. Tech-Xp 807156
    jcp_interest_tax_id = btc_data[index_test][665:666]
    contraparte_tributada_rendimento = btc_data[index_test][666:667]
    contract_type = btc_data[index_test][667:668]
    liquidation_id = btc_data[index_test][668:732]
    reserve_space = btc_data[index_test][733:1000]

    #elements_observed = [ticker_symbol, present_quantity, contract_number, trade_date, expire_date, liquidation_quantity, contract_interest, contract_type]
    #elements_observed = [quantity_covered, quantity_uncovered, quantity_renewed, present_quantity]
    #elements_observed = [ticker_symbol, present_quantity, origin, nature]
    #coisas_que_nao_sei = [origin, nature, volume, type_of_liquidation, liquidation_id, contract_type]
    #a_principio_inutil = [exchange_code, reserve_space]
    #observe = [ticker_symbol, liquidation_quantity, present_quantity]
    #print(observe)

    #print(present_quantity)
    #int_present_quantity = int(present_quantity)
    #int_liquidation_quantity = int(liquidation_quantity)
    #int_contract_interest = int(contract_interest)

    full_source = {  # per contract
        "date-of-register": trade_date,
        "contract-quantity": int(present_quantity),  # needs to be int
        "ticker-symbol": ticker_symbol,
        "previous-liquidation-quantity": liquidation_quantity, # needs to be int
        "contract-id": contract_number,
        "fund-account-and-broker": {
            "broker": executor_participant,
            "account_number": executor_participant_investor
        },
        "position-reference-date": movement_date, 
        "contract-exp-date": expire_date,
        "net-contract-quantity":'',#int_present_quantity-int_liquidation_quantity,
        "contract-interest-rate": contract_interest
    }

    elements_observed = [ticker_symbol, liquidation_quantity, present_quantity, 
    movement_date, trade_date, expire_date, executor_participant_investor, 
    contract_number, executor_participant, contract_interest, nature, underlying_asset_id, 
    due_date, portfolio_id, referenc_price_underlying_asset, 
    ]

    #print(elements_observed)
    return elements_observed #full_source # elements_observed,

def build_contract_list(contract_source, fund_nick):
    fund_list = create_fund_list()

    all_contracts = {

    }
    for i in range(len(fund_list)):
        if all_contracts:
            if fund_list[i] == all_contracts[fund_list[i]]:
                a={
                    fund_list[i]:all_contracts[fund_list[i]]
                }
                all_contracts.update()
            else:
                pass
        else:
            pass

    contract_list = []

def fund_brokerage_accounts_beta():
    # "fund-nickname-brocker": account_number
    obj = {
        "tech-fia-bdr-xp": 807156,
        "tech-fia-bdr-futura": 17808,
        "tech-fia-bdr-pactual": 1245356,
        "acoes-master-xp": 802665, 
        "acoes-master-futura": 12707, 
        "acoes-master-guide": 746632,
        "acoes-master-pactual": 495305,
        "acoes-master-itau": 1067558,
        "multi-xp": 806787,
        "multi-futura": 17651,
        "prev-100-master-xp": 806892,
        "prev-100-master-futura": 17757
    }
    return obj

def fund_brokerage_accounts():
    # "fund-nickname-brocker": account_number
    obj = {
        "tech-fia-bdr":{
            "xp": 807156,
            "pactual": 1245356,
            "futura": 17808
        },
        "acoes-master":{
            "xp": 802665,
            "pactual": 495305,
            "guide": 746632,
            "futura": 12707,
            "itau": 1067558
        },
        "multi":{
            "xp": 806787,
            "futura": 17651
        },
        "prev-100-master":{
            "xp": 806892,
            "futura": 17757
        }
    }
    return obj

def btc_position(current_btc_list):

    btc_list = []

    # incompleto
    return btc_list

def build_btc_list(btc_elements):
    # btc_elements = aluguel_de_ativos

    #btc_elements = btc_elements[0]

    elements = []
    for i in range(len(btc_elements)):
        elements.append(organise_btc(btc_elements, index_test=i))


    btc_list = []
    for item in range(len(elements)):
        #print(elements[item][1])
        #print(int(elements[item][1]))
        ticker_symb = elements[item][0].strip()
        liquidation_qnty = -int(elements[item][1])
        contract_quantity = int(elements[item][2])
        #print(contract_quantity+3)
        date_of_position = elements[item][3] # data da posicao
        date_of_trade = elements[item][4] # data de registro
        expiration_date = elements[item][5] # data do vcto do contrato
        fund_id = int(elements[item][6]) # C/C do fundo na respectiva corretora 
        interm_list = [ticker_symb, liquidation_qnty, contract_quantity, date_of_position,
                        date_of_trade, expiration_date, fund_id]

        btc_list.append(interm_list)

    return btc_list

def expiration_date_alert(btc_list):
    # returns elements that have expiration date close by
    return None

def sum_net_btc(fund_btc_list):
    ticker_list = []
    btc_net_sum = []
    for i in range(len(fund_btc_list)):
        ticker_list.append(fund_btc_list[i][0])
    ticker_list = list(set(ticker_list))

    for i in range(len(ticker_list)):
        i_list = []
        i_list.append(ticker_list[i])
        i_list.append(0)
        btc_net_sum.append(i_list)

    for j in range(len(fund_btc_list)):
        for k in range(len(btc_net_sum)):
            if fund_btc_list[j][0] == btc_net_sum[k][0]:
                btc_net_sum[k][1] += fund_btc_list[j][1]+fund_btc_list[j][2]
    print(btc_net_sum)
    return btc_net_sum

def create_fund_list():
    tech = "tech-fia-bdr"
    master = "acoes-master"
    multi = "multi"
    prev_master = "prev-100-master"

    fund_list = [tech, master, multi, prev_master]

    return fund_list

def fund_btc_list(btc_list, fund_accounts): # 

    funds_btc_list = []

    for accounts in range(len(fund_accounts)):
        #print(fund_accounts[accounts]+2)
        for contract in range(len(btc_list)):
            #print(btc_list[contract][5]+2)
            if fund_accounts[accounts] == btc_list[contract][6]:# fund_id index
                funds_btc_list.append(btc_list[contract])
                #print(btc_list[contract][5])

    return funds_btc_list

def print_btc(net_fund_btc):
    for i in range(len(net_fund_btc)):
        print('{}'.format(net_fund_btc[i][0]))
    for i in range(len(net_fund_btc)):
        print('{}'.format(net_fund_btc[i][1]))

    return True 

def create_btc_list_for_each_fund(funds_accounts, btc_list, fund_list):
    
    tech = fund_list[0]
    master = fund_list[1]
    multi = fund_list[2]
    prev_master = fund_list[3]

    tech_accounts = []
    master_accounts = []
    multi_accounts = []
    prev_master_accounts = []

    tech_btc_list = []
    master_btc_list = []
    multi_btc_list = []
    prev_master_list = []

    for accounts in funds_accounts:
        #print(accounts)  # apelido dos fundos
        for account in funds_accounts[accounts]:
            #print(funds_accounts[accounts][account]) contas 
            if accounts == tech:
                tech_accounts.append(funds_accounts[accounts][account])
                print(tech_accounts)
            elif accounts == master:
                master_accounts.append(funds_accounts[accounts][account])
            elif accounts == multi:
                multi_accounts.append(funds_accounts[accounts][account])
            elif accounts == prev_master:
                prev_master_accounts.append(funds_accounts[accounts][account])
    #for fund_accounts in all_accounts:
    tech_btc_list = fund_btc_list(btc_list=btc_list, fund_accounts=tech_accounts)
    master_btc_list = fund_btc_list(btc_list=btc_list, fund_accounts=master_accounts)
    multi_btc_list = fund_btc_list(btc_list=btc_list, fund_accounts=multi_accounts)
    prev_master_btc_list = fund_btc_list(btc_list=btc_list, fund_accounts=prev_master_accounts)
    #print(tech_btc_list)
    print(tech)
    #print(tech_btc_list)
    print(len(tech_btc_list))

    net_tech_btc_list = sum_net_btc(tech_btc_list)
    net_master_btc_list = sum_net_btc(master_btc_list)
    net_multi_btc_list = sum_net_btc(multi_btc_list)
    net_prev_master_btc_list = sum_net_btc(prev_master_btc_list)

    #print(net_tech_btc_list)
    #print_btc(net_tech_btc_list)
    #print_btc(net_master_btc_list)
    #print_btc(net_multi_btc_list)
    print_btc(net_prev_master_btc_list)

    all_funds = {
        "tech_btc": net_tech_btc_list,
        "ac_master_btc": net_master_btc_list,
        "prev_master_btc": net_prev_master_btc_list,
        "multi_btc": net_multi_btc_list
    }

    return all_funds

            
def build_contract_list(btc_elements):
    # btc_elements = aluguel_de_ativos
    btc_elements = btc_elements[1]
    elements = []
    for i in range(len(btc_elements)):
        elements.append(organise_btc(btc_elements, index_test=i))


    btc_list = []
    for item in range(len(elements)):
        ticker_symb = elements[item][0].strip()
        liquidation_qnty = -int(elements[item][1])
        contract_quantity = int(elements[item][2])
        #print(contract_quantity+3)
        date_of_position = elements[item][3] # data da posicao
        date_of_trade = elements[item][4] # data de registro
        expiration_date = elements[item][5] # data do vcto do contrato
        fund_id = int(elements[item][6]) # C/C do fundo na respectiva corretora 
        interm_list = [ticker_symb, liquidation_qnty, contract_quantity, date_of_position,
                        date_of_trade, expiration_date, fund_id]

        btc_list.append(interm_list)

    return btc_list


def build_btc_contract_info(btc_elements):

    elements = []

    for i in range(len(btc_elements)):
        elements.append(organise_btc(btc_elements, index_test=i))

    fund_acc = fund_brokerage_accounts()

    btc_obj_list = []
    broker_obj = counterparty_list()
    xp_number = broker_obj["xp"]
    guide_number = broker_obj["guide"]
    pactual_number = broker_obj["pactual"]
    futura_number = broker_obj["futura"]

    for item in range(len(elements)):
        ticker_symb = elements[item][0].strip()
        liquidation_qnty = -int(elements[item][1])
        contract_quantity = int(elements[item][2])
        date_of_position = elements[item][3]
        date_of_trade = elements[item][4]
        expiration_date = elements[item][5]
        fund_acc_number = int(elements[item][6])
        contract_id = elements[item][7].strip()
        broker_number = int(elements[item][8])
        net_contract_quantity = contract_quantity+liquidation_qnty
        contract_interest = int(elements[item][9])
        portfolio_id = int(elements[item][13])
        referenc_price_underlying_asset = int(elements[item][14])  # = n/10^7
        if int(elements[item][10]) == 4: # pegar se eh doador ou tomador
            lender_borrower = "T"    
        elif int(elements[item][10]) == 3:
            lender_borrower = "D"
        test_element = int(elements[item][11])
        due_date = elements[item][12]
        if broker_number == xp_number:
            counterparty = "xp"
        elif broker_number == guide_number:
            counterparty = "guide"
        elif broker_number == pactual_number:
            counterparty = "pactual"
        elif broker_number == futura_number:
            counterparty = "futura"
        else:
            counterparty = "not-listed... corretora não cadastrada no código #def build_btc _contract_info"
        for fund in fund_acc:
            for acc in fund_acc[fund]:
                if fund_acc_number == fund_acc[fund][acc]:
                    nick = fund
                else: 
                    pass

        #counterparty = elements[item][13]  if == 3 XP 
        #executor_participant_investor = 
        obj = {
            "position-date": date_of_position, # format:
            "lender-borrower": lender_borrower, 
            "ticker-symbol": ticker_symb, 
            "fund-account-number": fund_acc_number, 
            "contract-number": contract_id,
            "register-date": date_of_trade, 
            "previous-liquidation-quantity": liquidation_qnty, 
            "expire-date": expiration_date, 
            "due-date": due_date,
            "test-element": test_element,
            "quantity": contract_quantity,
            "net-present-quantity": net_contract_quantity, 
            "wallet-number": portfolio_id, # carteira planilha margem novo
            "underlying-asset-price": referenc_price_underlying_asset,  # ver na planilha margem novo
            "contract-interest-rate": contract_interest,
            "counterparty": counterparty, # contra parte
            "brokerage-firm": broker_number, # corretora
            "daily-cost": '', # custo diario
            "days-to-exp": '', # dias até vcto -> formula business days
            "margin-call": '', # chamada-de margem
            "fund-nickname": nick
        }

        btc_obj_list.append(obj)

    return btc_obj_list


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def counterparty_list():
    c_list = {
        "xp": 3, 
        "pactual": 85,
        "futura": 93,
        "orama": 3701,
        "credit-suisse": 6003,
        "morgan-stanely": 40,
        "c6": 6003,
        "inter": 1099,
        "itau": 114,
        "cm": 88,
        "tullett": 127,
        "terra": 107,
        "modal": 1982,
        "bny-mellon": 3611, # pq que tem no imbarq apenas algumas contas e n de todos os fundos?
        "jpm": 16,
        "guide": 15,
        "merril-lynch": 13,
    }
    return c_list

def counterparty_liquidation_list():
    # Criar aqui a lista dos nomes das corretoras "aceitas" pela mellon. e.g.: XP = AMERINV
    return 0

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



def xml_root(source):
    tree = ET.parse(source)
    root = tree.getroot()
    #root = ET.fromstring(source)
    return root



