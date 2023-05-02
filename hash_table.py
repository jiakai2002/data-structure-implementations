# we will implement a hashtable with a list of size 100
# use separate chaining to handle collision

class Hashtable:
    def __init__(self):
        self.size = 10
        self.list = [[] for i in range(self.size)]

    # returns a hash for a key using ASCII
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

    # add a key value pair into hash table, renamed to be standard operator
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.list[h]):
            # if the key already has a value, overwite old value
            if len(element) == 2 and element[0] == key:
                self.list[h][index] = (key, value)
                found = True
                print('hi')
                break
        # key does not have a value yet, append key value pair
        if not found:
            self.list[h].append((key, value))

    # retrieve value of given key, renamed to be standard operator
    def __getitem__(self, key):
        h = self.get_hash(key)
        # iterate through list in corresponding bucket to find key
        for element in self.list[h]:
            if element[0] == key:
                return element[1]

    # delete key value pair
    def __delitem__(self, key):
        h = self.get_hash(key)
        # iterate through list in corresponding bucket to find key
        for index, element in enumerate(self.list[h]):
            if element[0] == key:
                del self.list[h][index]


ages = Hashtable()
ages["john"] = 10
ages["ojhn"] = 15
ages["peter"] = 20
print(ages.get_hash("john"))
print(ages.get_hash("ojhn"))
print(ages.get_hash("peter"))
print(ages.list)
del ages["john"]
print(ages.list)
