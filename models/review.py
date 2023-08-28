       
class Review:
    reviews = []
    def __init__(self, customer, restaurant, rating):
        self._customer = customer 
        self._restaurant = restaurant  
        self._rating = rating  
        Review.reviews.append(self) 
        
    def rating(self):
        """Returns the rating for the restaurant
        """
        return self._rating  
    
    @classmethod
    def all(cls):
        """Returns all of the reviews
        """
        return cls.reviews
    
    def customer(self):
        """Returns the customerobject for that review
        """
        return self._customer
    
    def restaurant(self):
        """Returns the restaurant object for that review
        """
        return self._restaurant
          
        