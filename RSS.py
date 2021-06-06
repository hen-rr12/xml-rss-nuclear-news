class RSS:
    '''
    Class to describe an RSS channel feed - containing:
    title
    link
    description
    language
    '''

    def __init__(self, title, link, description, language):
        self.title = title
        self.link = link
        self.description = description
        self.language = language

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
