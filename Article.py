class Article():
    '''
    Class to describe an article - containing:
    guid
    title
    description
    pubDate
    link
    '''

    def __init__(self, guid, title, description, pubDate, link):
        self.guid = guid
        self.title = title
        self.description = description
        self.pubDate = pubDate
        self.link = link

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)