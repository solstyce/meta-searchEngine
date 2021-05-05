
import asset.metasearch
import json

class multipleSearch:
    def __init__(self):
        print("beginning")
        self.googleLink=[]
        self.duckLink=[]
        self.giveWaterLink=[]
        self.ecosiaLink=[]
        self.bingLink=[]
        self.yahooLink=[]
        self.organizedResults={} # link list organized by search engine without any modification
        self.classedbyLink=[] #link list with search engin indexes
        self.userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"
    def googleSearch(self,content,nb):
        self.googleLink = asset.metasearch.Google(content, self.userAgent,nb)    
    def duckSearch(self,content,nb):
       self.duckLink=asset.metasearch.Duckduckgo(content, self.userAgent,nb)
    def givewaterSearch(self,content,nb):
        self.giveWaterLink=asset.metasearch.Givewater(content, self.userAgent,nb)
    def ecosiaSearch(self,content,nb):
        self.ecosiaLink=asset.metasearch.Ecosia(content, self.userAgent,nb)
    def bingSearch(self,content,nb):
        self.bingLink=asset.metasearch.Bing(content, self.userAgent,nb)
    def yahooSearch(self,content,nb):
        self.yahooLink=asset.metasearch.Bing(content, self.userAgent,nb)
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

    def displayorganizedResults(self):
        print("Raw Results")
        print(self.organizedResults) # link list organized by search engine without any modification
        print("Links organized")
        print(self.classedbyLink) #link list with search engin indexes
    def SearchAll(self,content,nb):
        self.googleSearch(content,nb)
        self.duckSearch(content,nb)
        self.givewaterSearch(content,nb)
        self.ecosiaSearch(content,nb)
        self.bingSearch(content,nb)
        self.yahooSearch(content,nb)
       
    def organize(self):
        #Organize all Data in one global object
        #points are : 
        #1 : storing link organized by search engin
        #2 : listing all link with related search engin with index number

        #1 : 
        self.organizedResults["google"]=self.googleLink
        self.organizedResults["duckduckgo"]=self.duckLink
        self.organizedResults["givewater"]=self.giveWaterLink
        self.organizedResults["ecosia"]=self.ecosiaLink
        self.organizedResults["bing"]=self.bingLink
        self.organizedResults["yahoo"]=self.yahooLink
        #print(self.organizedResults)
        #print(json.dumps(self.organizedResults))
        #2 : merge lists
        tmp_list = self.googleLink+self.duckLink+self.giveWaterLink+self.ecosiaLink+self.bingLink+self.yahooLink
        #print(f"nb tmp : {len(tmp_list)}")
        tmp_list=set(tmp_list)
        #print(f"nb tmp : {len(tmp_list)}")
        tmp_list=list(tmp_list)
        for i in tmp_list:
            print(f"link : {i}")
            #search link in Google List
            #self.googleLink
            result = {}
            result['link']=i
            result['search']=[]
            if i in self.googleLink:
                googleIndex=self.googleLink.index(i)
                result['search'].append({'google':googleIndex})
                #print(f" google index : {googleIndex}")

            if i in self.duckLink:
                duckIndex=self.duckLink.index(i)
                result['search'].append({'duckduckgo':duckIndex})
                #print(f" duck duck go index : {duckIndex}")

            if i in self.giveWaterLink:
                giveWaterIndex=self.giveWaterLink.index(i)
                result['search'].append({'givewater':giveWaterIndex}) 
                #print(f" givewater index : {giveWaterIndex}")

            if i in self.ecosiaLink:
                ecosiaIndex=self.ecosiaLink.index(i)
                result['search'].append({'ecosia':ecosiaIndex})    
                #print(f" ecosia index : {ecosiaIndex}")   
            
            if i in self.bingLink:
                bingIndex=self.bingLink.index(i)
                result['search'].append({'bing':bingIndex})
                #print(f" bing index : {bingIndex}")

            if i in self.yahooLink:
                yahooIndex=self.yahooLink.index(i)
                result['search'].append({'yahoo':yahooIndex})
                #print(f" yahoo index : {yahooIndex}")
     
            self.classedbyLink.append(result)

    
       
    
        
    
        
    
        
    
        
        
 