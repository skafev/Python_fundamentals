class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.items_with_letter = []

    def add_product(self, product):
            self.products.append(product)

    def get_by_letter(self, first_letter):
        for item in self.products:
            if first_letter in item:
                self.items_with_letter.append(item)
        return self.items_with_letter

    def __repr__(self):
        res = f"Items in the {self.name} catalogue:\n"
        res += "\n".join(sorted(self.products))

        return res


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)