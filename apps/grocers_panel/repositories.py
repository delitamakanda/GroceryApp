from core.repositories import BaseRepository
from .models import Grocer, Meal, FoodMeal, Shop, Rating

class GrocerRepository(BaseRepository):
    model = Grocer


class MealRepository(BaseRepository):
    model = Meal
    
class FoodMealRepository(BaseRepository):
    model = FoodMeal
    

class ShopRepository(BaseRepository):
    model = Shop
    


class RatingRepository(BaseRepository):
    model = Rating
