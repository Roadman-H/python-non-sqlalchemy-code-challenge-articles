all = []


    def _init_(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    def get_title(self):
        return self._title
    def set_title(self, title):
        if type(title) is not str or len(title) == 0:
            return
        self._title = title
    title = property(get_title, set_titl