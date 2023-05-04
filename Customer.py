
class Customer:
    def __init__(self, id: int, name: str, city: str,age: int):
        self.id = id
        self.name = name
        self.city = city
        self.age=age
#======================================ADD CUSTOMER==============================================================================================     
    def get_customer(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None
    
    def add_customer(self, id,name):
        customer = Customer(id, name)
        self.books.append(customer)
        self.save_books()
#=====================================REMOVE CUSTOMER============================================================================================
    def remove_customer(self, id):
        customer = self.get_customer(id)
        if customer:
            self.customer.remove(customer)
            for customer in self.customers:
                if customer in customer.books:
                    customer.books.remove(customer)
            self.save_books()
            self.save_customers()   

    def __str__(self) -> str:
        return "ID: " + str(self.id) + " Name: " + self.name + " City: " + self.city + " age: " + str(self.age)
    
    def __repr__(self) -> str:
        return self.__str__()
    

all_customers: list[Customer] = []
def get_customer(id: int):
    for customer in all_customers:
        if customer.id == id:
            return customer
    return None
        