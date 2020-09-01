# IS211 Assignment1 Part2
#Simple Class


class Book:
    author = ""
    title  = ""

    def __init__(self,author,title):
        self.author = author
        self.title  = title

    def display(self):
        print (self.title, "written by", self.author)

