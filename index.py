from appliances.kitchen.utility.dishwasher import DishWasher
from appliances.laundry.dryer import Dryer
from appliances.laundry.washer import Washer
from appliances.kitchen.utility.refrigerator import Refrigerator
from appliances.kitchen import CoffeeMaker
from appliances.kitchen import CanOpener


whirlpool_dishwasher = DishWasher("blue") 
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless") 
print(lg_fridge.color)  
lg_fridge.make_ice()  
  
mr_coffee = CoffeeMaker("white")  
mr_coffee.make_coffee()    

luxury_can_opener = CanOpener("Deep Purple")
print(luxury_can_opener.color)
luxury_can_opener.open_can()