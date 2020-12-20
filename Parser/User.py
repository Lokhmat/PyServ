import requests



class User():
    def __init__(self, id, token, proxies, links):
        self.id = id
        self.token = token
        self.proxies = proxies
        self.links = links
        self.ads = []
    def send(self,ad,token):
        params = {'chat_id': str(self.token), 'text': str(ad)}
        method = 'sendMessage'
        print(params)
        try:
            resp = requests.post(token + method, params)
            return resp.text
        except Exception:
            print('failed to connect')
            return 1

