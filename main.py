import csv
from tabulate import tabulate
from parser import parse_args
from utils import parse_condition, compare

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def filter_data(data, condition):
    column, operator, value = parse_condition(condition)

    # Try to compare as numbers, fallback to strings
    def matches(row):
        raw = row[column]
        try:
            return compare(float(raw), float(value), operator)
        except ValueError:
            return compare(raw, value, operator)

    return [row for row in data if matches(row)]

def main():
    args = parse_args()
    data = read_csv(args.file)

    if args.where:
        data = filter_data(data, args.where)
    print(tabulate(data, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
