__author__ = 'Harsh'
from pymongo import MongoClient
import json
import time
def connect():
    connection = MongoClient('localhost', 27017)
    db = connection.job_vacancy_revised
    collection = db.data
    return collection

def geo_locations():
    connection=connect()
    mylist=connection.distinct("GEO")
    return mylist

def fetch_data_mongo(location):

    collection=connect()
    start=time.time()
    list_m=list(collection.find({"GEO":location},{"_id":0,"UOM_ID":0,"SCALAR_ID":0,"DGUID":0,"TERMINALS":0,"SYMBOL":0,"DECIMALS":0,"VECTOR":0,"COORDINATE":0,"UOM":0}))
    # for post in (collection.find({"GEO":location},{"_id":0,"UOM_ID":0,"SCALAR_ID":0,"DGUID":0,"TERMINALS":0,"SYMBOL":0,"DECIMALS":0,"VECTOR":0,"COORDINATE":0,"UOM":0})):
    #     list_m.append(post)
    end=time.time()
    return [json.dumps(list_m),('%.3f'%(end-start))]
fetch_data_mongo("Canada")





