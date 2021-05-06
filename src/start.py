from asset.search import * 
import logging

m = multipleSearch()
m.setMetasearchLogConfig('logs/test.log',logging.debug)
id=m.SearchAll("Mélenchon est un gros naze",50)
m.organize(id)
#m.displayorganizedResults()
#m.displayAll()