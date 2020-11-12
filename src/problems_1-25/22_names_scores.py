from algorithms import delete_quotes, get_alphabetical_value


names = []

with open('../../res/p022_names.txt', "r") as f:
    line = f.readline()

    while line:
        names = names + line.split(',')
        line = f.readline()

names = delete_quotes(names)
names.sort()

names_score = 0

for i in range(len(names)):
    names_score += (get_alphabetical_value(names[i]) * (i + 1))

print(names_score)
