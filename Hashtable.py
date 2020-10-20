class HashTable:
    def __init__(self, initialCapacity=13):
        self.__capacity = initialCapacity
        self.__elements = [[] for _ in range(self.__capacity)]

    def hashFunction(self, value):
        sum = 0
        for chr in value:
            sum += ord(chr)
        return sum % self.__capacity

    def add(self, value):
        key = self.hashFunction(value)
        if not self.__elements[key]:
            self.__elements[key] = [value]
            print("The value",value,"-> key",key,"->index in chained list:", 0)
        else:
            chainedList = self.__elements[key]
            if value not in chainedList:
                chainedList.append(value)
            print("The value",value,"-> key",key,"->index in chained list:", chainedList.index(value))

    def find(self, value):
        key = self.hashFunction(value)
        if self.__elements[key] is None:
            return None
        chainedList = self.__elements[key]
        if value in chainedList:
            return key, chainedList.index(value)
        else:
            return None
    
    def __str__(self):
        return str(self.__elements)