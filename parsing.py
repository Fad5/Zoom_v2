import csv
from typing import Any
from data_hadler import days_for_week


def get_info_work_day() -> list[dict[str | Any, str | Any]]:
    """
    Функция, которая получает имя пользователя и потом проходиься по
    csv файлу и помещает в js файл
    :param user: как записан в exel файле 
    :return:
    """
    name_file = 'data_base'
    js = []
    with open(f'{name_file}.csv', newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        for row in reader:
            js.append({
                '#': row[0].replace('\n', ' '),
                'Program': row[1].replace('\n', ' '),
                'Modul': row[2].replace('\n', ' '),
                'Data': row[3],
                'Time': row[4].replace(' ', '').replace('.', ':'),
                'Watch': row[5].replace('\n', ' '),
                'Item': row[6].replace('\n', ' '),
                'Comment': row[8].replace('\n', ' '),
                'Teacher': row[7].replace('\n', ' '),
                'Note': row[9],
                'Audience': row[10].replace('\n', ' '),
                'Webinar link': row[11].replace('\n', ' '),
                'Link to post': row[12].replace('\n', ' '),
                'Operator': row[13].replace('\n', ' '),
                'Account': row[14].replace('\n', ' '),
                'Hours': row[4]
            })
    return js


# Функции для того что бы переобразовать дату

def data_formating(date_ : str) -> str:
    """ Функция преднозначена для форматирования даты
    Args:
        date_ = дата не прошедшая форматирования

    Returns:
        date - отформатированная дата 
    """
    date_split = date_.split('.')
    date = f'{date_split[2]}-{date_split[1]}-{date_split[0]}'
    return date 

# Вывод 
def show_zoom(work_day):
                description_for_show_work_day = (
                f"👨Преподаватель:"
                f" {(work_day['Teacher'])}\n🗓Дата: "
                f"{work_day['Data']}\n🕐Время: {work_day['Time']}\n❗Примечание: {work_day['Note']}\n📌Оператор:"
                f" {work_day['Operator']}\n🔒Аккаунт: {work_day['Account']}.")
                return description_for_show_work_day

def split_user_zoom(user_name):
    if '|' in user_name:
        user_name_split = user_name.split('|')
        return user_name_split
    else:
        [user_name]


def get_info_zooms(user_name, day_:str = 'current'):
    list_zooms = []
    user_name = split_user_zoom(user_name)
    date_ = days_for_week(argument=day_)
    data = get_info_work_day()
    if user_name == None:
        return ['Вас нет в базе данных!!!']
    for i in data:
        if i["Operator"] in user_name:
            print(i['Operator'])
            print(data_formating(i['Data']))
            if str(date_) == data_formating(i['Data']):
                list_zooms.append(show_zoom(i))
    if not list_zooms:
        return ['У вас выходной!']
    return list_zooms


def show_current_week():
    pass





