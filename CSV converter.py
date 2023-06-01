import csv
import argparse
from collections import OrderedDict
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#read through the input. Added error handling for ease of use.
def read_csv(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        logging.info(f"Successfully read file: {filename}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        return []
    except Exception as e:
        logging.error(f"Error reading file {filename}: {e}")
        return []
#write the output. This should subjectivize the output.

def write_csv(filename, data, fields):
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"Successfully wrote to file: {filename}")
    except Exception as e:
        logging.error(f"Error writing to file {filename}: {e}")

def assign_numerical_variables(data, field):
    if not data or field not in data[0]:
        logging.warning(f"Field not found: {field}")
        return

    # Assign numerical variables to the values in the given field
    value_to_num = OrderedDict()
    for row in data:
        value = row[field]
        if value not in value_to_num:
            value_to_num[value] = len(value_to_num) + 1
        row[field] = value_to_num[value]
    logging.info(f"Assigned numerical variables to field: {field}")

def main(args):
    # Read the input CSV file
    data = read_csv(args.input)

    if not data:
        logging.error("No data found. Please check your input file.")
        return

    # Assign numerical variables to the specified fields
    for field in args.fields:
        assign_numerical_variables(data, field)

    # Write the modified data to the output CSV file
    write_csv(args.output, data, data[0].keys())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='Input CSV file')
    parser.add_argument('-o', '--output', required=True, help='Output CSV file')
    parser.add_argument('-f', '--fields', nargs='+', required=True, help='Fields to assign numerical variables to')
    args = parser.parse_args()
    main(args)