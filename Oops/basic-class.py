# TODO: Create a  basic class 
class book:
    def __init__(self,title):
        self.title = title

## * init function is one of the special function in python while working with classes. init function is called to initialize the new object with  information.
# * it is called before any function is called.
# * Note: this function is not constructor function because object is already created. and it is safe to start initializing it.

# * init function takes 2 args but only one is passed  because whenever we call a Method on a Python object the object itself gets automatically passed in as the first argument.

# TODO: Create a instance of  class.

b1=book("Python the hard way!")
b2=book("Python : Automate the boring stuff!")

#TODO: Print class and properties.

print(b1)
print(b1.title)
print(b2.title)