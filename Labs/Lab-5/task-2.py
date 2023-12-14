def my_solution():
    initial_list = [10, 20, 30, 40, 50, 60]
    limit = (len(initial_list) // 2)
    first = initial_list[0:limit]
    second = initial_list[limit:len(initial_list)]
    print(first)
    print(second)

def teacher(lst, first_part_len):
    first_part = lst[:first_part_len]
    second_part = lst[first_part_len:]
    return first_part, second_part

lst = [10 ,20 ,30 ,40 ,50 ,60]
first_part_len = 3
first_part, second_part = teacher(lst, first_part_len)
print("original list: ", lst)
print("first part: ", first_part)
print("second part: ", second_part)
