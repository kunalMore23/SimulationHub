class Car:
    def __init__(self, tyres, engineType) -> None:
        self.tyres = tyres
        self.engineType = engineType

    def myDecorator(function):
        def startEngine(*args, **kwagrs):
            return_type = function(*args, **kwagrs)
            print("Engine is starting...")
            return return_type

        return startEngine

    @myDecorator
    def hello(self, k):
        return "Hello World"
    
    @myDecorator
    def drive(self, key):
        print("Driving...")
        return "Car is being driven"
    
if __name__ == "__main__":
    c = Car(4, "Petrol")
    print(c.drive(1))