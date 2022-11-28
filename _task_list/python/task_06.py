"""
Напишите декоратор для функции деления (devide),
который при попытке деления на 0 возвращает None.
"""

# реализация декоратора тут


@zero_save
def devide(x, y):
    return x / y


assert devide(-4, 2) == -2
assert devide(0, 2) == 0
assert devide(4, 0) is None
print('Решено.')