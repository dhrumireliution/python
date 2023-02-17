''''Exercise: E001-V2
● Add new data members “parent”, “display_name”, “products” (list of product objects)
inside category class.
● Add a new member function to generate “display_name”.
● “display_name” has text value as below.
     Vehicle category without parent then “Vehicle” 
     Car category with “Vehicle” as parent then “Vehicle > Car”
     Petrol category with “Car” as parent then “Vehicle > Car > Petrol”
● Create 5 category objects with parent and child relation.
● Create 3 product objects in each category.
● Display Category with its Code, Display Name and all product details inside that
category.
● Display product list by category ( group by category, order by category name).
'''''

class Category:


        def __init__(self, name, code, no_of_products):
            self.name = name
            self.code = code
            self.no_of_products = no_of_products
            self.parent=0
            self.products=0
            self.display_name=0

        def show_category(self):
            print("name ", self.name)
            print("code", self.code)
            print("no_of_products", self.no_of_products)
            print("parent",self.parent)
            print("products",self.products)
            print("display_name:",self.display_name)

        def display_name(Category):

            pass

class Products(Category):

        def __init__(self, name, code, category, price):
            self.name = name
            self.code = code
            self.category = category
            category.no_of_products += 1
            self.price = price

        def show_products(self):
            print("name: ", self.name, ','"code:", self.code, ','"category:", self.category.name, ','"price:",
                  self.price)



#5 diffrent category:

c1 = Category("vehicle",101,0)
c2 = Category("car",102,0)
c3 = Category("petrol",103,0)
c4 = Category("creditcard",104,0)
c5 = Category("bank",105,0)

c_list=[c1,c2,c3,c4,c5]

#15 diffrent products:

p1 = Products("Car",201, c1, 200)
p2 = Products("bike",202, c1, 100)
p3 = Products("railed vehicles", 203, c1, 500)
p4 = Products("audi", 204, c2, 300)
p5 = Products("ford", 205, c2, 400)
p6 = Products("land rover", 206, c2, 150)
p7 = Products("Indian Oil Corporation", 207, c3, 100)
p8 = Products("Oil India Limited", 208, c3, 113)
p9 = Products("Tata Petrodyne", 209, c3, 120)
p10 = Products("Fuel Credit Cards", 210, c4, 210)
p11 = Products("Rewards Credit Cards", 211, c4, 214)
p12 = Products("Cashback Credit Cards", 212, c4, 230)
p13 = Products("icici", 213, c5, 211)
p14 = Products("hdfc", 214, c5, 300)
p15 = Products("sbi", 215, c5, 500)



p_list=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]

print(".......show category.........")
c1.show_category()
c2.show_category()
c3.show_category()
c4.show_category()
c5.show_category()

print(".......show products.......:")
for rec in p_list:
    rec.show_products()

Category.display_name(Category)