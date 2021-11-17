class MyDict(dict):
    def get(self, key):
        if key in self.keys():
            return self[key]
        else: return 0

newDict = MyDict()
newDict[1] = 'one'
newDict[2] = 'two'
newDict[3] = 'three'
print(newDict.get(1))
print(newDict.get(4))