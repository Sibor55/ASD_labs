"""
Здесь будут сортировки: \n
№4 Сортировка методом прочесывания (comb_sort) \n
№5 Вставками (insert_sort) \n
№6 Посредством выбора (sel_sort) \n
№7 Шелла (shell_sort) \n
№8 Поразрядная (radix_sort) \n
№9 Пирамидальная (heap_sort) \n
№10 Слиянием \n
№11 Быстрая \n
№12 Внешняя многофазная \n
"""


def comb_sort(ls):
    """Сортировка методом прочесывания (Comb Sort)"""
    n = len(ls)
    step = n  # Начальный шаг равен длине списка
    flag = False  # Флаг для отслеживания перестановок
    while step > 1 or flag:  # Продолжаем, пока шаг больше 1 или были перестановки
        if step > 1:
            step = int(step / 1.25)  # Уменьшаем шаг с коэффициентом 1.25
        flag, i = False, 0
        while i + step < n:
            if (
                ls[i] > ls[i + step]
            ):  # Если текущий элемент больше элемента на расстоянии шага
                ls[i], ls[i + step] = ls[i + step], ls[i]  # Меняем их местами
                flag = True  # Устанавливаем флаг перестановки
            i += step
    return ls


def insert_sort(ls):
    """Сортировка вставками (Insertion Sort)"""
    for j in range(1, len(ls)):  # Проходим по элементам начиная со второго
        key = ls[j]  # Текущий элемент для вставки
        i = j - 1
        while i >= 0 and ls[i] > key:  # Ищем место для вставки
            ls[i + 1] = ls[i]  # Сдвигаем элементы вправо
            i = i - 1
        ls[i + 1] = key  # Вставляем текущий элемент на правильное место
    return ls


def sel_sort(ls):
    """Сортировка выбором (Selection Sort)"""
    for i in range(len(ls) - 1):
        min_index = i  # Предполагаем, что минимальный элемент на текущей позиции
        for j in range(
            i + 1, len(ls)
        ):  # Ищем минимальный элемент в оставшейся части списка
            if ls[j] < ls[min_index]:  # Если нашли меньший элемент
                min_index = j  # Обновляем индекс минимального элемента
        ls[i], ls[min_index] = (
            ls[min_index],
            ls[i],
        )  # Меняем местами минимальный элемент и текущий
    return ls


def shell_sort(ls):
    """Сортировка Шелла (Shell Sort)"""
    last_index = len(ls)
    step = len(ls) // 2  # Начальный шаг равен половине длины списка
    while step > 0:  # Продолжаем до шага 0
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while (
                delta >= 0 and ls[delta] > ls[j]
            ):  # Если найден элемент больше, чем на шаге
                ls[delta], ls[j] = ls[j], ls[delta]  # Меняем местами
                j = delta
                delta = j - step
        step //= 2  # Уменьшаем шаг вдвое
    return ls


def radix_sort(ls):
    """Поразрядная сортировка (Radix Sort)"""
    max_digits = max(
        [len(str(x)) for x in ls]
    )  # Определяем количество цифр в максимальном числе
    base = 10  # Основание системы счисления
    bins = [[] for _ in range(base)]  # Создаем список для 'карманов' от 0 до 9
    for i in range(max_digits):  # Проходим по каждому разряду
        for x in ls:
            digit = (x // base**i) % base  # Извлекаем цифру нужного разряда
            bins[digit].append(x)  # Кладем элемент в соответствующий 'карман'
        ls = [x for queue in bins for x in queue]  # Объединяем элементы из 'карманов'
        bins = [[] for _ in range(base)]  # Очищаем 'карманы' для следующего разряда
    return ls
