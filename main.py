def replace_elements(arr, Z):
  count = 0
  for i in range(len(arr)):
      if arr[i] > Z:
          arr[i] = Z
          count += 1
  return count

n = int(input("Введіть розмір послідовності: "))
arr = []

print("Введіть елементи послідовності:")
for l in range(n):
  arr.append(float(input()))

Z = float(input("Введіть число Z: "))

replacements = replace_elements(arr, Z)

print("Масив після заміни:")
print(' '.join(map(str, arr)))
print("Кількість замін:", replacements)

print("Результат:")
for row in matrix: