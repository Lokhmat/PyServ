import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from Ad import Ad

class Parser:
    def get_page(self,url, num):
        #num is for defining with which ad to start     
        headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
        }



        

        site = requests.get('https://www.avito.ru/moskva',headers = headers, proxies = proxies, allow_redirects=False)
        bs = BeautifulSoup(site.text,"html.parser")
        needed = bs.findAll("div",class_="description item_table-description")
        Useful = [needed[k],needed[k+1],needed[k+2]]
        Ans = []
        for useful in Useful:
            bs1 = BeautifulSoup(str(useful),"html.parser")
            name = bs1.findAll("a",class_="snippet-link")
            temp = name
            name = str(str(name).split('>')[1])[:-3]
            bs2 = BeautifulSoup(str(useful), "html.parser")
            price = bs2.findAll("span",class_="snippet-price")
            price = str(str(price).split('>')[1])[2:-9]
            link ='https://www.avito.ru' + str(str(temp).split('"')[3])
            ans = [name,price,link]
            Ans.append(ans)
        return Ans