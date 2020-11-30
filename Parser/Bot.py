from User import User
from Parser import Parser
from Ad import Ad
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
        






if __name__=="__main__":
    bot = Bot()
    t=Parser.get_page(bot.users[0].links[0],0,bot.users[0])
    for e in t:
        print(e)