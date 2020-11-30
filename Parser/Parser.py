import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from Ad import Ad

class Parser:
    def get_page(url, num, proxies_list):
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
            'http' : proxies_list[int(proxies_list[0])]
        }
        proxies_list[0] = str((int(proxies_list[0]) + 1)%(len(proxies_list) - 1))
        site = requests.get(url,headers = headers, proxies = proxies, allow_redirects=False)
        bs = BeautifulSoup(site.text,"html.parser")
        needed = bs.findAll("div",class_="description item_table-description")
        print(needed)
        Useful = [needed[num],needed[num+1],needed[num+2]]
        Ans = []
        for useful in Useful:
            bs1 = BeautifulSoup(str(useful),"html.parser")
            name = bs1.findAll("a",class_="snippet-link")
            price = bs1.findAll("span",class_="snippet-price")
            temp = name
            name = str(str(name).split('>')[1])[:-3]
            price = str(str(price).split('>')[1])[2:-9]
            link ='https://www.avito.ru' + str(str(temp).split('"')[3])
            ans = Ad(name,price,link,-1)
            Ans.append(ans)
        return Ans