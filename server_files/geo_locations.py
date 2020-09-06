__author__ = 'Harsh'
import threading
import mongo_connect
main_list=[]
def get_geo(a,b):
    print('thread start'+str(a)+" "+str(b))
    connection=mongo_connect.connect()
    mylist=[]
    for post in range(a,b):
        mylist.append(connection.find()[post]["GEO"])
    mylist=list(dict.fromkeys(mylist))
    main_list.extend(mylist)
    #print(main_list)
    return main_list

a=0
b=10
threads=list()
while(b!=100):
    x=threading.Thread(target=get_geo,args=(a,b))
    print(x)
    threads.append(x)
    a=a+10
    b=b+10
    x.start()

print(main_list)