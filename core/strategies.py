from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, price):
        pass
    
class RegularPricingStrategy(PricingStrategy):
    def calculate_price(self, price):
        return price
    
class DiscountedPricingStrategy(PricingStrategy):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage
        
    def calculate_price(self, price):
        return price * (1 - self.discount_percentage / 100)