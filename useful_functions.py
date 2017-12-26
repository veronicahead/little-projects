# A small collection of useful functions in python

# Function tests if a number is even and returns True if so
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False

# Function determines if a number is an integer, also considers a number with a decimal part of 0 to be an integer ex 7.0 is 7
def is_int(x):
  if x - int(x) != 0:
    return False
  else: 
    return True
    
# Function takes series of digits and sums them, for example digit_sum(1234) returns 1 + 2 + 3 + 4 which is 10

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total
    
# Function returns the factorial of a given number x

def factorial(x):
  count = x
  total = 1
  while count > 0:
    total = total * count
    count -= 1
  return total
  
  # Function that returns True if a number, x, is prime
  
  def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
        
# Function takes string and returns it in reverse order
def reverse(text):
  total = ""
  for char in text:
    total = char + total
  return total
  
# Function removes all vowels from a string, y is not considered a vowel
def anti_vowel(text):
  for char in text:
    if char =="a" or char == "A" \
    or char == "e" or char == "E" \
    or char == "i" or char == "I" \
    or char == "o" or char == "O" \
    or char == "u" or char == "U":
  		text = text.replace(char,"")     
  return text
  
  # Function takes two inputs, a sequence and an item and will count the number of times the item appears in the given sequence
  def count(sequence,item):
  count = 0
  for i in sequence:
    if i == item:
      count += 1
    else:
      count = count
  return count
  
  # Function removes odd numbers from a set of numbers and returns only even numbers
  def purify(numbers):
  new_num=[]
  for item in numbers:
    if item % 2 == 0:
      new_num.append(item)
    else:
      new_num = new_num
  return new_num
  
  # Function takes product of list of integers
  def product(integers):
  total = 1
  for num in integers:
    total = total*num
  return total
  
  # Function finds median of list
  def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
