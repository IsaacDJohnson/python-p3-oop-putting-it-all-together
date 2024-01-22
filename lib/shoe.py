#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand ="brand", size= 0, condition = ""):
        self.brand = brand
        self.size = size
        self.condition = condition

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def brand(self):
        """The brand property"""
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        """the brand setter"""
        self._brand = brand

    @property
    def size(self):
        """the size property"""
        return self._size
        

    @size.setter
    def size(self, size):
        """the size setter"""
        if type(size) is int:
            self._size = size
        else:
            print("size must be an integer") 


    pass