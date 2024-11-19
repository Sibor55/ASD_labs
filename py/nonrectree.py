class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal_iterative(root):
    if not root:
        return ""
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(str(node.value))  # Сохранить значение текущего узла
        
        # Важно: сначала добавить правый узел, а затем левый, чтобы в следующий раз обработать левый первым
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return " ".join(result)

# Пример использования:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

print(preorder_traversal_iterative(root))
