# Задание 14


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        hash_index = self.hash_function(key)
        print(key, hash_index)
        # Избегаем дубликаты
        if key not in self.table[hash_index]:
            self.table[hash_index].append(
                key
            )  # Добавляем ключ в соответствующий список

    def display(self):
        for index, items in enumerate(self.table):
            if items:
                print(f"Index {index}: {items}")


# Чтение и заполнение
def fill_hash_table_from_file(filename, hash_table):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.strip().split()  # Разбиваем строку на слова
            for word in words:
                hash_table.insert(word)  # Вставляем каждое слово в хеш-таблицу


# Основная часть

filename = "py\\text.txt"
hash_table = HashTable(30)
fill_hash_table_from_file(filename, hash_table)  # Заполняем хеш-таблицу
print("Содержимое хеш-таблицы:")
hash_table.display()
