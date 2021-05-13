import numpy as np

pl_12m = {
  "mes1": 100*10**6,
  "mes2": 100*10**6,
  "mes3": 100*10**6,
  "mes4": 100*10**6,
  "mes5": 100*10**6,
  "mes6": 100*10**6,
  "mes7": 100*10**6,
  "mes8": 100*10**6,
  "mes9": 100*10**6,
  "mes10": 100*10**6,
  "mes11": 100*10**6,
  "mes12": 100*10**6
}
const = 20
pl_meta = 150*10**6
captacao = const*10**6
r = 0.34/8

def plm(pl_12meses):
  soma = 0
  for i in range(len(pl_12meses)):
    soma += pl_12meses['{}{}'.format('mes', i+1)]
  avg = soma/len(pl_12meses)

  return avg

def pl_dinamico(pl_12meses, captacao_mensal=0, rentab = 0):
  rentabilidade = 1+rentab
  pl_d = {
  "mes1": pl_12meses["mes2"],
  "mes2": pl_12meses['mes3'],
  "mes3": pl_12meses['mes4'],
  "mes4": pl_12meses['mes5'],
  "mes5": pl_12meses['mes6'],
  "mes6": pl_12meses['mes7'],
  "mes7": pl_12meses['mes8'],
  "mes8": pl_12meses['mes9'],
  "mes9": pl_12meses['mes10'],
  "mes10": pl_12meses['mes11'],
  "mes11": pl_12meses['mes12'],
  "mes12": (pl_12meses['mes12']*rentabilidade)+captacao_mensal
  }
  return pl_d


pl_medio = plm(pl_12m)


print(pl_medio)
pld = pl_dinamico(pl_12m, captacao)
print(pld)

meses = 0

pl_12m_inicial = pl_12m
plm_12m_inicial = plm(pl_12m_inicial)

while pl_medio < pl_meta:
  pl_12m = pl_dinamico(pl_12m, captacao, r)
  pl_medio = plm(pl_12m)
  meses += 1

print("considerando: o PL inicial de {} e, o PL medio 12m de {} e, a captacao mensal media de {}.".format(pl_12m_inicial["mes12"], plm_12m_inicial, captacao))
print(" O fundo depois de {} meses o fundo atingiu o PL medio de 12m {}. E seu PL atual é {}".format(meses, pl_meta, pl_medio))

print(r*100)

#def quanto_precisa_captar(plmedio, periodo):

"""for i in range(2):
  print('forlk')"""

#def quanto_captar_ate_pl_meta(pl_inicial, periodo, rentab, pl_meta = 150):

potencia = 3
contador = 0
obj_rent = {}
#while potencia > contador:
#  l = "rent{}".format(contador+1)
#  obj = {l: (potencia-contador)}
#
#

def calcula_captacao(periodos, pl_meta):
  soma_pl_captacao = 1

  return soma_pl_captacao


def calcula_pl(c, r, n, i):
  capt = c*(1+r)**(n-i)

  return capt

def soma_captacao(c, r, n):
  soma = 0

  for i in range(n):
    capt = calcula_pl(c, r, n, (i+1))
    soma += capt

  return soma
def media(soma, n):
  avg = soma/n
  return avg

def teste():
  c = 1000
  r = 0.04
  n = 6
  
  #soma = c*(1+r)**(n-1) + c*(1+r)**(n-2) + c*(1+r)**(n-3) + c*(1+r)**(n-4) + c*(1+r)**(n-5) + c*(1+r)**(n-6)
  #print(soma)

  return c, r, n
print()
c, r, n = teste()
soma = soma_captacao(c, r, n)
print(soma)

avg = media(soma, n)

