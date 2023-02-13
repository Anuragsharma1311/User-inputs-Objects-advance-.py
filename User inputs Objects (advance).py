class Phone:
    def set_color (self , color):
        self.color = color
    def set_cost (self , cost):
        self.cost = cost
    def show_color (self):
        print('color of my phone is' , self.color)
    def show_cost (self):
        print('cost of my phone is' , self.cost)
apple = Phone()
apple.set_color('Black')
apple.set_cost('10000')
apple.show_color()
apple.show_cost()