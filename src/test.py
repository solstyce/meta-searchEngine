import requests
from bs4 import BeautifulSoup

def Duckduckgo(search , userAgent, nbPages):
    baseURL = ('https://duckduckgo.com/html/?q=' + search)
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

def Givewater(search, userAgent, nbPages):
    baseUrl = ('https://search.givewater.com/serp?q='+search)
    headers = {'user-agent' : userAgent}

    results = []
    for i in range(0,nbPages):
        url=f"{baseUrl}&page={i}"
        print(f"URL applée : {url}")
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
    print(results)
    print("nb resultats :" + str(len(results)))
    return(results)
    return(results)

#test = Duckduckgo("mélanchonest un naze","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75",10)


test = Givewater("mélanchon est un naze","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75",22)
