class Ad():
    def __init__(self, name,description,price, link, views):
        self.name = name
        self.description = description
        self.price = price
        self.link = link
        self.views = views
    def __eq__(self,other):
        return self.link[-10:]==other.link[-10:]
        