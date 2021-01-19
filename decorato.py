def decorator(function_1):
    def now_exec():
        print("Boom!")
        function_1()
        print("Boom Post!")
    return now_exec

@decorator
def Passing_one():
    print("DigiLocker")


#who = decorator(Passing_one)
Passing_one()
