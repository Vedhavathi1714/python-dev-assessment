def calculate_average(numbers):
  try:
    if len(numbers) == 0:
      raise ValueError("The list is empty")
    return sum(numbers) / len(numbers)
  except ValueError as error:
    print("Erroer:", error)
    return None

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print("Average of data1:", calculate_average(data1))
print("Average of data2:", calculate_average(data2))
print("Average of data3:", calculate_average(data3))
