# Into to Python 3 guided project


class Store:
    def __init__(self, name, categories):
        # init is like a constructor. It is used to define and construct all of the attributes
        # attributes
        # self is like this in JS
        self.name = name
        self.categories = categories

    def __str__(self):
        # return f'{self.name} has {len(self.categories)} categories'
        output = self.name
        # 1. food
        # 2. clothes
        # 3. treats
        i = 1
        for category in self.categories:
            output += f'\n {i}. {category}'
            i += 1
        return output   

    def __repr__(self):
        # __repr__ similar to __str__.
        # __str__ is how we want to display the string to users.
        # __repr__ is how we want to display to developers.
        return f'{self.name} has {len(self.categories)} categories'


my_store = Store("Petapalooza", ["food", "clothes", "treats"])
# print(my_store.__repr__())
print(my_store)
