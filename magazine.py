from article import Article
from author import Author

class Magazine:
    _all_magazines = []  
    def __init__(self, name, category):
      
        if not isinstance(name, str) or not isinstance(category, str) or len(name) < 2 or len(name) > 16 or len(
                category) == 0:
            raise ValueError("Name must be a string between 2 and 16 characters, and category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []  
        Magazine._all_magazines.append(self)  


    @property
    def name(self):
        return self._name
   
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category
    
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value    

   
    def articles(self):
        return self._articles

    
    def contributors(self):
        
        return list(set(article.author for article in self._articles if isinstance(article.author, Author)))

    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

   
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
       
        return [author for author, count in author_counts.items() if count > 2]
    

   
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))