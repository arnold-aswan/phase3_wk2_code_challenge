
class Customer:
    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        
    def given_name(self):
        return self.name  
    
    def family_name(self):
        return self.family_name 
    
    def set_name(self, value):
        self.name = value
        
    def set_family_name(self, value):
        self.family_name = value    
    
    def full_name(self):
        return self.name, self.family_name
    
    name = property(given_name, set_name)
    family_name = property(family_name, set_family_name)