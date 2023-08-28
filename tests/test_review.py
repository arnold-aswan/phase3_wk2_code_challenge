from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

class TestReview:
    def test_review_initialization(self):
        """Tests if review is initailized with a customer, restaurant and a rating
        """
        customer = Customer("jack", "marley")
        restaurant = Restaurant("konoha")
        review = Review(customer, restaurant, rating=5)
        
        customer3 = Customer("seth", "rollins")
        restaurant3 = Restaurant("konoha senpo")
        review3 = Review(customer3, restaurant3, rating=5)
        assert review != None
        assert review.restaurant() == restaurant
        assert review.customer() == customer
        assert review.rating() == 5
        
    def test_restaurant_rating(self):
        """Returns the rating of the restaurant
        """    
        get_review = self.create_review()
        assert get_review.rating() == 4
     
    def test_review_all(self):
        """Returns all of the reviews
        """
        assert len(Review.all()) == 7   
            
    def test_review_customer(self):
        """Returns customer object
        """
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Limbo")
        review = Review(customer, restaurant, rating=5)
        assert customer.full_name() == "John Doe" 
    
    def test_review_restaurant(self):
        """Returns restaurant object
        """
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Limbo")
        review = Review(customer, restaurant, rating=5)
        assert restaurant.get_name() == "Limbo" 
                
                
    # def test_average_star_rating(self):
    #     """Returns average rating
    #     """
    #     customer = Customer("John", "Doe")
    #     restaurant = Restaurant("Limbo")
    #     review = Review(customer, restaurant, rating=5)
        
    #     customer02 = Customer("Jane", "Doe")
    #     restaurant02 = Restaurant("Limbo")
    #     review02 = Review(customer02, restaurant02, rating=5)
        
    #     assert Restaurant().average_star_rating() == 5
       
                    
    def create_review(self):
        customer1 = Customer("Alice", "Smith")
        restaurant1 = Restaurant("Los santos")
        review1 = Review(customer1, restaurant1, rating=4)    
        return review1