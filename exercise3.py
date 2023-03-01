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
        self.product = []

    def show_location(self):
        print("name:", self.name)
        print("code:", self.code)
        for x in self.product:
            print(x)

    def show_name(self):
        print("name: ", self.name)
        for x in self.product:
            print(x)
        print()

    def __repr__(self):
        return self.name

    @staticmethod
    def sort_location(loc_list):
        for i in range(len(loc_list)):
            for j in range(i + 1, len(loc_list)):
                if loc_list[i].name > loc_list[j].name:
                    loc_list[i], loc_list[j] = loc_list[j], loc_list[i]
        for i in loc_list:
            i.show_name()


class Movement:

    def __init__(self, from_location, to_location, quantity, product):
        self.from_location = from_location
        self.to_location = to_location
        self.quantity = quantity
        self.product = product
        self.generate_closing_stock()

        product.stock_at_locations.update({self.to_location.name: str(self.quantity)})
        product.stock_at_locations.update({self.from_location.name: str(self.generate_closing_stock())})

    def show_movement(self):
        print("from_location:", self.from_location.name)
        print("to_location:", self.to_location.name)
        print("product:", self.product.name)
        print("quantity:", self.quantity)
        print()

    def generate_closing_stock(self):

        for i, j in self.product.stock_at_locations.items():
            try:
                if self.quantity <= j:
                    return j - self.quantity
            except:
                return "sorry,out of stock"



    @staticmethod
    def movements_by_product(product):

        for i in mov_list:
            if i.product == product:
                i.show_movement()


class Product:

    def __init__(self, name, code, price, stock_at_locations, location):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = stock_at_locations
        self.location = location
        location.product.append(self)

    def show_products(self):
        print("name: ", self.name, ','"code:", self.code, ',' "price:", self.price, ',' "stock_at_locations:",

              self.stock_at_locations)

    def __repr__(self):
        return ("product:-" + "name:" + self.name + '|' + "code:" + str(
            self.code) + '|' + "price:" + str(self.price) + '|' + "stock_at_locations:" + str(self.stock_at_locations))


# location object:
ahmedabad = Location("ahmedabad", 101)
rajkot = Location("rajkot", 102)
surat = Location("surat", 103)
baroda = Location("baroda", 104)

loc_list = [ahmedabad, rajkot, surat, baroda]

# product object:
p1 = Product("car", 201, 200, {ahmedabad: 40}, ahmedabad)
p2 = Product("cloths", 203, 500, {baroda: 35}, baroda)
p3 = Product("watch", 204, 300, {rajkot: 25}, rajkot)
p4 = Product("shoes", 205, 400, {surat: 60}, surat)
p5 = Product("tv", 206, 150, {baroda: 45}, baroda)

p_list = [p1, p2, p3, p4, p5]

# movement object:
m1 = Movement(ahmedabad, surat, 30, p1)
m2 = Movement(baroda, rajkot, 40, p2)
m3 = Movement(rajkot, ahmedabad, 20, p3)
m4 = Movement(surat, rajkot, 56, p4)
m5 = Movement(baroda, ahmedabad, 40, p5)

mov_list = [m1, m2, m3, m4, m5]

# movements_by_product:
print("............movements_by_product............")
Movement.movements_by_product(p1)
Movement.movements_by_product(p2)
Movement.movements_by_product(p3)
Movement.movements_by_product(p4)
Movement.movements_by_product(p5)

print(".............show-product............")
for rec in p_list:
    rec.show_products()
print()

print("...........translocation..............")
Location.sort_location(loc_list)
