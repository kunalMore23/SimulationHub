class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("Object is being deleted")

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

if __name__ == "__main__":
    p = Person("Kunal", 22)
    print(p.age)
    print(p)

    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    print(v2)
