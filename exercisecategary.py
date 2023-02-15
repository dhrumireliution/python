''''
Exercise: E001-V1
  Create one class named "category" with members "name", "code", "no_of_products"
  Create one class named "product" with members "name", "code", "category", "Price"
  Create three objects of category.
  Create 10 different products. Code must be unique.
  Print category info with its no_of_products
  Sort and Print products based on price ( Price High to Low and Low to High) with all details.
  Search product using its code.
'''''

class category:

    def __init__(self, name, code,no_of_products):
        self.name = name
        self.code = code
        self.no_of_products=no_of_products

    def show_category(self):
        print("name ", self.name)
        print("code", self.code)
        print("no_of_products",self.no_of_products)


class product(category):

    def __init__(self, name, code, category, price):

        self.name = name
        self.code = code
        self.category = category
        category.no_of_products += 1
        self.price = price


    def show_products(self):
        print("name: ", self.name ,"code:",self.code,"category:",self.category.name,"price:",self.price)


    def shorting(p_list):
             # Sort and Print products based on price:

                # price Low to High:

        for i in range(len(p_list)):
            for j in range(i + 1, len(p_list)):
                if p_list[i].price > p_list[j].price:
                    p_list[i], p_list[j] = p_list[j], p_list[i]
        for i in p_list:
            i.show_products()


    def hightolow(p_list):
            # Sort and Print products based on price:

                    # Price High to Low:

        for i in range(len(p_list)):
            for j in range(i + 1, len(p_list)):
                if p_list[i].price < p_list[j].price:
                    p_list[i], p_list[j] = p_list[j], p_list[i]

        for i in p_list:
            i.show_products()

    def code(p_list):
             # Search product using its code:

        code = int(input("enter the code:"))
        for i in p_list:
            if i.code == code:
                i.show_products()

#3 diffrent category:
l1 = category("cloths", 201, 0)
l2 = category("watch", 301, 0)
l3 = category("shoes", 401, 0)


#10 diffrent products:

p1 = product("louis vuitton", 202, l1, 4000)
p2 = product("hermes", 203, l1, 2000)
p3 = product("nike", 204, l1, 3000)
p4 = product("adidas", 205, l1, 5000)
p5 = product("rolex", 302, l2, 8000)
p6 = product("omega sa", 303, l2, 10000)
p7 = product("patek philippe", 304, l2, 13000)
p8 = product("tag heuer", 305, l2, 22000)
p9 = product("puma", 402, l3, 3000)
p10 = product("new balance", 403, l3, 5000)

#list of diffrent products:
p_list = [p1, p2,p3,p4,p5,p6,p7,p8,p9,p10]

print(".......show category.........")
l1.show_category()
l2.show_category()
l3.show_category()

print(".......show products.......:")
for rec in p_list:
    rec.show_products()

print("..........low to high.......")
product.shorting(p_list)

print("......price high to low.......:")
product.hightolow(p_list)

print("serch product using its code......:")
product.code(p_list)















































