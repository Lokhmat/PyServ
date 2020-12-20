from User import User
from Parser import Parser
from Ad import Ad
import time
class Bot:
    token =  '1223014907:AAHQoqCh_RpBSFqBna8PvTi9j7yL9W6HDEY'
    api_url = 'https://api.telegram.org/bot{}/'.format(token)
    ads = []
    def __init__(self):
        lines = []
        self.users = []
        with open('users.txt', 'r') as file:
            lines = file.readlines()
        for line,i in zip(lines,range(len(lines))):
            proxies = []
            links = []
            with open('%s.txt' %line, 'r') as file:
                temp = file.read().splitlines()
            proxies = temp[:temp.index('-')]
            proxies.insert(0,'1')
            links = temp[temp.index('-')+1:]
            self.users.append(User(i,line,proxies,links))
    def work(self):
        while(True):
            try:
                for user in self.users:
                    for link in user.links:
                        print(user.proxies)
                        pages = Parser.get_page(link,0,user)
                        for page in pages:
                            if(not (page in user.ads)):
                                user.ads.append(page)
                #time.sleep(2.0/(len(user.proxies)-1))
                time.sleep(2)
            except Exception:
                print(Exception)

            
            

if __name__=="__main__":
    bot = Bot()
    bot.work()