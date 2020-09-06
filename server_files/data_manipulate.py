__author__ = 'Harsh'
def csv_encode():
    import csv
    path =  'metadata.csv'
    with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open(path + '-utf8.csv', 'w') as outfile:
         inputs = csv.reader(infile)
         output = csv.writer(outfile)
         for index, row in enumerate(inputs):
             if index == 0:
                 continue
             output.writerow(row)
             print(row)

def mongo_data_clean():
    from pymongo import MongoClient
    connection = MongoClient('localhost',27017)
    db=connection.job_vacancy_revised
    collection=db.data
    collection.update_many({"SCALAR_ID":3},{"$set":{"$mul": { "$toint":{"VALUE":1000}}}})
    #for post in collection.find({},{"_id":0})[0:10]:
    #     if(post["SCALAR_FACTOR"]=="thousands"):
    #         collection.find({},{ $set:{}})
mongo_data_clean()