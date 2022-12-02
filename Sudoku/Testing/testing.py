from itertools import chain

orders = [
    [2,0,1],
    [1,2,0],
    [2,1,0]
]

flatten_list = list(chain.from_iterable(orders))

indexes = {
    0: [],
    1: [],
    2: []
}

for i in range(len(flatten_list)):
    indexes[flatten_list[i]].append(i)

print(indexes)


row = [5,1,8,4,6,2,9,3,7]
print(row)

for i in range(3):
    row[indexes[i][0]], row[indexes[i][1]], row[indexes[i][2]] = row[indexes[i][1]], row[indexes[i][2]], row[indexes[i][0]]


print(row)

# indexes = [1,5,8]

# print(indexes)
# indexes[0], indexes[1], indexes[2] = indexes[1], indexes[2], indexes[0]

# print(indexes)