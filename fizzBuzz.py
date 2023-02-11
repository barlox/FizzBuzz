"""
  Write a program that prints the numbers from 1 to 100.
  But for multiplies of three print 'Fizz' instead of number and for the multiplies of five print 'Buzz'. 
  For numbers which are multiplies of both three and five print 'FizzBuzz'.
  
"""

def fizz_buzz(max_value = 100):
  answers = ['Fizz', 'Buzz']
  max_value += 1
  numbers = range(1, max_value)
  
  for num in numbers:
    if num % 3 == 0 and not num % 5 == 0:
      print(answers[0])
      continue
    elif num % 5 == 0 and not num % 3 == 0:
      print(answers[1])
      continue
    elif num % 5 == 0 and num % 3 == 0:
      print(''.join(answers))
      continue
    else:
      print(num)