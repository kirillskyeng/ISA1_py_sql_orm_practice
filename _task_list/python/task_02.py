"""
в списке всегда есть два числа, сумма которых равна таргету
реализовать такой алгоритм, который выдает индексы таких чисел
если несколько пар индексов дают таргет, возвращается первая пара
"""

def solution(lst, target):
    pass


assert solution([3, 1, 2, 3, 4], 4) == (0, 1)
assert solution([4, 4], 8) == (0, 1)
assert solution([3, 1, 2, 3, 4], 5) == (0, 2)
assert solution([-3, 1, 2, 3, 4], 1) == (0, 4)
print('Решено.')
