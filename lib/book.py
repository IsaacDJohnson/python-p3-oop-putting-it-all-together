#!/usr/bin/env python3

class Book:

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __init__(self, title="title", page_count="count"):
        self.title = title
        self.page_count = page_count
        
    @property
    def title(self):
        """The title property"""
        return self._title


    @title.setter
    def title(self, title):
        self._title = title
        pass

    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count


    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) is int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
        pass

    pass
    
        