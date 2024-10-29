# Пункт 1: В строке будут скобки только одного типа: или "()" , или "{}", или "[]"
# Пункт 2: В строке будут все три вида скобок
# Для успешной сдачи лабы оба пункта программа должна выполнять корректно (можно сделать отдельные программы на каждый пункт)

# Пример входа:
# ()[({}())]

def bracketcheck(string):
    brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in string:
        # print(stack)
        if i in brackets.values():
            stack.append(i)
        elif i in brackets.keys():
            if stack == [] or brackets[i] != stack.pop():
                return False
    return True if not stack else False


if __name__ == "__main__":
    
    
    brackettest = input("Введите строку: ")
    print(f"Строка{" не" if not bracketcheck(brackettest) else ""} существует")