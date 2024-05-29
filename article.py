class Article:
    def __init__(self, author, magazine, title):
        
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    
    @property
    def author(self):
        return self._author

    
    @property
    def magazine(self):
        return self._magazine