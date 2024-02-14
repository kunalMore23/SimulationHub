class Logger:
    def __init__(self) -> None:
        print("Constructor called")

    def logged(function):
        def wrapper(*args, **kwargs):
            value = function(*args, **kwargs)
            with open("logfile.txt", 'a+') as f:
                fname = function.__name__
                print(f"{fname} returned value {value}")
                f.write(f"{fname} was called and returned {value}\n")
            return value
        return wrapper
    
    @logged
    def hello(self):
        return "Hello World"

if __name__ == "__main__":
    p1 = Logger()
    print(p1.hello())