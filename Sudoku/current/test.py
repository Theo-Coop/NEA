# from copy import deepcopy

# class Test:
#     def __init__(self):
#         self.og = [[1,2], [1,3]]
#         self.new = deepcopy(self.og)
#         self.change()

#     def change(self):
#         self.new[1] = 256
#         print(self.og)
#         print(self.new)


# this = Test()

# print(this.new)
# print(this.og)


dicts = {
    (1,2): "hello",
    (1,3): "ez"
}

test = (25,6)

if test not in dicts:
    print("yess")