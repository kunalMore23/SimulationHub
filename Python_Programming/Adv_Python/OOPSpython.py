class Car:
    def __init__(self, numTyres, engineType):
        self.tyres = numTyres
        self.carEngineType = engineType

    def drive(self):
        print("Car is being driven")

    def selfDriving(self):
        return "This is a {} car".format(self.carEngineType)

if __name__ == "__main__":
    car1 = Car(4, "petrol")
    print(car1.selfDriving())
