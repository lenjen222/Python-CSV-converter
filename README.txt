Sales Report Generator

Abstract:
This Python program reads data from three CSV files (In this case TeamMap.csv, ProductMaster.csv, Sales.csv), processes it, and produces two output CSV files (In this case TeamReport.csv, ProductReport.csv).

Requirements
Python 3 or higher

Installation
No additional packages are needed to run this script.

Usage
This program takes 5 command line arguments:

-t or --team: The path to the TeamMap.csv file
-p or --product: The path to the ProductMaster.csv file
-s or --sales: The path to the Sales.csv file
--team-report: The path where the TeamReport.csv output file should be written
--product-report: The path where the ProductReport.csv output file should be written


run the program like this:
python3 report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report=TeamReport.csv --product-report=ProductReport.csv

(If using different CSVs, replace the CSV filenames with the path to your actual CSV files.)


Input Files:
TeamMap.csv: Contains two values per line, a team ID and the team name.
ProductMaster.csv: Contains information about a product. Each line contains the product ID, name, price per unit, and lot size.
Sales.csv: Contains information about each sale. Each line contains the sale ID, product ID, team ID, quantity sold, and discount percentage.


Output Files:
TeamReport.csv: Contains two values per line, the team name, and the total gross revenue of the team’s sales.
ProductReport.csv: Each line contains the product name, gross revenue from sales of the product, total number of units sold, and the total cost of all discounts provided on the product.
While the code focuses on these named files, the code will soon be tweaked to allow any number of file arguements and file names. The data processing will be next in the near future.
