import csv
import sys
import pytest

with open(sys.argv[1]) as csv_file_vendors:
    csv_reader_dim_vendors = csv.DictReader(csv_file_vendors, delimiter=',')
    vendors_map={}
    for row_vendors in csv_reader_dim_vendors:
        vendors_map[row_vendors["id"]]=row_vendors["type"]

with open(sys.argv[2]) as csv_file_orders:
    csv_reader_fact_orders = csv.DictReader(csv_file_orders, delimiter=',')
    result_map={}
    for row_orders in csv_reader_fact_orders:
        for vendor in vendors_map.keys():
            if vendor == row_orders["vendor_id"]:
                if row_orders["status"] in ['2','3']:
                    if vendor in result_map.keys():
                        result_map[vendor]+=float(row_orders["amt"])
                    else:
                        result_map[vendor]=float(row_orders["amt"])
    result_map=dict(sorted(result_map.items(), key=lambda item: -item[1]))
    for row in result_map.keys():
        print(row + " " + vendors_map[row] + " " + str(result_map[row]))
        
def test_file_check():
    assert csv_file_vendors and csv_file_orders
