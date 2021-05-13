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
from funcoes import *


def handler(event, context):

  s3 = boto3.resource('s3')
  obj = s3.Object("abalustre-btc-contracts", event["Records"][0]['s3']['object']['key'])
  body = obj.get()["Body"].read().decode("utf-8")

  es = Elasticsearch(
      cloud_id = (os.environ["ELASTICID"]),
      http_auth = (os.environ["ELASTICUSER"], os.environ["ELASTICPASSWORD"]))

  read_lines = read_file_lines(body) # read file into list of lines
  tg_list = target_and_group_list()
  g_list = segmenta_imbarq(lines=read_lines, target_group_list=tg_list)
  btc_bulk = g_list[6]

  btc_obj_list = build_btc_contract_info(btc_bulk)

  btc_contract_list = []

  for i in range(len(btc_obj_list)):
    obj = btc_obj_list[i]
    contract_id = obj["contract-number"]
    position_date = obj["position-date"].strftime("%Y-%m-%d")
    btc_contract_list({
      "_index": "daily-position",
      "_type": "_doc",
      "_id": "C:"+contract_id+"_D:"+position_date,
      "_source": obj
    })

  json_data = '\n'.join(json.dumps(contract) for contract in btc_contract_list)
  data_post = ndjson.loads(json_data)
  helpers.bulk(es, data_post)
  
  return btc_contract_list




