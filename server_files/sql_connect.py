__author__ = 'Harsh'
import mysql.connector
import time

def fetch_data_sql(location):

    connection = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='H@rsh7797sql',
                                 db='canada_job',
                                 charset='utf8mb4')
    start=time.time()
    cursor=connection.cursor()
    query="""SELECT `id`,`REF_DATE`,`GEO`,`Job vacancy statistics`,`North American Industry Classification System (NAICS)`, `VALUE`,`SCALAR_FACTOR`,
`STATUS`
FROM canada_job.main_data
INNER JOIN uom ON main_data.UOM_ID=uom.UOM_ID
INNER JOIN geo ON main_data.DGUID=geo.DGUID
INNER JOIN scalar ON main_data.SCALAR_ID=scalar.SCALAR_ID
where GEO='"""+location+"""' """

    #query="""select * from canada_job.result where GEO='"""+location+"""' """
    cursor.execute(query)
    data=cursor.fetchall()
    end = time.time()
    #for i in cursor:
    #    list.append(i)
    headings=['ID','REF_DATE','GEO','JOB VACANCY STATISTICS','NORTH AMERICAN INDUSTRY CLASSIFICATION SYSTEM (NAICS)', 'VALUE','SCALAR_FACTOR','STATUS']
    return [data,headings,('%.3f'%(end-start))]

