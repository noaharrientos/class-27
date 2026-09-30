class parent:
    def __init__ (self,nature,eyecolour):
        self.nature=nature
        self.eyecolour=eyecolour
    def display(self):
        print(f"My nature is {self.nature} and my eyecolour is {self.eyecolour}")
class child(parent):
    def __init__ (self,nature,eyecolour,age,gender,height):
        parent.__init__(self,nature,eyecolour)
        self.age=age
        self.gender=gender
        self.height=height
    def displayvalues(self):
        print(f"My age is {self.age}, my gender is {self.gender} and my height  is {self.height}")
object1 = child("calm","blue",13,"male",5.5)
object1.display()
object1.displayvalues()