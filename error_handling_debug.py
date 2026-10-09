def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)

    except ZeroDivisionError:
        print("Error: The list is empty.")
        return None

def get_list_element(my_list, index):
    try:
        if type(my_list) != list or type(index) != int:
            raise TypeError

        return my_list[index]

    except IndexError:
        print("Error: Index is out of range.")
        return None

    except TypeError:
        print("Error: Invalid list or index type.")
        return None

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print("Average of data1:", calculate_average(data1))
print("Average of data2:", calculate_average(data2))
print("Average of data3:", calculate_average(data3))

# Test get_list_element()
print(get_list_element([10, 20, 30], 1))
print(get_list_element([10, 20, 30], 5))
print(get_list_element("hello", 0))
