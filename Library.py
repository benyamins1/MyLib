import json
from Book import Book
from Customer import Customer
from Loan import Loan
from LibraryExceptions import NotFoundError, CantLoanError
from datetime import datetime, timedelta
import os

def load(file_name):
    if os.path.exists(file_name) == False:
        return []
    
    data = None
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def save(file_name, data):
    with open(file_name, 'w') as f:
        json.dump([obj.__dict__ for obj in data], f, default=str)


class Library:
    def __init__(self, books_file="books.json", customers_file="customers.json",loans_file="loans.json"):
        self.books_file = books_file
        self.customers_file = customers_file
        self.loans_file=loans_file
        self.books: list[Book] = self.load_books()
        self.customers: list[Customer] = self.load_customers()
        self.loans: list[Loan] = self.load_loans()

#============================================================LOAD============================================================
    def load_books(self):
        lst = load(self.books_file)
        self.books = []
        for item in lst:
            self.books.append( Book(**item) )
        return self.books
    def load_customers(self):
        lst = load(self.customers_file)
        self.customers = []
        for item in lst:
            self.customers.append( Customer(**item) )
        return self.customers
    def load_loans(self):
        lst = load(self.loans_file)
        self.loans = []
        for item in lst:
            item["loan_date"] = datetime.strptime(item["loan_date"], "%Y-%m-%d %H:%M:%S.%f")
            if item["return_date"] != None:
                item["return_date"] = datetime.strptime(item["return_date"], "%Y-%m-%d %H:%M:%S.%f")
            self.loans.append( Loan(**item) )
        return self.loans
    
#============================================================SAVE============================================================
    def save_books(self):
        save(self.books_file, self.books)
    def save_customers(self):
        save(self.customers_file, self.customers)
    def save_loans(self):
        save(self.loans_file, self.loans)

#============================================================ADD============================================================
    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        self.save_customers()

    def add_loan(self, loan: Loan):
        self.loans.append(loan)
        self.save_loans()

#============================================================REMOVE============================================================
    def remove_book(self, book_id: int):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
    
    def remove_customer_by_id(self, id: int):
        for customer in self.customers:
            if customer.id == id:
                self.customers.remove(customer)
                return
            
    def display_customers(self):
        print(self.customers)
    def display_books(self):
        print(self.books)
    def display_loans(self):
        print(self.loans)

    def display_late_loans(self): #!
        for loan in self.loans:
            book = self.find_book_by_id(loan.book_id)
            if loan.return_date != None and loan.return_date > loan.loan_date + book.get_loan_time():
                print(str(loan) + " (Not Active)")
            elif loan.loan_date + book.get_loan_time() < datetime.now():
                print(str(loan) + " (Active)")

    def find_customer_by_name(self, name: str) -> Customer | None:
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None
    
    def find_book_by_name(self, name: str) -> Book | None:
        for book in self.books:
            if book.name == name:
                return book
        return None
    
    def find_customer_by_id(self, id: int) -> Customer | None:
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None
    
    def find_book_by_id(self, id: int) -> Book | None:
        for book in self.books:
            if book.id == id:
                return book
        return None
    


    def loan_a_book(self, customer_id: int, book_id: int):
        cus = self.find_customer_by_id(customer_id)
        book = self.find_book_by_id(book_id)
        if cus == None or book == None:
            raise NotFoundError
        
        for loan in self.loans:
            if loan.book_id == book_id and loan.return_date == None:
                raise CantLoanError
            
        loan = Loan(customer_id, book_id)
        self.loans.append(loan)
        self.save_loans()

    def return_a_book(self, book_id: int):
        book = self.find_book_by_id(book_id)
        if book == None:
            raise NotFoundError
        
        for loan in self.loans:
            if loan.book_id == book_id and loan.return_date == None:
                loan.return_loan()
                self.save_loans()
                return
        raise NotFoundError
        