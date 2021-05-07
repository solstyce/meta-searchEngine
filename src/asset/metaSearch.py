import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlencode, urljoin, urlparse, quote



def setlogConfig(fileName,logLevel):
    logging.basicConfig(filename=fileName, level=logLevel)
    

#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')
#logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
#
#
#

httpResponseStatusCodes = {
    100 : 'Continue',
    101 : 'Switching Protocol',
    102 : 'Processing (WebDAV)',
    103 : 'Early Hints',
    201 : 'Created',
    202 : 'Accepted',
    203 : 'Non-Authoritative Information',
    204 : ' No Content',
    205 : 'Reset Content',
    206 : 'Partial Content',
    207 : 'Multi-Status (WebDAV)',
    208 : 'Already Reported (WebDAV)',
    226 : 'IM Used (HTTP Delta encoding)',
    300 : 'Multiple Choice',
    301 : 'Moved Permanently',
    203 : 'Found',
    303 : 'See Other',
    304 : 'Not Modified',
    305 : 'Use Proxy',
    306 : 'unused',
    307 : 'Temporary Redirect',
    308 : 'Permanent Redirect',
    400 : 'Bad Request',
    401 : 'Unauthorized',
    402 : 'Payment Required',
    403 : 'Forbidden',
    404 : 'Not Found',
    405 : 'Method Not Allowed',
    406 : 'Not Acceptable',
    407 : 'Proxy Authentication Required',
    408 : 'Request Timeout',
    409 : 'Conflict',
    410 : 'Gone',
    411 : 'Length Required',
    412 : 'Precondition Failed',
    413 : 'Payload Too Large',
    414 : 'URI Too Long',
    415 : 'Unsupported Media Type',
    416 : 'Range Not Satisfiable',
    417 : 'Expectation Failed',
    418 : 'I am a teapot',
    421 : 'Misdirected Request',
    422 : 'Unprocessable Entity (WebDAV)',
    423 : 'Locked (WebDAV)',
    424 : 'Failed Dependency (WebDAV)',
    425 : 'Too Early',
    426 : 'Upgrade Required',
    428 : 'Precondition Required',
    429 : 'Too Many Requests',
    431 : 'Request Header Fields Too Large',
    451 : 'Unavailable For Legal Reasons',
    500 : 'Internal Server Error',
    501 : 'Not Implemented',
    502 : 'Bad Gateway',
    503 : 'Service Unavailable',
    504 : 'Gateway Timeout',
    505 : 'HTTP Version Not Supported',
    506 : 'Variant Also Negotiates',
    507 : 'Insufficient Storage (WebDAV)',
    508 : 'Loop Detected (WebDAV)',
    510 : 'Not Extended',
    511 : 'Network Authentication Required'
}

def Google(search, userAgent,targetNbResults):
    # Pagination KO à revoir
    baseURL = ('https://google.com/search?q=' + quote(search))
    headers = {'user-agent' : userAgent}
    logging.info(f"start Google Research : {search} - Nb result {targetNbResults}")
    currentNbResults=0
    loop=1
    results = []
    while (currentNbResults < targetNbResults and loop < (targetNbResults + 2)) :
        url=f"{baseURL}&start={loop}"
        logging.info(f"URL appelée : {url}")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')
        
            for i in soup.find_all('div', {'class' : 'yuRUbf'}):
                link = i.find_all('a')
                links = link[0]['href']
                results.append(links)
        else:
            print('HTTP Response Status For Google : {}'.format(httpResponseStatusCodes.get(request.status_code)))
            results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
           
        currentNbResults=len(results) 
        logging.info(f"nb Results : {currentNbResults}")
        #print(f"nb : {currentNbResults}")   
        if loop == 1:
            loop=10
        else:
            loop=loop+10    


    return(results)


