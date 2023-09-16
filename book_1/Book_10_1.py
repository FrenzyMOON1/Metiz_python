with open("pi_digits.txt", 'r') as file_object:
    text = file_object.readlines()

pi_string = ''

for line in text:
    pi_string += line.strip()

print(pi_string[:10] + "..." + " длина = " + str(len(pi_string)))

birthday = input("Введите дату рождения: ")
