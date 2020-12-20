class Ad():
    def __init__(self, name,price, link, views):
        self.name = name
        self.price = price
        self.link = link
        self.views = views
    def __eq__(self,other):
        return self.link[-30:]==other.link[-30:]
    def __str__(self):
        return '%s \n%s \n%s \n%s'%(self.name,self.price,self.link,self.views)
        