def Duckduckgo(search , userAgent, targetNbResults):
    baseURL = ('https://duckduckgo.com/html/?q=' + quote(search))
    headers = {'user-agent' : userAgent}
    logging.info(f"start Duck Duck Go Research : {search} - Nb result {targetNbResults}")
    currentNbResults=0
    loop=0
    results = []

    while (currentNbResults < targetNbResults and loop < (targetNbResults/10 + 2)):
        url=f"{baseURL}&p={loop}"
        #print(f"URL appelée : {url}")
        logging.info(f"URL appelée : {url}")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')

            for i in soup.find_all('a', attrs={'class':'result__a'}):
                links = i['href']
                results.append(links)
        else:
            print('HTTP Response Status For Duckduckgo : {}'.format(httpResponseStatusCodes.get(request.status_code)))
            results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        currentNbResults=len(results)    
        loop=loop+1
    #print(results)
    #print("nb resultats :" + str(len(results)))
    logging.info(f"nb Results : {currentNbResults}")
    return(results[0:targetNbResults])

def Givewater(search, userAgent, targetNbResults):
    baseUrl = ('https://search.givewater.com/serp?q='+quote(search))
    headers = {'user-agent' : userAgent}
    logging.info(f"start GiveWater Research : {search} - Nb result {targetNbResults}")
    currentNbResults=0
    loop=0
    results = []
    while (currentNbResults < targetNbResults and loop < (targetNbResults/10 + 2)):
        url=f"{baseUrl}&page={loop}"
        logging.info(f"URL appelée : {url}")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')

            for i in soup.find_all('div', {'class' : 'web-bing__result'}):
                link = i.find_all('a')
                links = link[0]['href']
                results.append(links)
        else:
            print('HTTP Response Status For Givewater : {}'.format(httpResponseStatusCodes.get(request.status_code)))
            results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        loop=loop+1
        currentNbResults=len(results)    
    #print(results)
    #print("nb resultats :" + str(len(results)))
    logging.info(f"nb Results : {currentNbResults}")
    return(results[0:targetNbResults])



def Ecosia(search, userAgent, targetNbResults):
    baseUrl = ('https://www.ecosia.org/search?p=2&q='+quote(search))
    headers = {'user-agent' : userAgent}
    request = requests.get(baseUrl, headers=headers)
    logging.info(f"start Ecosia Research : {search} - Nb result {targetNbResults}")
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
       
        for i in soup.find_all('div', {'class' : 'result-firstline-container'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    else:
        print('HTTP Response Status For Ecosia : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(results)

def Bing(search, userAgent, targetNbResults):
    baseUrl = ('https://www.bing.com/search?q='+quote(search))
    headers = {'user-agent' : userAgent}
    logging.info(f"start Bing Research : {search} - Nb result {targetNbResults}")
    currentNbResults=0
    loop=1
    results = []
    
    while (currentNbResults < targetNbResults and loop < (targetNbResults + 2) ):
        url=f"{baseUrl}&first={loop}"
        logging.info(f"URL appelée : {url}")

        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, "html.parser")

            for i in soup.find_all('li', {'class' : 'b_algo'}):
                link = i.find_all('a')
                links = link[0]['href']
                results.append(links)
        else:
            print('HTTP Response Status For Bing : {}'.format(httpResponseStatusCodes.get(request.status_code)))
            results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        if loop == 1:
            loop=10
        else:
            loop=loop+10    
        currentNbResults=len(results)
    logging.info(f"nb Results : {currentNbResults}")
    return(results[0:targetNbResults])

def Yahoo(search, userAgent, targetNbResults):
    baseURL = ('https://search.yahoo.com/search?q=' + quote(search))
    logging.info(f"start Yahoo Research : {search} - Nb result {targetNbResults}")
    headers = {'user-agent' : userAgent}
    currentNbResults=0
    loop=1
    results = []

    while (currentNbResults < targetNbResults and loop < (targetNbResults + 2)):
        url=f"{baseURL}&b={loop}"
        logging.info(f"URL appelée : {url}")
        request = requests.get(url, headers=headers)
    
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')
            for i in soup.find_all(attrs={"class": "ac-algo fz-l ac-21th lh-24"}):
                link = i.get('href')
                ru = link.find('RU=')
                rk = link.find('RK=')
                processedLink=link[ru+3:rk-1]
                processedLink=unquote(processedLink)
                results.append(processedLink)
        else:
            print('HTTP Response Status For Yahoo : {}'.format(httpResponseStatusCodes.get(request.status_code)))
            results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        loop=loop+10
        currentNbResults=len(results)    
    #print(results)
    #print("nb resultats :" + str(len(results)))
    logging.info(f"nb Results : {currentNbResults}")
    return(results[0:targetNbResults])
