import random

user_id = 5

ran_num = random.randint(10000, 99999)
print(ran_num)

puzzle_id = int(str(user_id) + str(ran_num))

print(puzzle_id)