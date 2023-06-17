from cars import Car
from trucks import Trucks

car1 = Car("Toyota", "Yaris", "Greeeen", "Wroooomomoooom", "Henriks dytter")
truck1 = Trucks("Frederiks Trucker Truck", "kææmpe stor")

print("My car has the color "+car1.color + "...")
car1.car_broke_down()
print("now what do i do?? ")
print("you get a new " + car1.model)

print("Min truck hedder "+ truck1.name + " og den er " + truck1.size)
print("når jeg dytter med hornet siger det ")
truck1.truck_honk() 

