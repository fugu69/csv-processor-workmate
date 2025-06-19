import csv
from tabulate import tabulate

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def main():
    file_path = "products.csv"  # TO-DO: make it dynamic later
    data = read_csv(file_path)
    print(tabulate(data, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
