import csv

with open('E:\querycsv-redux-4.1.0.tar\dist\querycsv-redux-4.1.0\querycsv\\dim_vendors.csv') as csv_file:
    csv_reader_dim_vendors = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    vendors_map={}
    for row_vendors in csv_reader_dim_vendors:
        vendors_map[row_vendors["id"]]=row_vendors["type"]

with open('E:\querycsv-redux-4.1.0.tar\dist\querycsv-redux-4.1.0\querycsv\\fact_orders.csv') as csv_file:
    csv_reader_fact_orders = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    result_map={}
    for row_orders in csv_reader_fact_orders:
        for vendor in vendors_map.keys():
            if vendor == row_orders["vendor_id"]:
                if row_orders["status"]=='2' or row_orders["status"]=="3":
                    if vendor in result_map.keys():
                        result_map[vendor]+=float(row_orders["amt"])
                    else:
                        result_map[vendor]=float(row_orders["amt"])
    result_map=dict(sorted(result_map.items(), key=lambda item: -item[1]))
    for row in result_map.keys():
        print(row + " " + vendors_map[row] + " " + str(result_map[row]))
    print(result_map)