# Using instance methods and attributes

class book:
    def __init__(self,title,author,pages,price):
        self.title = title                                      # * Each one this is called instance attributes  becasue the value they holds are unique to each instance of object.
        self.author = author
        self.pages = pages
        self.price = price
        # * This double underscore used then Py interpreter will change the name of that attribute or method so that other class trying to access will get error.
        self.__secret = "This one is secret attribute!" 
    
    
    def getprice(self):
        if hasattr(self,"_discount"):                       # * has attributes check if there exists that attribute then only.
            return self.price - (self.price * self._discount)
        else:
            return self.price


    def discount(self,amount):
        self._discount = amount  # * this (single) underscore in front of attribute name this is to give others a hint that this attribute is considered internal to class.



b1=book("Python","No Idea",450,50)

# call methods of an instance "getprice"
print("Book Price is: ",b1.getprice())

# call method for setting Discount.
print(b1.discount(0.50))
print("Discounted Price: ",b1.getprice())
#calling hidden attribute
# print(b1.__secret) will give error
print(b1._book__secret) # will give output!

