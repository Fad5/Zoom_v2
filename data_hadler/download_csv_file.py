import datetime
import os

import pandas as pd
import threading
from pathlib import Path


def create_cvs_file() -> None:
    """
    Функция забирает онлайн таблицу google, проходится pandas и создает csv с данными
    :return: None
    """
    df = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/1vZc0LfpNmLZKnvn4EiEeD-HTZE5UJ2wBZX5fOF6FtBk/export?format=csv')
    column_names = df.keys().tolist()

    new_df = df[
        [column_names[0], column_names[1], column_names[2], column_names[3], column_names[4], column_names[5],
         column_names[6], column_names[7], column_names[8],
         column_names[9], column_names[10], column_names[11], column_names[12], column_names[13],
         column_names[14]]]  # Выберем из даты фрейма столбцы и сохраним в новый дате фрейм
    new_df.to_csv('data_base.csv', index=False)  # Экспорт в CSV файл
    print('Successful')
    threading.Timer(1800, create_cvs_file).start()


def get_info_last_download():
    base_dir = Path(__file__).resolve().parent.parent
    path_file = f'{base_dir}/data_base.csv'
    time_create_file = os.path.getmtime(path_file)
    date_time = str(datetime.datetime.fromtimestamp(time_create_file))
    return 'Полследнее обновление: ' + date_time[:-7]
