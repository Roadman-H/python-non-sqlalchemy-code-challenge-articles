def _init_(self, name, category):
        self.name = name
        self.category = category
    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) is str and 2 <= len(name) <= 16:
            self._name = name

    name = property(get_name, set_name)

    def get_category(self):
        return self._category

    def set_category(self, category):
        if type(category)is str and len(category) > 0:
            self._category = category

    category = property(get_category, set_category)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        

    def contributors(self):
        return list(set([article.author for article in self.articles()]))
        
    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        return list(set([article.author for article in self.articles()]))