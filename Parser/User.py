import requests



class User():
    def __init__(self, id, token, proxies, links):
        self.id = id
        self.token = token
        self.proxies = proxies
        self.links = links
        self.ads = [[]*len(links)]
    def send(self,ad,token):
        params = {'chat_id': str(self.token), 'text': str(ad)}
        adm_params = {'chat_id': '399868860', 'text': str(ad)}
        method = 'sendMessage'
        #print(params)
        try:
            resp = requests.post(token + method, params)
            adm_resp = requests.post(token + method, adm_params)
            return resp.text
        except Exception as e:
            print(e)
            return 1
    def send_text(self,text, token):
        params = {'chat_id': str(self.token), 'text': text}
        params = {'chat_id': '399868860', 'text': text}
        method = 'sendMessage'
        #print(params)
        try:
            resp = requests.post(token + method, params)
            adm_resp = requests.post(token + method, adm_params)
            return resp.text
        except Exception as e:
            print(e)
            return 1
    def clean():
        pass

