import random

t = 100000
same_birthday = 0

for _ in range(t):
    birthdays = []
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthday += 1
            break
        birthdays.append(birthday)

print(f'{same_birthday / t * 100}%')