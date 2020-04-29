subjects = {}

with open('6.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        subject, *marks = line.split()
        marks = map(lambda m: int(''.join(list(filter(lambda x: x.isdigit(), m)))), filter(lambda m: m != '—', marks))
        subjects[subject[:-1]] = sum(marks)

print(subjects)
