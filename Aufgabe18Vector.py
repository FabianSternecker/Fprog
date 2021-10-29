class Vector:
    def __init__(self):
        self.__vector = dict();
    def __setitem__(self, key, value):
        if(value != 0):
            self.__vector[key] = value;
    def __getitem__(self, item):
        return self.__vector[item];
    def __str__(self):
        return str(self.__vector)
testVector = Vector()
testVector[0] = 0.0
testVector[1] = 0.1
testVector[2] = 0.5
print(testVector)