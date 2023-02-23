''''
Exercise: E001-V3 : 

Create one class named “location” with members “name”, “code”.
Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”. This method will return all “movement” objects which belong to the passed “product” as an argument.
Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains “location” as key and actual stock of that product on that location as value.
Create 4 different location objects.
Create 5 different product objects.
Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve. 
Display movements of each product using the “movement_by_product” method.
Display product details with its stock at various locations using “stock_at_locations”.
Display product list by location ( group by location).
'''''


class Location:

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def show_location(self):
        print("name:", self.name)
        print("code:", self.code)


class Movement:

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = self.movements_by_product()
        self.quantity = quantity

    def show_movement(self):
        print("from_location:", self.from_location.name)
        print("to_location:", self.to_location.name)
        print("product:", self.product)
        print("quantity:", self.quantity)
        print()

    @staticmethod
    def movements_by_product(self):
       pass


class Product:

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = {}

    def show_products(self):
        print("name: ", self.name, ','"code:", ','"price:", self.price, ','"stock_at_locations:",
              self.stock_at_locations)


# location object:
l1 = Location("ahmedabad", 101)
l2 = Location("rajkot", 102)
l3 = Location("surat", 103)
l4 = Location("baroda", 104)

# product object:
p1 = Product("car", 201, 200)
p2 = Product("cloths", 203, 500)
p3 = Product("watch", 204, 300)
p4 = Product("shoes", 205, 400)
p5 = Product("tv", 206, 150)

# movement object:
m1 = Movement(l1, l3, p1, 300)
m2 = Movement(l4, l2, p2, 450)
m3 = Movement(l2, l1, p3, 600)
m4 = Movement(l3, l2, p4, 600)
m5 = Movement(l4, l1, p5, 600)

m1.show_movement()
m2.show_movement()
m3.show_movement()
m4.show_movement()
m5.show_movement()
