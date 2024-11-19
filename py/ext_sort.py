import os
import tempfile
import heapq


def external_sort(input_file, output_file, chunk_size):
    temp_files = []

    total_input_lines = 0
    total_output_lines = 0

    # 1. Чтение и сортировка блоков
    with open(input_file, "r") as f:
        while True:
            lines = []
            for _ in range(chunk_size):
                line = f.readline()
                if not line:
                    break
                stripped_line = line.strip()
                if stripped_line:  # Убедимся, что строка не пустая
                    lines.append(int(stripped_line))
                    total_input_lines += 1
            if not lines:
                break
            lines.sort()
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w+")
            temp_file.writelines(f"{line}\n" for line in lines)
            temp_file.close()
            temp_files.append(temp_file.name)

    # 2. Слияние отсортированных временных файлов
    with open(output_file, "w") as out_file:
        min_heap = []
        file_pointers = [open(temp_file, "r") for temp_file in temp_files]

        # Инициализация кучи
        for i, fp in enumerate(file_pointers):
            line = fp.readline()
            if line:
                heapq.heappush(min_heap, (int(line.strip()), i))

        # Слияние
        while min_heap:
            smallest, file_index = heapq.heappop(min_heap)
            out_file.write(f"{smallest}\n")
            total_output_lines += 1
            line = file_pointers[file_index].readline()
            if line:
                heapq.heappush(min_heap, (int(line.strip()), file_index))

        # Закрываем все файловые указатели
        for fp in file_pointers:
            fp.close()

    # Удаление временных файлов
    for temp_file in temp_files:
        os.remove(temp_file)

    # Отладка: вывод количества строк
    print(f"Строк в инпуте: {total_input_lines}")
    print(f"Строк в аутпуте: {total_output_lines}")


# Пример использования
input_file = "py\\large_input.txt"
output_file = "sorted_output.txt"
chunk_size = 25  # Количество строк, которое можно загрузить в память одновременно

external_sort(input_file, output_file, chunk_size)
