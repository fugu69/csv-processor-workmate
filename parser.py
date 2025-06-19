import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="CSV file processor")
    parser.add_argument("--file", required=True, help="Path to the CSV file")
    return parser.parse_args()
