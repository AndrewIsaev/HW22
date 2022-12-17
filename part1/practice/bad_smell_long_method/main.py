# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read_csv(csv_string) -> list:
    return [x.split(';') for x in csv.split('\n')]


def _sort_data(data):
    return sorted(data, key=lambda x: int(x[1]))


def _filter_data(data):
    return [x for x in data if int(x[1]) > 10]


def get_users_list():
    data = _read_csv(csv)
    sort_data = _sort_data(data)
    filter_data = _filter_data(sort_data)
    return filter_data


if __name__ == "__main__":
    print(_sort_data(_read_csv(csv)))
    print(get_users_list())
