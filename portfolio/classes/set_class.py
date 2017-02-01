class mySet:
    def __init__(self):
        self.dict = {}

    def __iter__(self):
        return iter(self.dict.keys())

    def __contains__(self, item):
        return item in self.dict

    def add(self, item):
        self.dict[item] = 1

    def __len__(self):
        return len(self.dict)

    def issubset(self, t):
        key_set = self.dict.keys()
        for key in key_set:
            if key not in t:
                return False
        return True

    def issuperset(self, t):
        key_set = self.dict.keys()
        for key in t:
            if key not in key_set:
                return False
        return True

    def union(self, t):
        for key in t:
            self.dict[key] = 1

    def intersection(self, t):
        key_set = self.dict.keys()
        for key in key_set:
            if key not in t:
            	self.dict.pop(key)

    def copy(self):
    	new_set = mySet()
        for e in self.dict:
            new_set.add(e)
        return new_set

    def __str__(self):
        string = '{'
        for e in self.dict.keys():
            string += str(e)
            string += ','
        string = string[:-1]
        return string + '}'