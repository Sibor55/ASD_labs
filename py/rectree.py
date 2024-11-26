"""
(https://en.wikipedia.org/wiki/Tree_traversal)
"""


class TreeNode:()
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parse_tree(expression):
    """Парсинг линейно-скобочной строки и создание дерева."""

    def helper(index):
        # Чтение числа (значения узла)
        start = index
        while index < len(expression) and (
            expression[index].isdigit() or expression[index] == "-"
        ):
            index += 1
        value = int(expression[start:index])

        node = TreeNode(value)

        # Если дальше идет левая и правая часть (в скобках)
        if index < len(expression) and expression[index] == "(":
            index += 1  # Пропустить '('
            if expression[index] != ",":
                node.left, index = helper(index)  # Создаем левое поддерево
            if expression[index] == ",":
                index += 1  # Пропустить ','
            if expression[index] != ")":
                node.right, index = helper(index)  # Создаем правое поддерево
            index += 1  # Пропустить ')'

        return node, index

    tree, _ = helper(0)
    return tree


def preorder_traversal(node):
    """Прямой (preorder) обход."""
    if node is None:
        return []
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)


def inorder_traversal(node):
    """Центральный (inorder) обход."""
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)


def postorder_traversal(node):
    """Концевой (postorder) обход."""
    if node is None:
        return []
    return (
        postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]
    )


# Пример использования
expression = "8(3(1,6(4,7)),10(,14(13,)))"
tree = parse_tree(expression)

print("Прямой обход (preorder):", preorder_traversal(tree))
print("Центральный обход (inorder):", inorder_traversal(tree))
print("Концевой обход (postorder):", postorder_traversal(tree))
