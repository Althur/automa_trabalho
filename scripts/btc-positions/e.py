
import os
import sys
if os.environ["STAGE"] == "prod":
    sys.path.append("/mnt/access/")

import json
from elasticsearch import Elasticsearch 
from datetime import datetime,date
from dateutil.relativedelta import relativedelta



es = Elasticsearch(
    cloud_id = (os.environ["ELASTICID"]),
    http_auth = (os.environ["ELASTICUSER"], os.environ["ELASTICPASSWORD"]))

    