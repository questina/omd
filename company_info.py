import math
from typing import Dict, Optional

COMPANY_CSV_PATH = './Corp_Summary.csv'
REVIEW_CSV_PATH = './Department_review.csv'
HEADER = ['ФИО полностью', 'Департамент', 'Отдел', 'Должность', 'Оценка', 'Оклад']
DEPARTMENT_REVIEW_HEADER = ['Департамент', 'Численность', 'Вилка зарплат', 'Средняя зарплата']
SALARY_COLUMN_IDX = HEADER.index('Оклад')
DEPARTMENT_COLUMN_IDX = HEADER.index('Департамент')
TEAM_COLUMN_IDX = HEADER.index('Отдел')


class DepartmentInfo:
    """
    Вспомогательный класс, который хранит в себе информацию о департаменте.
    Он содержит в себе название департамента, названия всех команд внутри него,
    кол-во работников, минимальную и максимальную зарплаты,
    среднюю зарплату по департаменту.
    """
    def __init__(self, department_name: str) -> None:
        self.name: str = department_name
        self.teams: set = set()
        self.workers_number: int = 0
        self.min_salary: float = math.inf
        self.max_salary: float = 0
        self.sum_salary: float = 0

    def add_department_worker_info(self, salary: float, team_name: str) -> None:
        """
        Метод класса добавляет и обновляет новую информацию про работника департамент.
        :param salary: зарплата работника.
        :param team_name: название команды работника.
        """
        self.workers_number += 1
        self.teams.add(team_name)
        self.min_salary = min(self.min_salary, salary)
        self.max_salary = max(self.max_salary, salary)
        self.sum_salary += salary

    @property
    def avg_salary(self) -> float:
        """
        Метод высчитывает среднюю зарплату.
        :return: средняя зарплата.
        """
        return self.sum_salary / self.workers_number


def read_department_file(csv_file_path: str) -> Dict[str, DepartmentInfo]:
    """
    Функция считывает csv файл и собирает информацию про департаменты.
    :param csv_file_path: путь до csv файла;
    :return: словарь, где ключом явлется имя департамента, а значением класс DepartmentInfo,
    в котором лежит кумулятивная информация по департаменту.
    """
    with open(csv_file_path, 'r') as csv_file:
        csv_file.readline()  # skipping line with header
        departments_data = {}
        for line in csv_file.readlines():
            row = line.strip().split(';')
            department_name = row[DEPARTMENT_COLUMN_IDX]
            salary = float(row[SALARY_COLUMN_IDX])
            team = row[TEAM_COLUMN_IDX]
            if department_name not in departments_data:
                departments_data[department_name] = DepartmentInfo(department_name)
            departments_data[department_name].add_department_worker_info(salary, team)
    return departments_data


def convert_department_info_to_csv_str(department_info: DepartmentInfo, delimiter: str = ';') -> str:
    """
    Функция конвертирует информацию про каждый департамент в одну строчку csv файла.
    Строчка содержит в себе информацию про название департамента, численность,
    зарплатную вилку, среднюю зарплату.
    :param department_info: данные о департаменте.
    :param delimiter: разделитель в csv файл.
    :return: Строка в формате csv.
    """
    salary = f'{department_info.min_salary} - {department_info.max_salary}'
    return delimiter.join(
        [
            department_info.name,
            str(department_info.workers_number),
            salary,
            str(round(department_info.avg_salary, 2)),
        ]
    ) + '\n'


def make_str_for_department_review(department_info: Dict[str, DepartmentInfo], delimiter: str = ';') -> str:
    """
    Функция формирует общую строку со всей информацией по каждому департаменту в формате:
    заголовок + строчки с информацией о каждом департаменте, разделенные delimiter.
    :param department_info: информация по департаментам.
    :param delimiter: разделитель между строчками с информацией об одном департаменте.
    :return: Общая строка с полной информацией по всем департаментами.
    """
    whole_review_str = delimiter.join(DEPARTMENT_REVIEW_HEADER) + '\n'
    for department in department_info:
        whole_review_str += convert_department_info_to_csv_str(department_info[department], delimiter=delimiter)
    return whole_review_str


def write_department_review_file(csv_file_path: str, departments_data: Dict[str, DepartmentInfo]) -> None:
    """
    Функция записывает в csv файл собранную информацию по департаментам.
    :param csv_file_path: путь до csv файла.
    :param departments_data: информация по департаментам.
    """

    with open(csv_file_path, 'w') as csv_file:
        csv_file.write(make_str_for_department_review(departments_data))


def print_department_hierarchy(department_info: Dict[str, DepartmentInfo]) -> None:
    """
    Функция выводит в стандартный вывод иерархию компании в виде названия департамента
    и названия команд, содержащихся в нем.
    :param department_info: информация по департаментам.
    """
    for department in department_info:
        print(f'- {department}')
        for team in department_info[department].teams:
            print(f'  - {team}')


def print_department_review(department_info: Dict[str, DepartmentInfo]) -> None:
    """
    Функция выводит в стандартный вывод собранную информацию по каждому департаменту:
    название департамента, численность, зарплатная вилка, средняя зарплата.
    :param department_info: информация по департаментам.
    """
    print(make_str_for_department_review(department_info, delimiter=', '), end='')


def process_input(user_input: str) -> Optional[int]:
    """
    Функция валидирует ввод пользователя и приводит его к int, если ввод корректен.
    :param user_input: ввод пользователя.
    :return: ввод пользователя в формате целого числа или None, если ввод некорректен.
    """
    if user_input.isdigit():
        user_input = int(user_input)
        if 1 <= user_input <= 3:
            return user_input
    print('Пожалуйста введите цифру от 1 до 3!')
    return None


def main():
    departments = read_department_file(COMPANY_CSV_PATH)
    while True:
        print('Выберите что хотите сделать и введите соответствующую цифру\n\n'
              '1. Вывести в понятном виде иерархию команд.\n'
              '2. Вывести сводный отчёт по департаментам: название, численность, '
              '"вилка" зарплат в виде мин – макс, среднюю зарплату.\n'
              '3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла.')
        user_choice = process_input(input())
        if user_choice is not None:
            if user_choice == 1:
                print_department_hierarchy(departments)
            elif user_choice == 2:
                print_department_review(departments)
            else:
                write_department_review_file(REVIEW_CSV_PATH, departments)
                print(f'Сохранил файл по пути {REVIEW_CSV_PATH}')
        print()


if __name__ == '__main__':
    main()
