import argparse
import csv
from collections import defaultdict

def main(args):
    # Reading from input files
    team_map = read_csv(args.team, ['TeamId', 'Name'])
    product_master = read_csv(args.product, ['ProductId', 'Name', 'Price', 'LotSize'])
    sales = read_csv(args.sales, ['SaleId', 'ProductId', 'TeamId', 'Quantity', 'Discount'])

    # Create default dictionaries to store total sales for teams and products
    team_sales = defaultdict(float)
    product_sales = defaultdict(float)
    product_units = defaultdict(int)
    product_discounts = defaultdict(float)

    # Calculate total sales
    for sale in sales:
        product_id = sale['ProductId']
        team_id = sale['TeamId']
        quantity = int(sale['Quantity'])
        discount = float(sale['Discount'])
        # Find the corresponding product
        for product in product_master:
            if product['ProductId'] == product_id:
                # Calculate gross revenue (not reduced by the discounts)
                price_per_unit = float(product['Price'])
                lot_size = int(product['LotSize'])
                gross_revenue = price_per_unit * lot_size * quantity
                team_sales[team_id] += gross_revenue
                product_sales[product_id] += gross_revenue
                product_units[product_id] += lot_size * quantity
                product_discounts[product_id] += gross_revenue * discount / 100
                break

    # Write to output files
    write_team_csv(args.team_report, team_map, team_sales, 'TeamId')
    write_product_csv(args.product_report, product_master, product_sales, product_units, product_discounts, 'ProductId')

def read_csv(filename, fieldnames):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, fieldnames=fieldnames)
        data = list(reader)
    return data

def write_team_csv(filename, data, sales, id_field):
    with open(filename, 'w', newline='') as f:
        fieldnames = ['Team', 'GrossRevenue']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        # Sort teams by gross revenue in descending order
        sorted_data = sorted(data, key=lambda x: sales[x[id_field]], reverse=True)
        for row in sorted_data:
            writer.writerow({'Team': row['Name'], 'GrossRevenue': sales[row[id_field]]})

def write_product_csv(filename, data, sales, units, discounts, id_field):
    with open(filename, 'w', newline='') as f:
        fieldnames = ['Name', 'GrossRevenue', 'TotalUnits', 'DiscountCost']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        # Sort products by gross revenue in descending order
        sorted_data = sorted(data, key=lambda x: sales[x[id_field]], reverse=True)
        for row in sorted_data:
            writer.writerow({'Name': row['Name'], 'GrossRevenue': sales[row[id_field]], 
                             'TotalUnits': units[row[id_field]], 'DiscountCost': discounts[row[id_field]]})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--team', required=True, help='Team Map file')
    parser.add_argument('-p', '--product', required=True, help='Product Master file')
    parser.add_argument('-s', '--sales', required=True, help='Sales file')
    parser.add_argument('--team-report', required=True, help='Team Report file')
    parser.add_argument('--product-report', required=True, help='Product Report file')
    args = parser.parse_args()
    main(args)