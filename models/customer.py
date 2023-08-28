from models.review import Review

class Customer:
    customer_count = []
    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        Customer.customer_count.append(self)
        
    def given_name(self):
        """Returns the customer's given name
        """
        return self._given_name  
    
    def get_family_name(self):
        """Returns the customer's family name
        """
        return self._family_name 
    
    def set_given_name(self, value):
        """sets the customer's given name
        """
        self._given_name = value
        
    def set_family_name(self, value):
        """sets the customer's family name
        """
        self._family_name = value    
    
    def full_name(self):
        """Returns the customer's full name
        """
        return f"{self._given_name} {self._family_name}"
    
    @classmethod
    def all(cls):
        """Returns all the customer instances
        """
        return cls.customer_count
    
    name = property(given_name, set_given_name)
    family_name = property(get_family_name, set_family_name)
    
    def add_review(self, restaurant, rating):
        """Creates a new review and associate it with that customer
        """
        Review(self, restaurant, rating) #call Review instance & pass in 3 arguments

    
    def restaurants(self):
        """Returns unique list of restaurants
        """
        unique_restaurants = [review.restaurant() for review in self.reviews]  
        return list(set(unique_restaurants)) 
    
    def num_reviews(self):
        """Returns the number of reviews
        """
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
        """Returns the customer with a given name
        """
        for customer in cls.customer_count:
            if name == customer.full_name():
                return customer
            else:return "customer name not found"
            
    @classmethod
    def find_all_by_given_name(cls, name):
        """Returns a list of names that match the given name
        """
        matching_names = [customer for customer in cls.customer_count if name == customer._given_name()] 
        return matching_names 
    