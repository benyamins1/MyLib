from Library import Library
from Book import Book
from Customer import Customer
from utils_lib import Main
    
lib = Library()
def add_customer():
    id = int(input("Enter customers' id"))
    name = input("Enter customers' name")
    city = input("Enter customers' city")
    age = int(input("Enter customers' age"))
    c = Customer(id, name, city, age)
    lib.add_customer(c)

def add_book():
    id = int(input("Enter books' id"))
    name = input("Enter books' name")
    author = input("Enter books' author")
    year_published = input("Enter books' publish date")
    type = int(input("Enter books' type"))
    b = Book(id, name, author, year_published, type)
    lib.add_book(b)

#===========================================MENU=====================================================================================================================================================================================================================================================================================
def main():
    while True:
        choices=int(input("ENTER YOUR CHOICE :\n(1)Add new book\n(2)Find book by name\n(3)Remove book\n(4)Diplay all book\n(5)Loan book\n(6)Return a loan book\n(7)Display late loan books\n(8)Display all loan\n(9)Add new customer\n(10)Remove customer by Id\n(11)Find customer by name\n(12)Display all customer\n") )  
        if choices==Main.Add_New_Book.value:
            add_book()

        elif choices==Main.Find_Book_By_Name.value:
            book_name = input("Enter books' name")
            b = lib.find_book_by_name(book_name)
            print(b)
                            
        elif choices==Main.Remove_Book.value:
            book_id=int(input("Enter book Id: "))
            lib.remove_book(book_id)        
        
        elif choices==Main.Loan_Book.value:
            customer_id=int(input("Enter your id"))
            book_id=int(input("Enter book Id"))          
            lib.loan_a_book(customer_id,book_id)       
        
        elif choices==Main. Add_New_Customer.value:
            add_customer()
        
        elif choices==Main. Remove_Customer_By_Id.value:
            id=int(input("Enter your Id name"))
            lib.remove_customer_by_id(id)
                    
        elif choices==Main.Display_All_Book.value:
            lib.display_books()
        
        elif choices==Main.Display_All_Loan.value:
            lib.display_loans()    
        
        elif choices==Main.Display_All_Customer.value:        
            lib.display_customers()    
        
        elif choices==Main.Return_a_Loan_book.value:
            book_id=int(input("Enter book Id"))
            lib.return_a_book(book_id)
        
        elif choices==Main.Display_Late_Loans.value:     
            lib.display_late_loans()
        
        elif choices==Main.Find_Customer_By_Name.value:
            lib.find_customer_by_id()
            

if __name__ == '__main__':
            main()


