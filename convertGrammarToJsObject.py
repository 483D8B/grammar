import csv
import json

# Read the CSV file
with open('grammar.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=';')
    headers = next(reader)  # This will store the header row
    rows = [row for row in reader]

# Convert to a list of dictionaries
data = [dict(zip(headers, row)) for row in rows]

# Convert the list of dictionaries to a JavaScript object
js_object = 'var grammar = ' + json.dumps(data, ensure_ascii=False) + ';'

# Write the JavaScript object to a file
with open('grammar.js', 'w', encoding='utf-8') as f:
    f.write(js_object)
