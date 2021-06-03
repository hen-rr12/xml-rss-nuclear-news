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