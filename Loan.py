from datetime import datetime,timedelta,date
import Book
#===========================================LOAN=========================================================================================================================================
class Loan:
    def __init__(self, customer_id: int, book_id: int, loan_date = datetime.now(), return_date: datetime = None):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def return_loan(self):
        self.return_date = datetime.now()

    def calculate_return_date(self):
        book = Book.get_book(self.book_id)
        return self.loan_date + book.get_loan_time()
    
    def __str__(self) -> str:
        return "Customer ID: " + str(self.customer_id) + " Book ID: " + str(self.book_id) + " Loan Date: " + str(self.loan_date) + " Return Date: " + str(self.return_date)

    def __repr__(self) -> str:
            return self.__str__()
