# Задание 13


# Определяем хеш-таблицу
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]  # Создаем список списков

    def hash_function(self, key):
        # Простая хеш-функция (например, сумма кодов символов)
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        hash_index = self.hash_function(key)

        if self.table[hash_index] is None:
            self.table[hash_index] = key
            return

        # Квадратичная пробировка
        i = 1
        while self.table[hash_index] is not None:
            new_index = (hash_index + i * i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
            i += 1

    def display(self):
        for index, items in enumerate(self.table):
            if items:
                print(f"Index {index}: {items}")


# Функция для чтения файла и заполнения хеш-таблицы
def fill_hash_table_from_file(filename, hash_table):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.strip().split()  # Разбиваем строку на слова
            for word in words:
                hash_table.insert(word)  # Вставляем каждое слово в хеш-таблицу


# Основная часть

filename = "py\\text.txt"  # Укажите имя вашего файла
print("1")
hash_table = HashTable(30)  # Создаем хеш-таблицу с размером 10
print("2")
fill_hash_table_from_file(filename, hash_table)  # Заполняем хеш-таблицу
print("Содержимое хеш-таблицы:")
hash_table.display()  # Выводим содержимое хеш-таблицы
