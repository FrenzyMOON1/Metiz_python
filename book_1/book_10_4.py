import json

numbers = [1, 2, 3, 4, 5, 6, ]

file_name = 'numbers.json'
with open(file_name, 'r') as f:
    info = json.load(f)
    print(info)
