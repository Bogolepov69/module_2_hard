n = int(input("Введите целое число от 3 до 20: "))
pairs = []

for a in range(1, n):
    for b in range(a + 1, n):
        if (n % (a + b) == 0) and (a != b):
            pairs.append((a, b))

result = ""
for pair in pairs:
    result += str(pair[0]) + str(pair[1])

print(f"Для числа {n}: {result}")