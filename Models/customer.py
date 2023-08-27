from review import Review

class Customer:
    customer_count = []
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.customer_count.append(self)
        
    def given_name(self):
        return self.given_name  
    
    def family_name(self):
        return self.family_name 
    
    def set_given_name(self, value):
        self.given_name = value
        
    def set_family_name(self, value):
        self.family_name = value    
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls):
        return cls.customer_count
    
    name = property(given_name, set_given_name)
    family_name = property(family_name, set_family_name)
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating) #call Review instance & pass in 3 arguments
        self.reviews.append(review) 
    
    def restaurants(self):
        unique_restaurants = [review.restaurant() for review in self.reviews]  
        return list(set(unique_restaurants)) 
    
    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customer_count:
            if name == customer.full_name():
                return customer
            else:return "customer name not found"
            
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_names = [customer for customer in cls.customer_count if name == customer.given_name] 
        return matching_names 
    