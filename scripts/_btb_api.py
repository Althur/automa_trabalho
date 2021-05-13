import requests
import json


#hash11_api = "https://api.hashdex.io/prod/marketdata/v1/inav/HASH11"

#response = requests.get(hash11_api) # 202 if working

import os
import sys
if os.environ["STAGE"] == "prod":
    sys.path.append("/mnt/access/")

import json
from elasticsearch import Elasticsearch 
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

def answer(statusCode, data = {}):
    try:
        return {
            'headers': {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": True
            },
            'statusCode': statusCode,
            'body': json.dumps(data)
        }
    except Exception as e:
        print('### ERROR')
        print(e)

def handler(event, context):   
    try:
        items_in_page = 30
        try:
            order = str(event["multiValueQueryStringParameters"]['order'][0])
        except:
            order = "desc"

        try:
            current_page = int(event["multiValueQueryStringParameters"]['page'][0])
        except:
            current_page = 1
        
        try:
            to_date = datetime.strptime(event["multiValueQueryStringParameters"]['to'][0], "%Y-%m-%d")
        except:
            to_date = date.today()
        try:
            from_date = datetime.strptime(event["multiValueQueryStringParameters"]['from'][0], "%Y-%m-%d")
        except:
            from_date = to_date + relativedelta(days =- 29)
        
        from_data = (current_page - 1)*items_in_page
        es = Elasticsearch(
            cloud_id = (os.environ["ELASTICID"]),
            http_auth = (os.environ["ELASTICUSER"],os.environ["ELASTICPASSWORD"])
        )
        
        query_body = {
            "from": "{}".format(from_data),
            "sort":[{
                "timestamp":{"order":"{}".format(order)}
            }],
            "query" : {
                "range": {
                    "timestamp": {
                        "gte": from_date.strftime("%Y-%m-%d"),
                        "lte": to_date.strftime("%Y-%m-%d")
                    }
                }
            }
        }
        res = es.search(index="indicators", body=query_body, size = items_in_page)
        result = res["hits"]["hits"]
        totally = res["hits"]['total']['value']
        list_result = []

        for i in range(len(result)):
            result_elastic = result[i]["_source"]
            list_result.append(result_elastic)
        
        num_pages = int(totally/items_in_page)
        if totally%items_in_page > 0:
            num_pages+=1
        
        if current_page > num_pages:
            status_code = 404
        else:
            status_code = 200
        
        data_return = { 
            "data": list_result,
            "pagination": {
                "current": current_page ,
                "items": totally,
                "pages": num_pages
            }
        }

        return answer(status_code , data_return)


    except (Exception) as error:
        print("###ERROR")
        print(error)