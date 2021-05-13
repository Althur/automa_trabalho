import os
import sys 
import csv
import ndjson
import json
import boto3
import requests

import numpy as np
import pandas as pd

from datetime import timedelta, datetime
from elasticsearch import Elasticsearch, helpers

sys.path.append('.')
#from functions import *
from functions import *

#es = Elasticsearch(
#    cloud_id = (os.environ["ELASTICID"]),
#    http_auth = (os.environ["ELASTICUSER"],os.environ["ELASTICPASSWORD"])
#)


es = Elasticsearch(
    cloud_id = "abalustre:dXMtZWFzdC0xLmF3cy5mb3VuZC5pbyRjYWNkNzFlNDIyOGE0YjhkOThhZDI0YzAzMzRjMDQ0NSRhM2QxNGRhN2M5Nzc0NzQ4YjljMzJlNTc0MTNmYzI3MA==",
    http_auth = ("elastic","zFPGnd9MRWtY33NElX3v9RQK")
)

resp = es.search(
  index="btc-contracts",
  body={"query":{"match_all": {}}}
)

print(resp['hits'])