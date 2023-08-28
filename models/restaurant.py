from models.review import Review

class Restaurant:
    restaurants = []
    def __init__(self, name):
        self._name = name
        Restaurant.restaurants.append(self)
        
    def get_name(self):
        """Returns the restaurant name
        """
        return self._name  
        
    def reviews(self):
        """Returns a list of reviews for the restaurant
        """
        return [review for review in Review.reviews if review.restaurant().name() == self._name]    
    
    def customers(self):
        """Returns a unique list of customers who have reviewed a restaurant
        """
        unique_customers = [review.customer() for review in self.reviews()]
        return list(set(unique_customers))
    
    def average_star_rating(self):
        """Returns average star rating for a restaurant
        """
        rating = sum(review.rating() for review in self.reviews())
        return rating / len(self.reviews())