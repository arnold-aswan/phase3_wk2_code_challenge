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
        
        assert review != None
        assert review.restaurant() == restaurant
        assert review.customer() == customer
        assert review.rating() == 5
        
    def test_restaurant_rating(self):
        """Returns the rating of the restaurant
        """    
        get_review = self.create_review()
        assert get_review.rating() == 4
        
            
    def create_review(self):
        customer = Customer("Alice", "Smith")
        restaurant = Restaurant("Sample Restaurant")
        review = Review(customer, restaurant, rating=4)    
        return review