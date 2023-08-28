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
        
    def test_customer_set_given_name(self):
        """
        Tests for customer set given name
        """     
        customer = Customer("Jack", "Daoe")
        customer.set_given_name("Jax")
        assert customer.given_name() == "Jax"
        
    def test_customer_set_family_name(self):
        """
        Tests for customer set family name
        """     
        customer = Customer("Jack", "Daoe")
        customer.set_family_name("Jones")
        assert customer.get_family_name() == "Jones"    
        
    def test_add_reviews(self):
        """Tests add review and associate it with that customer
        """    
        customer = Customer("Neji", "Hyuga")
        restaurant = Restaurant("White Lotus")
        customer.add_review(restaurant, rating=5)
        assert Review.reviews[-1].restaurant() == restaurant 

    def test_unique_restaurants(self):
        """Test returns a unique list of restaurants
        """
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Red Lotus")
        restaurant2 = Restaurant("Chernobyl")
        restaurant3 = Restaurant("Magnum")
        review = Review(customer, restaurant, rating=4)
        review2 = Review(customer, restaurant2, rating=4)
        review3 = Review(customer, restaurant3, rating=5)
      
        assert len(customer.restaurants()) == 3
        
    def test_number_of_reviews_authored_by_customer(self):
        """Test returns first match found by given name
        """     
        
        customer1 = Customer("Chuck", "Noris")
        customer2 = Customer("Chuck", "Noris")
        first_match = Customer.find_by_name("Chuck Noris")
        assert first_match == customer1
        assert first_match != customer2