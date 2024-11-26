class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        hash_index = self.hash_function(key)
        if key not in self.table[hash_index]:
            self.table[hash_index].append(key)

    def display(self):
        for index, items in enumerate(self.table):
            if items:
                print(f"Index {index}: {items}")


def fill_hash_table_from_file(filename, hash_table):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                hash_table.insert(word)


filename = "py\\text.txt"
hash_table = HashTable(5)
fill_hash_table_from_file(filename, hash_table)
print("Содержимое хеш-таблицы:")
hash_table.display()
