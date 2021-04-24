import pandas as pd
import numpy as np


w = {
}

fund_list = ["tech", "ac-master", "multi", "prev"]


for i in range(len(fund_list)):
  if fund_list[i] == "tech":
    a = {
      fund_list[i]:100-2
    }
    w.update(a)
  elif fund_list[i] == "ac-master":
    a = {
      fund_list[i]:55
    }
    w.update(a)
  elif fund_list[i] == "multi":
    a = {
      fund_list[i]:0
    }
    w.update(a)
  elif fund_list[i] == "prev":
    a = 0.5
    a = {
      fund_list[i]:0.5
    }
    w.update(a)

print(w)
  

update_list =  ["tech", "ac-master", "multi", "prev"]

for i in range(len(fund_list)):
  if fund_list[i] == "tech":
    a = {
      fund_list[i]:w[fund_list[i]] + 100-2
    }
    w.update(a)
  elif fund_list[i] == "ac-master":
    a = {
      fund_list[i]:55
    }
    w.update(a)
  elif fund_list[i] == "multi":
    a = {
      fund_list[i]:0
    }
    w.update(a)
  elif fund_list[i] == "prev":
    a = 0.5
    a = {
      fund_list[i]:0.5
    }
    w.update(a)

print(w)

h = {}

if h:
  print(True)
else:
  print(False)