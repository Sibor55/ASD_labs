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
    """
    Сортировка методом прочесывания (Comb Sort).
    Алгоритм основан на пузырьковой сортировке, но с уменьшением шага проверки элементов.
    """
    n = len(ls)
    step = n  # Начальный шаг (равен длине списка)
    flag = True  # Флаг для отслеживания перестановок
    while step > 1 or flag:
        if step > 1:
            step = int(
                step / 1.25
            )  # Уменьшаем шаг (коэффициент 1.25 - стандартное значение)
        flag = False
        for i in range(n - step):
            if ls[i] > ls[i + step]:  # Сравниваем элементы на расстоянии шага
                ls[i], ls[i + step] = ls[i + step], ls[i]  # Меняем их местами
                flag = True  # Устанавливаем флаг, если произошла перестановка
    return ls


def insert_sort(ls):
    """
    Сортировка вставками (Insertion Sort).
    Элементы сравниваются с предыдущими и вставляются на нужную позицию.
    """
    for j in range(
        1, len(ls)
    ):  # Начинаем с 1-го элемента, так как 0-й уже отсортирован
        key = ls[j]  # Запоминаем текущий элемент
        i = j - 1
        while (
            i >= 0 and ls[i] > key
        ):  # Сдвигаем элементы, пока не найдем место для вставки
            ls[i + 1] = ls[i]
            i -= 1
        ls[i + 1] = key  # Вставляем текущий элемент на нужное место
    return ls


def sel_sort(ls):
    """
    Сортировка выбором (Selection Sort).
    Алгоритм ищет минимальный элемент и перемещает его в начало неотсортированной части списка.
    """
    for i in range(len(ls) - 1):
        min_index = (
            i  # Предполагаем, что минимальный элемент находится на текущей позиции
        )
        for j in range(
            i + 1, len(ls)
        ):  # Поиск минимального элемента в оставшейся части
            if ls[j] < ls[min_index]:
                min_index = j  # Обновляем индекс минимального элемента
        ls[i], ls[min_index] = (
            ls[min_index],
            ls[i],
        )  # Меняем местами текущий и минимальный элементы
    return ls


def shell_sort(ls):
    """
    Сортировка Шелла (Shell Sort).
    Улучшенный вариант сортировки вставками с использованием переменного шага.
    """
    n = len(ls)
    step = n // 2  # Начальный шаг равен половине длины списка
    while step > 0:
        for i in range(step, n):
            temp = ls[i]  # Текущий элемент для вставки
            j = i
            while j >= step and ls[j - step] > temp:  # Сравнение с элементами через шаг
                ls[j] = ls[j - step]
                j -= step
            ls[j] = temp  # Вставляем элемент
        step //= 2  # Уменьшаем шаг
    return ls


def radix_sort(ls):
    """
    Поразрядная сортировка (Radix Sort).
    Работает с числами, сортируя их по разрядам (единицы, десятки, сотни и т.д.).
    """
    max_num = max(ls)  # Находим максимальное число для определения количества разрядов
    exp = 1  # Текущий разряд (единицы, десятки и т.д.)
    while max_num // exp > 0:  # Продолжаем, пока есть разряды для обработки
        bins = [
            [] for _ in range(10)
        ]  # Создаем 10 "карманов" для каждого разряда (0-9)
        for num in ls:
            bins[(num // exp) % 10].append(
                num
            )  # Кладем число в соответствующий "карман"
        ls = [num for sublist in bins for num in sublist]  # Собираем числа обратно
        exp *= 10  # Переходим к следующему разряду
    return ls


def heap_sort(ls):
    """
    Пирамидальная сортировка (Heap Sort).
    Сначала строится двоичная куча (heap), затем элементы извлекаются из нее.
    """

    def max_heapify(ls, heap_size, root_index):
        """
        Преобразует часть списка в максимальную кучу.
        """
        largest = root_index
        left = 2 * root_index + 1  # Левый потомок
        right = 2 * root_index + 2  # Правый потомок

        # Находим наибольший элемент среди корня и потомков
        if left < heap_size and ls[left] > ls[largest]:
            largest = left
        if right < heap_size and ls[right] > ls[largest]:
            largest = right

        # Если наибольший элемент не корень, меняем их местами и рекурсивно преобразуем поддерево
        if largest != root_index:
            ls[root_index], ls[largest] = ls[largest], ls[root_index]
            max_heapify(ls, heap_size, largest)

    n = len(ls)

    # Строим максимальную кучу
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(ls, n, i)

    # Извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        ls[i], ls[0] = ls[0], ls[i]  # Меняем корень (максимум) с последним элементом
        max_heapify(ls, i, 0)  # Преобразуем оставшуюся кучу
    return ls


def merge_sort(ls):
    """
    Сортировка слиянием (Merge Sort).
    Делит список на части, сортирует их рекурсивно и затем объединяет.
    """
    if len(ls) <= 1:  # Базовый случай: список длиной 0 или 1 уже отсортирован
        return ls

    mid = len(ls) // 2  # Делим список пополам
    left = merge_sort(ls[:mid])  # Рекурсивно сортируем левую часть
    right = merge_sort(ls[mid:])  # Рекурсивно сортируем правую часть

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):  # Объединяем два отсортированных списка
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])  # Добавляем оставшиеся элементы
    merged.extend(right[j:])
    return merged


def quicksort(ls):
    """
    Быстрая сортировка (Quick Sort).
    Рекурсивно делит список на меньшие и большие элементы относительно опорного.
    """
    if len(ls) <= 1:  # Базовый случай: список длиной 0 или 1 уже отсортирован
        return ls
    pivot = ls[len(ls) // 2]  # Опорный элемент (средний)
    left = [x for x in ls if x < pivot]  # Элементы меньше опорного
    middle = [x for x in ls if x == pivot]  # Элементы равные опорному
    right = [x for x in ls if x > pivot]  # Элементы больше опорного
    return (
        quicksort(left) + middle + quicksort(right)
    )  # Рекурсивно сортируем и объединяем
