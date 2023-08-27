from models.customer import Customer
from models.review import Review
from models.restaurant import Restaurant

class TestCustomer:
    def test_create_customer(self):
        customer = Customer("john", "doe")
        assert customer != None
        assert customer._given_name == "john"
        assert customer._family_name == "doe"
        assert Customer.customer_count == [customer]
        
    def test_customer_given_name(self):
        """
        Test returns customer given name
        """    
        customer1 = Customer("john", "jones")
        assert customer1.given_name() == "john"
        
    def test_customer_family_name(self):
        """
        Tests returns customer's family name
        """    
        customer2 = Customer("John", "Doe")
        assert customer2.get_family_name() == "Doe"
        
    def test_customer_full_name(self):
        """
        Test returns customer's full name
        """    
        customer3 = Customer("Jack", "Daniels")
        assert customer3.full_name() == "Jack Daniels"
        
    def test_customer_all(Self):
        """
        Test returns all instances of customer class
        """    
        assert len(Customer.all()) == 4