# swahili2words/cli.py

import argparse
from .converter import number_to_swahili

def main():
    parser = argparse.ArgumentParser(description="Convert numbers into Swahili words.")
    parser.add_argument("number", help="The number to convert (e.g., 12345 or 12.50)")
    parser.add_argument("--currency", action="store_true", help="Format as currency (shilingi/senti)")

    args = parser.parse_args()

    try:
        num = float(args.number) if "." in args.number else int(args.number)
        result = number_to_swahili(num, as_currency=args.currency)
        print(result)
    except ValueError:
        print("⚠️ Tafadhali ingiza nambari halali.")
