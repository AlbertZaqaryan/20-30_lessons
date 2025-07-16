import math

class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    def item_count(self):
        return len(self.collection)
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)
    
    def page_item_count(self, page_index):
        if page_index < self.page_count() - 1:
            return self.items_per_page
        else:
            if len(self.collection) % self.items_per_page == 0:
                return self.items_per_page
            else:
                return len(self.collection) % self.items_per_page
    
    def page_index(self, item_index):
        return item_index // self.items_per_page

book1 = PaginationHelper(['audi', 'opel', 'bmw', 'mers', 'honda', 'fiat', 'mini', 'rolls'], 3)
print(book1.page_index(0))