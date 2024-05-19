import csv
from jinja2 import Environment, FileSystemLoader

# Read the CSV file
with open('grammar.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=';')
    grammar_points = list(reader)

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the grammar points
output = template.render(grammar_points=grammar_points)

# Write the output to the HTML file
with open('emptyGeneratedContent.html', 'w', encoding='utf-8') as file:
    file.write(output)
