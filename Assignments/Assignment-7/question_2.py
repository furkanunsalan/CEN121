def recursive_sum(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + recursive_sum(num_list[1:])

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_sum(num_list)
print(f"Sum of the given list is {result}")
