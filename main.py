def find_max_element(matrix):
  max_element = matrix[0][0]
  max_row = 0
  max_col = 0
  rows = len(matrix)
  cols = len(matrix[0])

  for i in range(rows):
      for j in range(cols):
          if matrix[i][j] > max_element:
              max_element = matrix[i][j]
              max_row = i
              max_col = j

  return max_row, max_col

def swap_rows(matrix, row1, row2):
  matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def swap_columns(matrix, col1, col2):
  for i in range(len(matrix)):
      matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

def rearrange_matrix(matrix):
  max_row, max_col = find_max_element(matrix)
  swap_rows(matrix, 0, max_row)
  swap_columns(matrix, 0, max_col)

n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

print("Введіть елементи матриці:")
matrix = []
for i in range(n):
      row = list(map(int, input().split()))

      if len(row) != m:
          print(f"Помилка: у рядку {i+1} введено неправильну кількість елементів.")
          exit()
      matrix.append(row)

rearrange_matrix(matrix)

print("Результат:")
for row in matrix:
  print(" ".join(map(str, row)))
