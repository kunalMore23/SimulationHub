def myDecorator(function):
    def wrapper():
        print("I am decorating the function")
        function()
        
    return wrapper

@myDecorator
def hello_world():
    print("Hello world")

if __name__ == "__main__":
    hello_world()