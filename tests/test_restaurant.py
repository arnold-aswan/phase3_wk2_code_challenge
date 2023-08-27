from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

class TestRestaurant:
    def test_new_restaurant_created(self):
        """Tests if a new restaurant is created succesfully
        """
        restaurant = Restaurant("barista")
        assert restaurant != None
        assert restaurant.get_name() == "barista"
        
    def test_get_restaurant_name(self):  
        """Test returns restaurant name 
        """  
        restaurant1 = Restaurant("Ichiraku")
        assert restaurant1.get_name() == "Ichiraku"