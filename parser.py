import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="CSV file processor")
    parser.add_argument("--file", required=True, help="Path to the CSV file")
    parser.add_argument("--where", help='Filter condition, e.g. "price>300"')
    parser.add_argument("--aggregate", help='Aggregate data, e.g. "price=avg"')
    
    return parser.parse_args()
