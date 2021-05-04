#from ScrapeSearchEngine.SearchEngine import Google
#from ScrapeSearchEngine.SearchEngine import Duckduckgo
#from ScrapeSearchEngine.SearchEngine import Givewater
#from ScrapeSearchEngine.SearchEngine import Ecosia
#from ScrapeSearchEngine.SearchEngine import Bing
#from ScrapeSearchEngine.SearchEngine import Yahoo

import asset.metasearch

#from googlesearch import search
#import ddg3
#from duckduckpy import query


class multipleSearch:
    def __init__(self):
        print("beginning")
        self.googleLink=[]
        self.duckLink=[]
        self.giveWaterLink=[]
        self.ecosiaLink=[]
        self.bingLink=[]
        self.yahooLink=[]
        self.userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"
    def googleSearch(self,content):
        self.googleLink = asset.metasearch.Google(content, self.userAgent,100)    
    def duckSearch(self,content):
       self.duckLink=asset.metasearch.Duckduckgo(content, self.userAgent,100)
    def givewaterSearch(self,content):
        self.giveWaterLink=asset.metasearch.Givewater(content, self.userAgent,100)
    def ecosiaSearch(self,content):
        self.ecosiaLink=asset.metasearch.Ecosia(content, self.userAgent,100)
    def bingSearch(self,content):
        self.bingLink=asset.metasearch.Bing(content, self.userAgent,100)
    def yahooSearch(self,content):
        self.yahooLink=asset.metasearch.Bing(content, self.userAgent,100)
    def displayAll(self):
        
        print("google")
        print(self.googleLink)

        print("******************************************")
        print("duck duck go :")
        print(self.duckLink)

        print("******************************************")
        print("givewater :")
        print(self.giveWaterLink)

        print("******************************************")
        print("Ecosia :")
        print(self.ecosiaLink)

        print("******************************************")
        print("Bing :")
        print(self.bingLink)

        print("******************************************")
        print("Yahoo :")
        print(self.yahooLink)

    def SearchAll(self,content):
        self.googleSearch(content)
        self.duckSearch(content)
        self.givewaterSearch(content)
        self.ecosiaSearch(content)
        self.bingSearch(content)
        self.yahooSearch(content)
       # self.googleText, self.googleLink=Google(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.duckText, self.duckLink=Duckduckgo(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.giveWaterText, self.giveWaterLink=Givewater(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.ecosiaText, self.ecosiaLink=Ecosia(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.bingText, self.bingLink=Bing(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")

       # self.yahooText, self.yahooLink=Yahoo(content,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75")
    def organize():
        print("todo")
 