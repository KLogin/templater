from data import data
from template import template

for dataRow in data:
    print(template.format(d = dataRow))
    print('')