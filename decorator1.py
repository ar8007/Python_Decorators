def wrapper_function(origional_function):
    def inner_function(*args,**kwargs):
        print("Hello Alok Ranjan")
        return origional_function(*args,**kwargs)
    return inner_function

@wrapper_function
def ranjan():
    print("i want to visit your village !")
@wrapper_function
def unknown(name,age):
    print("hello my name is {} and my age is {}".format(name,age))

ranjan()
unknown("Alok Ranjan",23)
# wrapper_function = wrapper_function(unknown)
# wrapper_function("Alok RAnjan",25)
# rahul = wrapper_function(ranjan)
# rahul()