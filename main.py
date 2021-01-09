import matplotlib.pyplot as plt
import math, sys

def prime_finder(number):
    count_factors = 0
    divisor = number
    while divisor>=1: 
      upper_factor = number/divisor
      if upper_factor.is_integer() is True:
        upper_factor = int(upper_factor)
        count_factors += 1
      divisor -= 2
    return number, count_factors

def prime_data_finder(number):
    count_factors = 0
    divisor = math.floor(number**0.5)
    while divisor >= 1: 
      upper_factor = number/divisor
      if upper_factor.is_integer() is True:
        upper_factor = int(upper_factor)
        count_factors += 1
      divisor -= 1
    if count_factors == 2 or number == 2 and number >1:
      number = int(number)
    else:
      number = ""
    return number

def correct_inputs(upper = "", placement = "step"):
  play = False
  main_count = 0
  while play != True:
    if placement == "lower" or placement == "upper":
      if placement == "lower":
        bound = input("What is the lower limit of your range:\t")
      elif placement == "upper":
        bound = input("and the upper limit:\t")
      try:
        bound = int(bound)
        play = True
      except ValueError:
        play = False
    else:
      if main_count == 0:
        bound = input("What is your desired step:\t")
      if main_count >0:
        bound = input("I need a correct input:\t")
      try:
        bound = int(bound)
        play = True
        check = int(upper)/bound
        if check.is_integer() is False:
          play = False
        else:
          play = True
      except ValueError:
        play = False
    main_count += 1
  return bound

def plotting(x, y):
  graph = plt.plot(x,y, "ro")
  plt.xlabel("Number Range")
  plt.ylabel("Number of Primes")
  plt.title("Change in ratio of Primes")
  plt.savefig('plot.png', dpi = 72)
  plt.show()
  print("Your data graph was saved to \'plot.png\'")



def prime_presenter():
  lower = int(correct_inputs("","lower"))
  upper = int(correct_inputs("","upper"))
  prime_number_list = []
  for x in range(lower, upper + 1):
    if x%2 == 1 or x==2:
      x, count = prime_finder(x)
      if count == 2 or x == 2:
        prime_number_list.append(f"{x}")
  print(f"There are {len(prime_number_list)} primes within your range")
  print(prime_number_list)

def prime_data():
  lower = 0
  upper = int(correct_inputs("","upper"))
  step = int(correct_inputs(upper,))
  prime_data_list = {}
  count_list = []
  prime_count_list = []
  count = lower + step
  general_count = 0
  print("Processing...")
  while count <= upper:
    prime_list = []
    for x in range(count - step, count + 1):
      if prime_data_finder(x) != "":
        prime_list.append(prime_data_finder(x))
    general_count += len(prime_list)
    prime_data_list.update({count:general_count})
    count_list.append(count)
    prime_count_list.append(general_count)
    count += step
  print("Getting your image ready...")
  plotting(count_list, prime_count_list)
  choice = input("Would like to know more information about your graph? (\'yes\'' or \'no\'')")
  while choice.lower() != "yes" or choice.lower() != "no":
    choice = input("Tis yes or no mate:\t")
  if choice == "yes":
    more_info = 


  
  
def main():
  main_choice = input("I deal with primes, here are my options:\n1: Find the number of primes in a range\n2: Run a graph of prime ratios\nYour choice:\t")
  play = False
  while play != True:
    try:
      main_choice = int(main_choice)
      if main_choice in range(1,3):
        play = True
      else:
        main_choice = input("I need a correct choice option:\t")
    except ValueError:
      main_choice = input("I need a correct choice option:\t")
  
  if main_choice == 1:
    prime_presenter()
  
  if main_choice == 2:
    prime_data()

main()


