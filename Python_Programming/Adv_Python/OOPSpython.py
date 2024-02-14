class Car:

    def __init__(self, numTyres, engineType):
        self.tyres = numTyres
        self.carEngineType = engineType

    def driveDecorator(function):
        def startEngine(*args, **kwargs):
            print("Engine is starting....")
            function(*args, **kwargs)
        return startEngine

    @driveDecorator
    def drive(self):
        print("Car is being driven")

    def selfDriving(self):
        return "This is a {} car".format(self.carEngineType)

def driveDecorator(function):
    def startEngine():
        print("Engine is starting....")
        function()
    return startEngine

@driveDecorator
def drive():
    print("Car is being driven...")

if __name__ == "__main__":
    car1 = Car(4, "petrol")
    car1.drive(1)
    # drive()