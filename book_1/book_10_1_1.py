file_name = "learning_python.txt"

with open(file_name, 'r') as f:
    for line in f:
        print(line.replace('Python', 'Ruby').strip())
