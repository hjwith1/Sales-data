import statistics

sales_data = [6226,1521,1842,2051,1728,2138,7479,4434,3615,5472,7224,1812]
print("total=",sum(sales_data))
print("median=",statistics.median(sales_data))
print("average=",statistics.mean(sales_data))
print("maximum sales in 1 month=",max(sales_data))
print("minimum sales in 1 month=",min(sales_data))

import csv
field_names = ["year", "month", "sales", "expenditure"]
data = [
    {"year":2018,"month":"jan", "sales":6226,"expenditure":3808},
    {"year":2018, "month":"feb", "sales":1521, "expenditure":3373},
    {"year":2018, "month":"mar", "sales":1842, "expenditure":3965},
    {"year":2018, "month":"apr", "sales":2051, "expenditure":1098},
    {"year":2018, "month":"may", "sales":1728, "expenditure":3046},
    {"year":2018, "month":"jun", "sales":2138, "expenditure":2258},
    {"year":2018, "month":"jul", "sales":7479, "expenditure":2084},
    {"year":2018, "month":"aug", "sales":4434, "expenditure":2799},
    {"year":2018, "month":"sep", "sales":3615, "expenditure":1649},
    {"year":2018, "month":"oct", "sales":5472, "expenditure":1116},
    {"year":2018, "month":"nov", "sales":7224, "expenditure":1431},
    {"year":2018, "month":"dec", "sales":1812, "expenditure":3532}
]

with open("sales.csv", "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)