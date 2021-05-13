import requests
import json


CERT = 'http://www.bvmfnet.com.br/pt-br/servicos/download/Conectividade_pos_negociacao_certificacao.pdf'
PROD = 'http://www.bvmfnet.com.br/pt-br/servicos/download/Conectividade_pos_negociacao_Producao.pdf'

ACESSO_BTB_BUY_SIDE = 'https://btb.b3.com.br/'
ACESSO_IMERCADO = 'imercado.btb.com.br/BTB'


# Dados obrigatórios para incluir ordem no livro de ofertas
# verbo: POST
# metodo: order/entry
id_participante = '3'
investidor_participante = '802656'
# custodiante codigo = ''
# custodiante conta  = ''
security_symbol = 'ticker'
prazo_liquidação_ = 0 # 0 = d+0; 1 = D+1 
indicador_ordem_certificada = True # booleano; True = sim; False = nao
quantidade = 10000 # bigInt; numero inteiro com limite grande de digitos
taxa = 11.1 # decimal
exp_date = '2021-06-17' # type date
order_type = '1' # 1 = Doador, 2 = Tomador

# consultar orderm


# consultar book de ofertas disponíveis
# verbo: GET
# Método: book/list/{symbol}/{daysToSettlementIndicator}
# retorna as 100 melhores ofertas disp de determinado instrumento


codigo_neg = 'ticker'
prazo_liquidação = 1


