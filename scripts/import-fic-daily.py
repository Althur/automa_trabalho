import os
import sys 
import csv
import ndjson
import json
import boto3

import numpy as np
import pandas as pd

from datetime import timedelta, datetime
from elasticsearch import Elasticsearch, helpers

sys.path.append('.')
#from functions import *
from funcoes import *


def handler(event, context):

  root = xml_root(body)
  header = root.find("fundo").find("header")
  date = datetime.strptime(header.find("dtposicao").text, "%Y%m%d")
  fund = header.find('cnpj').text
  quota = int(float(header.find('valorcota').text) * 100000000)
  admin = header.find('cnpjadm').text
  custodian = header.find('cnpjcustodiante').text
  equity = float(header.find('patliq').text)
  fund_name = header.find("nome").text
  manager = header.find("nomegestor").text 

  obj = {
    "date": date.strftime("%Y-%m-%d"),
    "fund": fund,
    "quota": quota,
    "equity": equity,
    "fund_name": fund_name,
    "administrator": admin,
    "custodian": custodian,
    "manager": manager
    }

    import_data = {
      "_index": "fic-daily-info",
      "_type": "_doc",
      "_id": fund+"_"+date,
      "_source": obj
    }

  json_data = '\n'.join(json.dumps(import_data))
  data_post = ndjson.loads(json_data)
  helpers.bulk(es, data_post)
