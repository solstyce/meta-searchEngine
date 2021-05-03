import requests
from bs4 import BeautifulSoup

def Google(search, userAgent):
    # Pagination KO à revoir
    URL = ('https://google.com/search?q=' + search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
       
        for i in soup.find_all('div', {'class' : 'yuRUbf'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    else:
        print('HTTP Response Status For Google : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(results)

def Duckduckgo(search , userAgent, nbPages):
    baseURL = ('https://duckduckgo.com/html/?q=' + search+'&p=0')
    headers = {'user-agent' : userAgent}
#    request = requests.get(URL, headers=headers)

    results = []
    for i in range(0,nbPages):
        url=f"{baseURL}&p={i}"
        print(f"URL applée : {url}")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')

            for i in soup.find_all('a', attrs={'class':'result__a'}):
                links = i['href']
                results.append(links)
        else:
            print('HTTP Response Status For Duckduckgo : {}'.format(httpResponseStatusCodes.get(request.status_code)))
            results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))


    print(results)
    print("nb resultats :" + str(len(results)))
    return(results)

def Givewater(search, userAgent):
    URL = ('https://search.givewater.com/serp?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')

        for i in soup.find_all('div', {'class' : 'web-bing__result'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    else:
        print('HTTP Response Status For Givewater : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(results)

def Ecosia(search, userAgent):
    URL = ('https://www.ecosia.org/search?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

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

def Bing(search, userAgent):
    URL = ('https://www.bing.com/search?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, "html.parser")

        for i in soup.find_all('li', {'class' : 'b_algo'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    else:
        print('HTTP Response Status For Bing : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(results)

def Yahoo(search, userAgent):
    URL = ('https://search.yahoo.com/search?q=' + search)
    request = requests.get(URL)

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
    
        for i in soup.find_all(attrs={"class": "ac-algo fz-l ac-21th lh-24"}):
            link = i.get('href')
            results.append(link)
    else:
        print('HTTP Response Status For Yahoo : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        
    return(results)
