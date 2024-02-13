import matplotlib.pyplot as plt
import numpy as np


class dsTypeTests:
    def __init__(self):
        pass

    def numpyLib():
        l = [1, 2, 3, 4, 5]
        arr = np.array(l)
        print(arr)


    def pltTest():
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [1, 2, 3, 4, 5]

        plt.plot(lst1, lst2)
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()


    def dictTest():
        dict = {"car1": "mercedes", "car2": "BMW", "car3": "audi"}
        for key in dict:
            print(key)
        for value in dict.values():
            print(value)


    def nestedDictTest():
        nDict1 = {"mercedes": "1990"}
        nDict2 = {"audi": "1930"}
        nDict3 = {"BMW": "1920"}
        mdict = {"1": nDict1, "2": nDict2, "3": nDict3}
        print(mdict["1"]["mercedes"])


    def tupleTest():
        pass


if __name__ == "__main__":
    test = dsTypeTests()
    test.nestedDictTest()
