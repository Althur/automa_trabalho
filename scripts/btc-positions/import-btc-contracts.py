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
from functions import *

def handler(event, context):

  s3 = boto3.resource('s3')
  obj = s3.Object("abalustre-btc-contracts", event["Records"][0]['s3']['object']['key'])
  body = obj.get()["Body"].read()
  #print(body[1])
  lines = body.splitlines()
  #print(str(lines[1], 'ISO-8859-1'))
#  print(str(lines[10], 'utf-8'))
#  line10 = str(lines[10], 'utf-8')
#  print(line10)
#  utf_lines = []
#  for i in range(len(lines)):
#    utf_lines.append(str(lines[i], 'utf-8'))
#  print(utf_lines)
  es = Elasticsearch(
      cloud_id = (os.environ["ELASTICID"]),
      http_auth = (os.environ["ELASTICUSER"], os.environ["ELASTICPASSWORD"]))
  tg_list = target_and_group_list()
  g_list = segmenta_imbarq(lines=lines, target_group_list=tg_list)
  btc_bulk = g_list[6]
  btc_obj_list = build_btc_contract_info(btc_bulk)
  btc_contract_list = []
  for i in range(len(btc_obj_list)):
    obj = btc_obj_list[i]
    print(type(obj))
    print(obj)
    contract_id = obj['contract_number']
    position_date = obj['position_date']
    btc_contract_list.append({
      "_index": "btc-contracts",
      "_type": "_doc",
      "_id": "C:"+contract_id+"_D:"+position_date,
      "_source": obj
    })

  json_data = '\n'.join(json.dumps(contract) for contract in btc_contract_list)
  data_post = ndjson.loads(json_data)
  helpers.bulk(es, data_post)
  
  return btc_contract_list


