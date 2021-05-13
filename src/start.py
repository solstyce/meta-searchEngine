from asset.search import * 
import logging

m = multipleSearch()
#print(logging.DEBUG) => 10
#print(logging.ERROR) => 40
#print(logging.INFO) => 20
#print(logging.WARNING) => 30
#print(logging.CRITICAL) => 50
m.setMetasearchLogConfig('logs/test.log',10)
id=m.SearchAll("Mélenchon est un gros naze",5)
m.organize(id)
#m.displayorganizedResults()
#m.displayAll()