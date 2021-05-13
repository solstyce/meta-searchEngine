import requests
from urllib.parse import unquote, urlencode, urljoin, urlparse, quote
from bs4 import BeautifulSoup
import pymongo

myclient = pymongo.MongoClient("mongodb://metadmin:metaPWD.2@146.59.234.152:27015/")
mydb = myclient["metasearch"]
myCollection = mydb["research"]
disc = {"ZIZI":"caca"}
r= myCollection.insert_one(disc)
print(r)

