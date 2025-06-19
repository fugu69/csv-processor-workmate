import csv
from tabulate import tabulate
from parser import parse_args

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def main():
    args = parse_args()
    data = read_csv(args.file)
    print(tabulate(data, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
