n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
without_edges = numbers[1:-1]
every_second = numbers[::2]
print("Исходный список:", numbers)
print("Без крайних:", without_edges)
print("Каждый второй:", every_second)

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers[0], numbers[-1] = numbers[-1], numbers[0]
after_swap = numbers.copy()
numbers.append(numbers.pop(0))
after_shift = numbers.copy()
print("После перестановки:", after_swap)
print("После сдвига влево:", after_shift)

stack = []
while True:
    print("1 — положить, 2 — забрать, 3 — посмотреть верхний, 4 — показать, 5 — выйти")
    choice = input()
    if choice == "1":
        stack.append(input())
    elif choice == "2":
        if len(stack) == 0:
            print("Стек пуст!")
        else:
            item = stack.pop()
            print("Забрали:", item)
    elif choice == "3":
        if len(stack) == 0:
            print("Стек пуст!")
        else:
            top_item = stack[-1]
            print("Сверху:", top_item)
    elif choice == "4":
        print("Стек:", stack)
    elif choice == "5":
        break
    else:
        print("Нет такого пункта")

n = int(input())
list1 = []
list2 = []
print("Первый список:")
for i in range(n):
    list1.append(int(input()))
print("Второй список:")
for i in range(n):
    list2.append(int(input()))
common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
print("Список 1:", list1)
print("Список 2:", list2)
print("Общие:", common)

words = input().split()
longest = words[0]
shortest = words[0]
total = 0
for w in words:
    total += len(w)
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w

avg = round(total / len(words))
longest_length = len(longest)
shortest_length = len(shortest)
for w in words:
    if len(w) == avg:
        print(w)
print(f'длинное: "{longest}" ({longest_length}), короткое: "{shortest}" ({shortest_length}), средняя длина: {avg}\nСлова средней длины: {w}')

items = []
while True:
    item = input()
    if item == "готово":
        break
    items.append(item)

while len(items) > 0:
    for i in range(len(items)):
        number = i + 1
        product = items[i]
        print(number, product)
    num = int(input())
    if 1 <= num <= len(items):
        removed_item = items.pop(num - 1)
        print("Вычеркнуто:", removed_item)
    else:
        print("Нет такого номера")
print("Список пуст!")


n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

first = max(numbers[0], numbers[1])
second = min(numbers[0], numbers[1])
for x in numbers[2:]:
    if x > first:
        second = first
        first = x
    elif x > second:
        second = x
print('наибольшее: {first}\nвторое по величине: {second}')


chars = list(input())
for i in range(5):
    text = "".join(chars)
    print(text)
    chars.append(chars.pop(0))


n = int(input())
student_grades = {}
for _ in range(n):
    name = input()
    grades = [int(g) for g in input().split()]
    student_grades[name] = grades

averages = []
for i in range(n):
    avg = sum(grades[i]) / len(grades[i])
    averages.append(avg)
    name = names[i]
    first_grade = grades[i][0]
    second_grade = grades[i][1]
    third_grade = grades[i][2]
    result = f"{name}: {first_grade} {second_grade} {third_grade} -> средняя: {avg:.2f}"
    print(result)

best = averages.index(max(averages))
best_name = names[best]
print("Лучший:", best_name)

rolls = [3, 6, 1, 4, 6, 2, 5, 6, 3, 4]
for i in range(len(rolls)):
    number = i + 1
    roll = rolls[i]
    print("Бросок", number, ":", roll)

sixes = rolls.count(6)
average_roll = sum(rolls) / len(rolls)
unique_rolls = sorted(set(rolls))
print("Шестёрок выпало:", sixes)
print("Средний результат:", average_roll)
print("Уникальные значения:", unique_rolls)


n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(len(numbers) - 2):
    part = numbers[i:i + 3]
    part_sum = sum(part)
    part_average = part_sum / 3
    result = f"({part[0]}+{part[1]}+{part[2]})/3 = {part_average:.2f}"
    print(result)


n = int(input())
matrix = []
k = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(k)
        k += 1
    matrix.append(row)

print("Исходная:")
for row in matrix:
    print(*row)

transposed = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    transposed.append(row)

print("Транспонированная:")
for row in transposed:
    print(*row)


n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    step = i + 1
    print("Шаг", step, ":", numbers)


n = int(input())
fib = []
for i in range(n):
    if i < 2:
        fib.append(1)
    else:
        fib.append(fib[-1] + fib[-2])
print(fib)

x = int(input())
if x in fib:
    print("Число", x, "— есть в последовательности!")
else:
    print("Число", x, "— не входит.")


grades = []
while True:
    g = int(input())
    if g == 0:
        break
    grades.append(g)

sorted_grades = sorted(grades)
average_grade = round(sum(grades) / len(grades), 2)
mode = 1
for g in range(2, 6):
    if grades.count(g) > grades.count(mode):
        mode = g
mode_count = grades.count(mode)
excellent_percent = round(grades.count(5) / len(grades) * 100)

print("Исходный список:", grades)
print("Отсортированный:", sorted_grades)
for g in range(1, 6):
    count = grades.count(g)
    print("Оценка", g, ":", count, "раз")
print("Средняя оценка:", average_grade)
print("Мода:", mode, "(встречается", mode_count, "раз)")
print("Отличников:", excellent_percent, "%")