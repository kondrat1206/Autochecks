from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        self.value = value
        self.result = []
        print(self.data)
        for key in self.data:
            print(key)
            if self.data[key] == self.value:
                self.result.append(key)
        print(self.result)
        return self.result



dic = LookUpKeyDict()
dic["a"] = 1
dic["b"] = 2

dic.lookup_key(2)