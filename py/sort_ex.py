import sorting
from timer import Timer
import random

"""Для проверки сортировок"""

large_list = [random.randint(1, 100000) for _ in range(10000)]
sort_funcs = [
            sorting.comb_sort,
            sorting.insert_sort,
            sorting.sel_sort,
            
            ]


def check_sort(ls, sort_func):
    t = Timer()
    t.start()
    newlist = sort_func(ls.copy())
    t.stop()
    return newlist


for sort_func in sort_funcs:
    sorted_list = check_sort(large_list, sort_func)
    print(
        f"{sort_func.__name__} завершена: \n {sorted_list[:10]} . . . {sorted_list[-10:]} \n \n \n"
    )

print(f"Список: {large_list[:10]} . . . {large_list[-10:]}")
