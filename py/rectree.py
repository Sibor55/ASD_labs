"""
(https://en.wikipedia.org/wiki/Tree_traversal)
Pre-order, NLR

    Visit the current node (in the figure: position red).
    Recursively traverse the current node's left subtree.
    Recursively traverse the current node's right subtree.

The pre-order traversal is a topologically sorted one, because a parent node is processed before any of its child nodes is done.
Post-order, LRN

    Recursively traverse the current node's left subtree.
    Recursively traverse the current node's right subtree.
    Visit the current node (in the figure: position blue).

Post-order traversal can be useful to get postfix expression of a binary expression tree.
In-order, LNR

    Recursively traverse the current node's left subtree.
    Visit the current node (in the figure: position green).
    Recursively traverse the current node's right subtree.

In a binary search tree ordered such that in each node the key is greater than
all keys in its left subtree and less than all keys in its right subtree,
in-order traversal retrieves the keys in ascending sorted order
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
