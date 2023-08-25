
class Customer:
    customer_count = 0
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customer_count += 1
        
    def get_given_name(self):
        return self.given_name  
    
    def get_family_name(self):
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
    
    name = property(get_given_name, set_given_name)
    family_name = property(get_family_name, set_family_name)
    
    
class Restaurant:
    def __init__(self, name):
        self.name = name
        
    def name(self):
        return self.name  
  
    
class Review:
    reviews = []
    def __init__(self, customer, restaurant, rating):
        self.customer = customer 
        self.restaurant = restaurant  
        self.rating = rating  
        Review.reviews.append(self) 
        
    def rating(self):
        return self.rating  
    
    @classmethod
    def all(cls):
        return cls.reviews
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
          
        