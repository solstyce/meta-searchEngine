from asset.search import * 
import datetime
import time
import logging

#print(logging.DEBUG) => 10
#print(logging.ERROR) => 40
#print(logging.INFO) => 20
#print(logging.WARNING) => 30
#print(logging.CRITICAL) => 50


fileName=f"logs/{datetime.datetime.today()}-execution.logs"
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y:%H:%M:%S', level=10, filename=fileName)
logging.debug("local Config Init OK !")

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

with open("basefile/search.csv",'r', encoding='utf8') as f:
    for line in f.readlines():
        m = multipleSearch()
        #m.setMetasearchLogConfig('testprout.log',10)
        m.log("debut recherche {line}")
        m.connect_vpn()
        print(f"searchAll : {line}")
        m.setRandomUserAgent()
        id=m.SearchAll(line,20)
        m.organize(id)
        #sleep pour éviter de se faire jeter par duck duck go pour spam ^_^
        print("start sleeping for 10s")
        time.sleep(10)
        m.disconnect_vpn()
       
       # print("continue sleeping for 60s")
       # time.sleep(60)
       # print("continue sleeping for 60s")
       # time.sleep(60)
       # print("continue sleeping for 60s")
        


#m.displayorganizedResults()
#m.displayAll()