from core.services import BaseService
from apps.grocers_panel.repositories import GrocerRepository, MealRepository, FoodMealRepository, ShopRepository, RatingRepository

class GroceryService(BaseService):
    repository_class = GrocerRepository
    
class MealService(BaseService):
    repository_class = MealRepository
    
class FoodMealService(BaseService):
    repository_class = FoodMealRepository
    
class ShopService(BaseService):
    repository_class = ShopRepository
    
class RatingService(BaseService):
    repository_class = RatingRepository