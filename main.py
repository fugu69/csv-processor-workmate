import csv
from tabulate import tabulate
from parser import parse_args
from utils import parse_condition, compare, parse_aggregate, aggregate, parse_order_by

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

    if args.order_by:
        column, direction = parse_order_by(args.order_by)
        try:
            data.sort(key=lambda row: float(row[column]), reverse=(direction == "desc"))
        except ValueError:
            data.sort(key=lambda row: row[column], reverse=(direction == "desc"))

    if args.aggregate:
        column, operation = parse_aggregate(args.aggregate)
        try:
            values = [float(row[column]) for row in data]
        except ValueError:
            print(f"Aggregation only works with numeric columns. '{column}' is not numeric.")
            return
        result = aggregate(values, operation)
        print(f"{operation.upper()} of {column}: {result}")
    else:
        print(tabulate(data, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
