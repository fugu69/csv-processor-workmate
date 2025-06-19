from tabulate import tabulate
from parser import parse_args
from utils import parse_aggregate, aggregate
from processor import read_csv, filter_data, sort_data

def main():
    args = parse_args()
    data = read_csv(args.file)

    if args.where:
        data = filter_data(data, args.where)

    if args.order_by:
        data = sort_data(data, args.order_by)

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
