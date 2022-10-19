from copy import deepcopy

class Test:
    def __init__(self):
        self.og = [[1,2], [1,3]]
        self.new = deepcopy(self.og)
        self.change()

    def change(self):
        self.new[1] = 256
        print(self.og)
        print(self.new)


this = Test()

print(this.new)
print(this.og)
