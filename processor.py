import csv
from utils import parse_condition, compare, parse_order_by

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_data(data, condition):
    column, operator, value = parse_condition(condition)

    def matches(row):
        raw = row[column]
        try:
            return compare(float(raw), float(value), operator)
        except ValueError:
            return compare(raw, value, operator)

    return [row for row in data if matches(row)]

def sort_data(data, order_by_arg):
    column, direction = parse_order_by(order_by_arg)
    try:
        data.sort(key=lambda row: float(row[column]), reverse=(direction == "desc"))
    except ValueError:
        data.sort(key=lambda row: row[column], reverse=(direction == "desc"))
    return data
