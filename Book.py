from datetime import datetime, timedelta
import json

class Book:
    def __init__(self, id: int, name: str, author: str, year_published: datetime, type: int):
        self.id = id
        self.name = name
        self.author = author
        self.year_published = year_published
        self.type = type
#===============================PERIOD LOAD===================================================================================
    def get_loan_time(self):
        if self.type == 1:
            return timedelta(days=10)
        elif self.type == 2:
            return timedelta(days=5)
        elif self.type == 3:
            return timedelta(days=2)

    def add_book(self, id, title, author):
        book = Book(id, title, author, True)
        self.books.append(book)
        self.save_books()
    
    def remove_book(self, id):
        book = self.get_book(id)
        if book:
            self.books.remove(book)
            for customer in self.customers:
                if book in customer.books:
                    customer.books.remove(book)
            self.save_books()
            self.save_customers()
    
    def get_book(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None   
    
    def __str__(self) -> str:
        return "ID: " + str(self.id) + " Name: " + self.name + " Author: " + self.author + " Year published: " + str(self.year_published) + " Type: " + str(self.type )
    
    def __repr__(self) -> str:
        return self.__str__()
    
all_books: list[Book] = []

def get_book(id: int):
    for book in all_books:
        if book.id == id:
            return book
    return None
print("for test github")