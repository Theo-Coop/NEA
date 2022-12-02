from itertools import chain

orders = [
    [2,0,1],
    [1,2,0],
    [2,1,0]
]

flatten_list = list(chain.from_iterable(orders))

new_orders = [
    [],
    [],
    []
]

for i in range(3):
    selected_num = flatten_list[i]
    for num in flatten_list:
        if num == selected_num:
            new_orders[i].append(flatten_list[num])

print(new_orders)