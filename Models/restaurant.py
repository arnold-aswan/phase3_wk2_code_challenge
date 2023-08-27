from review import Review

class Restaurant:
    restaurants = []
    def __init__(self, name):
        self.name = name
        Restaurant.restaurants.append(self)
        
    def name(self):
        return self.name  
        
    def reviews(self):
        return [review for review in Review.reviews if review.restaurant().name() == self.name]    
    
    def customers(self):
        unique_customers = [review.customer() for review in self.reviews()]
        return list(set(unique_customers))
    
    def average_star_rating(self):
        rating = sum(review.rating() for review in self.reviews())
        return rating / len(self.reviews())