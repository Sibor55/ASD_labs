# На вход подаётся математическое выражение. Элементы - числа.
# Операции - "+ - * /".
# Также есть скобочки. Окончанием выражения служит "=".
# Программа должна вывести результат выражения
# Пример ввода:
# 2+7*(3/9)-5=

# https://en.wikipedia.org/wiki/Reverse_Polish_notation
# Воспользовался обратной польской записью
# и прошлой программой для проверки скобок

from brackets import bracketcheck

operator_list = ["*", "/", "+", "-"]
digit_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Приоритет операторов
def precedence(op):
    if op in ("+", "-"):
        return 1
    elif op in ("*", "/"):
        return 2
    return 0


# Операции
def sum(operands):
    return float(operands[0]) + float(operands[1])


def sub(operands):
    return float(operands[0]) - float(operands[1])


def mult(operands):
    return float(operands[0]) * float(operands[1])


def division(operands):
    return float(operands[0]) / float(operands[1])


# Преобразование в обратную польскую нотацию (RPN)
def RPN(expression):
    if not bracketcheck(expression):
        return ["PError"]

    stack = []
    output = []
    number_buffer = ""

    while expression:
        token = expression[0]
        expression = expression[1:]

        if token in digit_list:
            # Сохраняем цифры для многозначных чисел
            number_buffer += token

        else:
            if number_buffer:
                # Если накопились цифры, добавляем их как число в output
                output.append(number_buffer)
                number_buffer = ""

            if token in operator_list:
                # Пока последний элемент - оператор с высшим приоритетом
                while (
                    stack
                    and stack[-1] in operator_list
                    and precedence(stack[-1]) >= precedence(token)
                ):
                    output.append(stack.pop())  # Выталкиваем операторы в строку
                stack.append(token)  # Добавляем текущий оператор в стек

            elif token == "(":
                stack.append(token)  # Открытые скобки в стек

            elif token == ")":
                # Выталкиваем все до открывающей скобки
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()  # Убираем "("

    
    if number_buffer:
        output.append(number_buffer)  # Добавляем последнее накопленное число
    # Выталкиваем оставшиеся операторы из стека
    while stack:
        output.append(stack.pop())

    return output


# Основная функция вычисления
def Calc(expr):
    rpn_expr = RPN(expr)
    print(rpn_expr)  # Отладка, для понимания полученной RPN

    if rpn_expr[0] == "PError":
        return "Ошибка в скобках"

    stack = []
    for token in rpn_expr:
        if token.isdigit():
            stack.append(token)  # Если число, добавляем в стек
        elif token in operator_list:
            # Выполняем операцию с двумя верхними элементами стека
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(sum([a, b]))
            elif token == "-":
                stack.append(sub([a, b]))
            elif token == "*":
                stack.append(mult([a, b]))
            elif token == "/":
                if b == "0":  # Проверка на деление на 0
                    return "Деление на ноль"
                stack.append(division([a, b]))

    return stack[0]  # Возвращаем результат


# Пример использования
expression = input("Введите выражение: ")

if expression.endswith("="):
    expression = expression[:-1]

print(f"{expression} = {Calc(expression)}")
