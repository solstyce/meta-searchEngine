from ScrapeSearchEngine.SearchEngine import Google
from ScrapeSearchEngine.SearchEngine import Duckduckgo
from ScrapeSearchEngine.SearchEngine import Givewater
from ScrapeSearchEngine.SearchEngine import Ecosia
from ScrapeSearchEngine.SearchEngine import Bing
from ScrapeSearchEngine.SearchEngine import Yahoo

from googlesearch import search
#import ddg3
from duckduckpy import query


class multipleSearch:
    def __init__(self):
        print("beginning")
        self.googleText=[]
        self.googleLink=[]
        self.duckText=[]
        self.duckLink=[]
        self.giveWaterText=[]
        self.giveWaterLink=[]
        self.ecosiaText=[]
        self.ecosiaLink=[]
        self.bingText=[]
        self.bingLink=[]
        self.yahooText=[]
        self.yahooLink=[]
    def googleSearch(self,content):
        self.googleLink = search(content, num_results=100)    
    def duckSearch(self,content):
       # r= ddg3.query('toto')
       # print("DUCK DUCK GO : ")
       # tmp = query(content)
        #print(tmp)
       # print("Résultats !")
       # topics = tmp.related_topics

        #print(topics.type)
        #for i in topics:
         #   print("===================>")
          #  print(i)
        #self.duckLink = 
        #print("todo")
        self.duckText, self.duckLink=Duckduckgo(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")
    def givewaterSearch(self,content):
        print("todo")
    def ecosiaSearch(self,content):
        print("todo")
    def bingSearch(self,content):
        print("todo")
    def yahooSearch(self,content):
        print("todo")
    def displayAll(self):
        
        print("google")
        print(self.googleLink)
        print(self.googleText)

        print("******************************************")
        print("duck duck go :")
        print(self.duckLink)
        print(self.duckText)

        print("******************************************")
        print("givewater :")
        print(self.giveWaterLink)
        print(self.giveWaterText)

        print("******************************************")
        print("Ecosia :")
        print(self.ecosiaLink)
        print(self.ecosiaText)

        print("******************************************")
        print("Bing :")
        print(self.bingLink)
        print(self.bingText)

        print("******************************************")
        print("Yahoo :")
        print(self.yahooLink)
        print(self.yahooText)

    def SearchAll(self,content):
        self.googleSearch(content)
        self.duckSearch(content)
       # self.googleText, self.googleLink=Google(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.duckText, self.duckLink=Duckduckgo(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.giveWaterText, self.giveWaterLink=Givewater(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.ecosiaText, self.ecosiaLink=Ecosia(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.bingText, self.bingLink=Bing(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.yahooText, self.yahooLink=Yahoo(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")
    def organize():
        print("todo")
 