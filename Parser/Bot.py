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
        try:
            for user in self.users:
                user.send_text('Версия 0.2.1 запуск.',self.api_url)
        except Exception as e:
            print(e)
        while(True):
            try:
                for user in self.users:
                    for i in range(len(user.links)):
                        print(user.proxies)
                        pages = Parser.get_page(user.links[i],0,user)
                        for page in pages:
                            if(not (page in user.ads[i])):
                                user.ads[i].append(page)
                                user.send(page,self.api_url)
                            if(len(user.ads[i])>50):
                                user.ads[i]=user.ads[i][-5:]

            except Exception as e:
                print(e)
            time.sleep(3/(len(user.proxies)-1))

            
            

if __name__=="__main__":
    bot = Bot()
    bot.work()