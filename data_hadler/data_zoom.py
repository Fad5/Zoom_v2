from datetime import date, datetime, timedelta
from typing import List, Dict


def create_file_report(data) -> None:
    """
    Добавления в файл report_date.txt отчет о обновления exel файла

    return: None
    """
    with open('report_date.txt', 'a', encoding='utf-8') as f:
        f.write(data)


def start_weekday() -> date:
    """
    Функция, которая возвращает дату текущего понедельника

    return: start_week - дата текущего понедельника
    """
    current_day = date.today()
    weeks = current_day.weekday()
    start_week = current_day - timedelta(days=weeks)
    return start_week


def week(argument: str) -> tuple[date, date]:
    """
    Функция возвращает начало и конец недели в зависимости от argument,
    она работает с текущей, прошлой и будущей. Функйия получит начало этой недели
    и уже либо прибавляет 7 дней или убавляет для нахождения начало прошлой или будущей.

    - argument - ключ слова для получения значения(next, last, current)

    return: start_week, finish_week - (datetime.date(year, month, day), datetime.date(year, month, day))
    """
    data_kay = {'next': [13, 7], 'last': [1, 7], 'current': [0, 6]}
    current_day = date.today()
    weeks = current_day.weekday()
    start_week = current_day - timedelta(days=weeks)
    finish_week = start_week + timedelta(days=data_kay[argument][0])
    start_week = start_weekday() + timedelta(days=data_kay[argument][1])
    return start_week, finish_week


def days(argument: str, day: int = 1, current_day: date = date.today()) -> date:
    """
    Функция для получения даты текущего, прошлого и будующего дня в формате
    datetime.date в зависимости от argument

    Аргументы: 
    - argument - (next, last,' ') - получение дня в зависимости от того что написано:
       по умолчанию текущия день,
       next - следующий, 
       last - прошлый

    return: datetime.date 
    """
    create_file_report(f'{current_day} | {datetime.now()} \n')
    if argument == 'next':
        next_day = date.today() + timedelta(days=day)
        return next_day
    elif argument == 'last':
        last_day = date.today() - timedelta(days=day)
        return last_day
    else:
        return date.today()


def days_for_week(argument: str = 'today', day: int = 1, current_day: date = date.today()) -> date:
    """
    Получение текущего, прошлого и будующего дня в формате datetime,
    в зависимости от argument

    - argument - без аргумента сегодняя,
        next - дата завтрошний дня
        last - дата вчеранего дня
    return: день в формате datetime ()
    """
    if argument == 'next':
        next_day = current_day + timedelta(days=day)
        return next_day
    elif argument == 'last':
        last_day = current_day - timedelta(days=day)
        return last_day
    else:
        return current_day


def list_work_day() -> List:
    """
    Функция создает список в который будут входить 3 спиcка состоящие из
    дней недели текущей, будущей и прошлой

    return: список список дней текущей, будущей и прошлой недели
      [[last_week_days],[current_week_days],[next_week_days]]
    """

    full_list_day = []
    arguments = ['last', 'current', 'next']
    for argument in arguments:
        data = week(argument)
        start_week = data[0]
        list_day = []
        for i in range(0, 7):
            number_day = days_for_week('next', current_day=start_week, day=i)
            list_day.append(number_day)
        full_list_day.append(list_day)
    return full_list_day
