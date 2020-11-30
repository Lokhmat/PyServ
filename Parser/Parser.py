import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from Ad import Ad

class Parser:
    def get_page(url, num, user):
        #num is for defining with which ad to start     
        headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
        }
        proxies = {
            'http' : user.proxies[int(user.proxies[0])]
        }
        if(int(user.proxies[0])+1==len(user.proxies)):
            user.proxies[0] = '1'
        else:
            user.proxies[0] = str((int(user.proxies[0]) + 1))
        site = requests.get(url,headers = headers, proxies = proxies, allow_redirects=False)
        bs = BeautifulSoup(site.text,"html.parser")
        needed = bs.select('div[class*="iva-item-body-"]')
        Useful = [needed[num],needed[num+1],needed[num+2]]
        Ans = []
        for useful in Useful:
            bs1 = BeautifulSoup(str(useful),"html.parser")
            name = bs1.findAll("span",itemprop="name")
            price = bs1.select('span[class*="price-text-"]')
            temp = bs1.select('a[class*="link-link-"]')
            name = str(str(name).split('>')[1])[:-6]
            price = str(str(price).split('>')[1])[:-7]
            print(temp)
            link ='https://www.avito.ru' + str(str(temp).split('href="')[1].split('" itemprop')[0])
            ans = Ad(name,price,link,-1)
            Ans.append(ans)
        return Ans