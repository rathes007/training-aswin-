import csv 

f = open('annual-enterprise-csv.csv')
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row)
f.close()

print (data[1:])

def convert_row(row):
    return """<Students>
    <Year>%s</Year>
    <Industry_aggregation_NZSIOC>%s</Industry_aggregation_NZSIOC>
    <Industry_code_NZSIOC>%s</Industry_code_NZSIOC>
    <Industry_name_NZSIOC>%s</Industry_name_NZSIOC>
    <Units>%s</Units>
    <Variable_code>%s</Variable_code>
    <Variable_name>%s</Variable_name>
    <Variable_category>%s</Variable_category>
    <Value>%s</Value>
    <Industry_code_ANZSIC06>%s</Industry_code_ANZSIC06>
    <Students>"""% (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])

    with open('output.xml', 'w') as f:
        f.write('\n'.join([convert_row(row)for row in data]))