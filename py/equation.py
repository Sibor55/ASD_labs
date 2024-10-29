def find_numbers(x):
    results = []
    k = 0
    while 3**k <= x:
        l = 0
        while 3**k * 5**l <= x:
            m = 0
            while 3**k * 5**l * 7**m <= x:
                if 3**k * 5**l * 7**m == x:
                    results.append((k, l, m))
                m += 1
            l += 1
        k += 1
    return results


x = int(input("Введите число x: "))
results = find_numbers(x)
if results:
    print(f"Числа, удовлетворяющие условию для x={x}:")
    for k, l, m in results:
        print(f"k={k}, l={l}, m={m}")
else:
    print(f"Нет чисел, удовлетворяющих условию для x={x}.")
