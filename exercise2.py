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


        def __init__(self, name, code, no_of_products,parent=None):
            self.name = name
            self.code = code
            self.no_of_products = no_of_products
            self.parent=parent
            self.products = []
            self.display_name=self.generate_display_name()

        def show_category(self):
            print("name: ", self.name)
            print("code:", self.code)
            print("no_of_products:", self.no_of_products)
            for x in self.products:
                print(x)
            print("display_name:",self.display_name)

            print()

        def show_name(self):
            print("name: ", self.name)
            for x in self.products:
                print(x)
            print()

        def generate_display_name(self):


             if self.parent==None:
                 return self.name
             # else:
             #   Category.generate_display_name(self)
             #    return self.parent+'>'+self.name




        def sort_category(c_list):
            for i in range(len(c_list)):
                for j in range(i + 1, len(c_list)):
                    if c_list[i].name > c_list[j].name:
                        c_list[i], c_list[j] = c_list[j], c_list[i]
            for i in c_list:
                i.show_name()

class Products(Category):

        def __init__(self, name, code, category, price):
            self.name = name
            self.code = code
            self.category = category
            category.no_of_products += 1
            category.products.append(self)
            self.price = price

        def show_products(self):
            print("name: ", self.name, ','"code:", self.code, ','"category:", self.category.name, ','"price:",
                  self.price)

        def __repr__(self):
            return ( "product:-"+ "name:" + self.name +  '|'+  "price:"+ str(self.price)+ '|'+  "code:" + str(self.code)+ '|'+"category:" + self.category.name )



#5 diffrent category:

c1 = Category("vehicle",101,0)
c2 = Category("car",102,0,c1.name)
c3 = Category("petrol",103,0,c2.name)
c4 = Category("creditcard",104,0,c3.name)
c5 = Category("bank",105,0,c4.name)

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


print(".......show category.........")
c1.show_category()
c2.show_category()
c3.show_category()
c4.show_category()
c5.show_category()

print("...........showsortcategory..............")
Category.sort_category(c_list)


