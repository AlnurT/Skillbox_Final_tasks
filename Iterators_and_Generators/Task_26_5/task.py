"""Задача 5. Количество строк

Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и
вычисляет общее количество строк кода, игнорируя пустые строки и строчки комментариев.
"""
import os


def build_generator_line_work_code(pyfile: str):
    with open(pyfile, encoding="utf-8") as file:
        doc_str = False
        for line in file:
            line = line.replace("\n", "#").strip()
            if line.startswith('"""') or doc_str:
                doc_str = True
            elif not line.startswith("#"):
                yield 1
            if line.endswith('"""#'):
                doc_str = False


def calculate_number_of_lines_in_pyfiles(path: str):
    for _, _, files in os.walk(path):
        pyfiles = (file for file in files if file.endswith(".py"))
        for pyfile in pyfiles:
            yield sum(build_generator_line_work_code(pyfile))


def main():
    path = r"C:\Python_Projects\Skillbox_Final_tasks\Iterators_and_Generators\Task_26_5"
    total_lines = sum(calculate_number_of_lines_in_pyfiles(path))
    print(total_lines)


if __name__ == "__main__":
    main()
