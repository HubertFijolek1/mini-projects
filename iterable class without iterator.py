class CombinationsIterator:
 
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
 
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0
 
    def __next__(self):
 
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1
 
        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1
 
        if self.current_product >= len(self.products):
            self.current_product =0
            raise StopIteration()
 
        item_to_return = "{} - {} -{}".format(self.products[self.current_product],
                                              self.promotions[self.current_promotion],
                                              self.customers[self.current_customer])
 
        self.current_customer += 1
 
        return  item_to_return
 
 
class Combinations:
 
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.iterator = CombinationsIterator(self.products, self.promotions, self.customers)
 
    def __iter__(self):
        return  self.iterator
 
 
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]
 
combinations = Combinations(products, promotions, customers)
 
for c in combinations:
    print(c)