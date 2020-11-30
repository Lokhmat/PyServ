import requests

class User():
    def __init__(self, id, token, proxies, links):
        self.id = id
        self.token = token
        self.proxies = proxies
        self.links = links

