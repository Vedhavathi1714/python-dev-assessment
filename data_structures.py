def filter_and_sort_evens(numbers): 
    even_numbers = []
  for number in numbers:
      if number % 2==0:
           even_numbers.append(number)
      
  even_numbers.sort()
  return even_numbers
      
def count_character_frequency(text):
    frequency = {}
        
    for character in text:
        if character in frequency:
            frequency[character ]+=1
        else:
            frequency[character]=1
    return frequency

numbers =[3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
print(filter_and_sort_evens(numbers))

text = "This my task for Basic Data Structures & Algorithms"
print(count_character_frequency(text))
