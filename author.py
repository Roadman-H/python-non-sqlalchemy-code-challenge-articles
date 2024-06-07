def _init_(self, name):
        self._name = None
        self.name = name
        
    def get_name(self):
        return self._name
    def set_name(self, name):
        if self._name is not None:
            return
        elif type(name) is not str or len(name) == 0:
            return
        self._name = name
    name = property(get_name, set_name)
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
         new_article = Article(self, magazine, title)
         return new_article
    def topic_areas(self):
        if len(self.articles()) == 0:
             return None
        else:
          return list(set(article.magazine.category for article in self.articles()))
        
