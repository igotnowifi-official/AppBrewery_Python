class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml\n")
        print(f"Milk: {self.resources['milk']}ml\n")
        print(f"Coffee: {self.resources['coffee']}g\n")

    def resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
              print(f"Sorry there is not enough {item}.\n")
              if input("Would you like to refill resources. Type 'y' for yes and 'n' for no. \n").lower() == 'y':
                self.resources[item] += 300
              return can_make  
              can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}.\n")