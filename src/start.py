from asset.search import * 
import logging
import time

#print(logging.DEBUG) => 10
#print(logging.ERROR) => 40
#print(logging.INFO) => 20
#print(logging.WARNING) => 30
#print(logging.CRITICAL) => 50


with open("basefile/search.csv",'r', encoding='utf8') as f:
    for line in f.readlines():
        
        m = multipleSearch()
        print(f"searchAll : {line}")
        m.setMetasearchLogConfig('logs/test.log',10)
        id=m.SearchAll(line,50)
        m.organize(id)
        #sleep pour éviter de se faire jeter par duck duck go pour spam ^_^
        print("start sleeping for 60s")
        time.sleep(10)
       # print("continue sleeping for 60s")
       # time.sleep(60)
       # print("continue sleeping for 60s")
       # time.sleep(60)
       # print("continue sleeping for 60s")
        


#m.displayorganizedResults()
#m.displayAll()