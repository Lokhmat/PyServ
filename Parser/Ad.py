class Ad():
    def __init__(self, name,description,price, link, views):
        self.name = name
        self.description = description
        self.price = price
        self.link = link
        self.views = views
    
print(Ad("as","asdf", 111,"asdf",12))