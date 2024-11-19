class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parse_tree(expression):
    """Парсинг линейно-скобочной строки формата 8(3(1,6(4,7)),10(,14(13,)))."""

    def helper(index):
        # Чтение числа (значения узла)
        start = index
        while index < len(expression) and (
            expression[index].isdigit() or expression[index] == "-"
        ):
            index += 1
        value = int(expression[start:index])

        node = TreeNode(value)

        # Проверка наличия дочерних элементов
        if index < len(expression) and expression[index] == "(":
            index += 1  # Пропустить '('

            # Левый потомок
            if expression[index] != ",":
                node.left, index = helper(index)

            # Пропустить запятую
            if index < len(expression) and expression[index] == ",":
                index += 1

            # Правый потомок
            if index < len(expression) and expression[index] != ")":
                node.right, index = helper(index)

            index += 1  # Пропустить ')'

        return node, index

    tree, _ = helper(0)
    return tree


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Добавление узла в дерево."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        elif value > node.value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

    def search(self, value):
        """Поиск узла в дереве."""
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def delete(self, value):
        """Удаление узла из дерева."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:  # Найден узел
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Найти минимальное значение в правом поддереве
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def to_string(self):
        """Преобразование дерева в линейно-скобочную запись."""
        return self._to_string(self.root)

    def _to_string(self, node):
        if not node:
            return ""
        left = self._to_string(node.left)
        right = self._to_string(node.right)
        return f"{node.value}({left},{right})" if left or right else f"{node.value}"


# --- Основная программа ---
tree = BinarySearchTree()

print(
    "Введите дерево в линейно-скобочной записи (пример: 8(3(1,6(4,7)),10(,14(13,)))):"
)
input_tree = input()
tree.root = parse_tree(input_tree)

while True:
    print("\nМеню:")
    print("1. Добавить узел")
    print("2. Удалить узел")
    print("3. Найти узел")
    print("4. Вывести дерево в линейно-скобочной записи")
    print("0. Выход")
    choice = input("Введите номер операции: ")

    if choice == "1":
        value = int(input("Введите значение для добавления: "))
        tree.insert(value)
    elif choice == "2":
        value = int(input("Введите значение для удаления: "))
        tree.delete(value)
    elif choice == "3":
        value = int(input("Введите значение для поиска: "))
        found = tree.search(value)
        print("Найдено" if found else "Не найдено")
    elif choice == "4":
        print("Текущее дерево:", tree.to_string())
    elif choice == "0":
        print("Текущее дерево перед выходом:", tree.to_string())
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
