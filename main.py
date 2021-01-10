from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math, sys
import time, sys

extra_resources = "https://en.wikipedia.org/wiki/Riemann_hypothesis ,\nhttps://math.uni.lu/eml/projects/reports/prime-distribution.pdf,\nand https://www.youtube.com/watch?v=zlm1aajH6gY&ab_channel=QuantaMagazine"

prime_list = []

def prime_presenter():
  lower = int(correct_inputs("","lower"))
  upper = int(correct_inputs("","upper"))
  global prime_number_list_2
  prime_number_list = []
  prime_number_list_2 = ""
  for x in range(lower, upper + 1):
      x, count = prime_finder(x)
      if count == 1:
        prime_number_list.append(f"{x}")
  try:
    prime_number_list.remove("1")
  except:
    y=1
  for x in prime_number_list:
    prime_number_list_2 += f"{x} "
  print(f"There are {len(prime_number_list)} primes within your range")

def prime_finder(number):
    count_factors = 0
    divisor = math.floor(number**0.5)
    while divisor>=1: 
      upper_factor = number/divisor
      if upper_factor.is_integer() is True:
        upper_factor = int(upper_factor)
        count_factors += 1
        prime_list.append(number)
      divisor -= 1
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
    if (count_factors == 1) and number >1:
      number = int(number)
      prime_list.append(number)
    else:
      number = ""
    return number

def prime_data(main_choice):
  lower = 0
  upper = int(correct_inputs("","upper"))
  step = int(correct_inputs(upper,))
  prime_data_list = {}
  prime_count_list = []
  count = lower + step
  general_count = 0
  count_list = []
  approaching_list = []
  print("Processing...")
  if main_choice == "2":
    t_1 = time.perf_counter()
    while count <= upper:
      if math.log10(count) != 0:
        approaching_number = round(count/math.log(count),20)
        log_val_1 = approaching_number  - (0.00002119140548874392 * count) + (0.000000001048136027939523 * count**2) + 0.10500080147996602
        log_val_2 = log_val_1 + (0.000023493437644103025 *count) - (0.0000000010935633602541922 * count**2) - 0.140357625257643
        approaching_number = log_val_2 + (0.000005569506823401875*count) - (0.00000000009512863876912848 * count**2) - 0.07807374409750371 
      elif math.log10(count) == 0:
        approaching_number = 0
        print(count)
      approaching_list.append(approaching_number)
      count_list_1 = []
      for x in range(count - step, count + 1):
        if prime_data_finder(x) != "":
          count_list_1.append(prime_data_finder(x))
      general_count += len(count_list_1)
      prime_data_list.update({count:general_count})
      count_list.append(count)
      prime_count_list.append(general_count)
      count += step
  if main_choice == "3":
    t_1 = time.perf_counter()
    general_count = 0
    while count <= upper:
      if math.log(count) != 0:
        approaching_number = round(1/math.log(count, math.e),7)
      elif math.log(count) == 0:
        approaching_number = 0
      approaching_list.append(approaching_number)
      count_list_1 = []
      for x in range(count - step, count + 1):
        if prime_data_finder(x) != "":
          count_list_1.append(prime_data_finder(x))
      general_count += len(count_list_1)
      ratio = round(general_count/count,8)
      prime_data_list.update({count:general_count})
      count_list.append(count)
      prime_count_list.append(ratio)
      count += step
  prime_list_2 = list(dict.fromkeys(prime_list))
  print(100*(prime_count_list[-1] - approaching_list[-1])/count_list[-1])
  t_2 = time.perf_counter()
  print("Getting your image ready...")
  x = plotting(count_list, prime_count_list, approaching_list)
  t_3 = time.perf_counter()
  return t_1, t_2, t_3, prime_list

def digit_data():
  print("Do know this is very intensive, counting all the digits, but enjoy.")
  list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9 = [],[],[],[],[],[],[],[],[],[]
  g_count_0 = 0
  g_count_1 = 0
  g_count_2 = 0
  g_count_3 = 0
  g_count_4 = 0
  g_count_5 = 0
  g_count_6 = 0
  g_count_7 = 0
  g_count_8 = 0
  g_count_9 = 0
  lower = 0
  upper = int(correct_inputs("","upper"))
  step = int(correct_inputs(upper,))
  count = lower + step
  count_list = []
  print("Processing...")
  t_1 = time.perf_counter()
  while count <= upper:
      prime_str = ""
      for x in range(count - step, count + 1):
        if prime_data_finder(x) != "":
          prime_list.append(x)
      prime_digitdata_list = list(dict.fromkeys(prime_list))
      global prime_save_list
      prime_save_list = prime_digitdata_list
      for x in prime_digitdata_list:
        prime_str += f"{x}"
      g_count_0 = int(prime_str.count("0"))
      g_count_1 = int(prime_str.count("1")) 
      g_count_2 = int(prime_str.count("2")) 
      g_count_3 = int(prime_str.count("3")) 
      g_count_4 = int(prime_str.count("4")) 
      g_count_5 = int(prime_str.count("5")) 
      g_count_6 = int(prime_str.count("6")) 
      g_count_7 = int(prime_str.count("7")) 
      g_count_8 = int(prime_str.count("8")) 
      g_count_9 = int(prime_str.count("9"))
      list_0.append(g_count_0), list_1.append(g_count_1),list_2.append(g_count_2), list_3.append(g_count_3), list_4.append(g_count_4), list_5.append(g_count_5), list_6.append(g_count_6), list_7.append(g_count_7), list_8.append(g_count_8), list_9.append(g_count_9), count_list.append(count)
      count += step
  global highest_number_dict
  highest_number_dict = {0:g_count_0, 1:g_count_1, 2:g_count_2, 3:g_count_3, 4:g_count_4, 5:g_count_5,6:g_count_6, 7:g_count_7, 8:g_count_8, 9:g_count_9}
  max_set = max(highest_number_dict, key =highest_number_dict.get)
  t_2 = time.perf_counter()
  print("Getting your image ready...")
  digit_plotting(list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, count_list)
  t_3 = time.perf_counter()
  return t_1, t_2, t_3, max_set

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

def plotting(x, y, y_2 = ""):
  plt.plot(x,y, "ro")
  if y_2 != "":
    plt.plot(x, y_2, "bo")
  plt.xlabel("Number Range")
  plt.ylabel("Number of Primes")
  plt.title("Change in ratio of Primes")
  plt.savefig('plot.png', dpi = 300)
  print("Your data graph was saved to \'plot.png\'")

def digit_plotting(x,x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9, y):
  plt.plot(y,x, "mo")
  plt.plot(y,x_1, "ro")
  plt.plot(y,x_2, "yo")
  plt.plot(y,x_3, "go")
  plt.plot(y,x_4, "co")
  plt.plot(y,x_5, "bo")
  plt.plot(y,x_6, "ko")
  plt.plot(y,x_7, "m-")
  plt.plot(y,x_8, "r-")
  plt.plot(y,x_9, "y-")
  height_1 = str(x_1[-1])
  height_1 = height_1.replace("(","")
  height_1 = height_1.replace(")","")
  height_1 = height_1.replace(",","")
  height_1 = int(height_1)
  height = math.floor(height_1*0.55)
  plt.xlabel("Number Range")
  plt.ylabel("Number of relative Digits among Primes")
  plt.title("Change in ratio of Primes")
  plt.text(0, height,"Magenta o: 0\nRed o: 1\nYellow o: 2\nGreen o: 3\nCyan o: 4\nBlue o: 5\nBlack o: 6\nMagenta -: 7\nRed -: 8\nYellow -: 9")
  plt.savefig('Dowloads>plot.png', dpi = 72)
  print("Your data graph was saved to \'plot.png\'")

def bonus(t_1, t_2, t_3, main_choice, prime_list = "", max_set = ""):
  prime_list = list(dict.fromkeys(prime_list))
  count = 0
  play = False
  while play != True:
    if count == 0:
      if main_choice >1:
        choice = input("Would like to know more information about your graph? (\'yes\' or \'no\'):\t")
      else:
        choice = input("Would you like to see those primes:\t")
    else:
      choice = input("Tis yes or no mate:\t")
    choice = choice.lower()
    if choice == "yes":
      play = True
    if choice == "no":
      play = True
  print("\n")
  choice = choice.lower()
  if choice == "yes":
    if main_choice == 1:
      print(f"Here they are:\n{prime_number_list_2}")
    if main_choice == 2 or main_choice == 3:
      print(f"The largest prime was:  {prime_list[-1]}\nThere were a total of {len(prime_list)} primes\nIt took {round(t_2 - t_1, 3)} seconds to process the numbers \nand {round(t_3 - t_2, 3)} to process the graph ")
    if main_choice == 4:
      print(f"The most-occuring number among primes was:  {max_set}\nwhich occured {highest_number_dict[max_set]} times. There were a total of {len(prime_save_list)} primes\nIt took {round(t_2 - t_1, 3)} seconds to process the numbers \nand {round(t_3 - t_2, 3)} to process the graph ")
    useless = input()
    if main_choice == 2:
      print(f"Well, this graph approaches the line x/log(x)\nThis was proved near the end of the 19th century by two\n mathemeticians Jacques Hadamard and Charles J. de la Vallée-Poussin")
      useless = input()
      print(f"and original interest was founded by mathmeticians Carl F. Gauss and AdrienMarie Legendre\nThis is the foundation for theoretical mathematics like Reimanns hypothesis\nwhich sets a foundation for many other feilds\nsuch as Quantum Mechanics and Number Theory")
      useless = input()
      print(f"For more info:\n{extra_resources}")
    elif main_choice >2:
      print("The study of primes is important and higly prevalent\nin the math feild, being used in many ways, but most importantly in cryptology.\nIn crytology they take two very large prime numbers and multiply them\nas a verification key between 2 devices.\nIt's very hard for computers to divide out primes, especially large ones,\nso this works well to ensure a consistent and secure\nverification process to connect to devices")
      useless = input()
      print("Currently primes have no consistent behavior but by\nReimanns Hypothesis, if you can prove all non-trivial zeroes\nof the ζ() function have a real-component of 1/2,\nthen primes can be predicted, making cracking down cryptology really easy, \nimagine the power you could weild. \nAlso, you get 1 million dollars for proving Reimanns hypothesis.")
      useless = input()
      print("Primes have interested mathematicians since the beggining\n of math itself, what will you contribute to the thought behind\n one of the most mysterious parts of the universe?\n")
      print(f"For more info:\n{extra_resources}")

def percent_error():
  upper = int(correct_inputs("","upper")) + 100
  total_error = 0
  quantity = 0
  step = 100
  count = 1100
  general_count = 0
  count_list_2 = []
  log_val_list = []
  for x in range(1000, upper , 100):
    x = int(x)
    count_1 = x
    while count_1 < count:
      count_list_1 = []
      count_list_2.append(x)
      for x in range(count , count + 101, 1):
        if prime_data_finder(x) != "":
          count_list_1.append(prime_data_finder(x))
      general_count += len(count_list_1)
      count_1 += step
    count+= step
    log_val_1 = ((general_count - (x/math.log(x)))/x)
    log_val_2 = log_val_1  - (0.00002119140548874392 * x) + (0.000000001048136027939523 * x**2) + 0.10500080147996602
    log_val_3 = log_val_2 - ((-5.))
    log_val = abs(log_val_2 + (0.000023493437644103025 * x) - (0.0000000010935633602541922 * x**2) - 0.140357625257643)
    total_error
    log_val_list.append(log_val)
    count_list = list(dict.fromkeys(count_list_1))
  minimum = min(log_val_list)
  print(minimum)
  number_val = log_val_list.index(minimum)*100 + 1000
  print(number_val)
  plotting_2(count_list_2, log_val_list)

def plotting_2(x, y):
  # define the true objective function
  def objective(x, a, b, c):
	  return a * x + b * x**2 + c
  popt, _ = curve_fit(objective, x, y)
  # summarize the parameter values
  a, b, c = popt
  print(a, b, c)
  print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
  # plot input vs output
  plt.scatter(x, y)
  # define a sequence of inputs between the smallest and largest known inputs
  x_line = arange(min(x), max(x), 1)
  # calculate the output for the range
  y_line = objective(x_line, a, b, c)
  # create a line plot for the mapping function
  plt.plot(x_line, y_line, '--', color='red')
  plt.savefig("plot.png")

def main():
  main_count = 0
  y= -1
  while y <0:
    if main_count == 0 or main_count%4 == 0:
      print("I deal with primes,", end = "")
      main_choice = input("here are my options:\n1: Find the number of primes in a range\n2: Run a graph of prime ratios\n3: 2 but a different view\n4: Change in digit counts over the range\n5: Quit\nYour choice:\t")
    else:
      main_choice = input('\nYour choice:\t')
    play = False
    while play != True:
      try:
        main_choice = int(main_choice)
        if main_choice in range(1,6):
          play = True
        else:
          main_choice = input("I need a correct choice option:\t")
      except ValueError:
        main_choice = input("I need a correct choice option:\t")
    
    if main_choice == 1:
      prime_presenter()
      bonus(0,0,0,1,prime_number_list_2 ,"")
      
    
    if main_choice == 2:
      t_1, t_2, t_3, prime_list = prime_data("2")
      bonus(t_1, t_2, t_3, 2, prime_list)
    
    if main_choice == 3:
      t_1, t_2, t_3, prime_list = prime_data("3")
      bonus(t_1, t_2, t_3, 3, prime_list)
    
    if main_choice == 4:
      t_1, t_2, t_3, max_set = digit_data()
      bonus(t_1, t_2, t_3, 4, "", max_set)
    
    if main_choice == 5:
      percent_error()
      print("\nThank you for using me :)\nIhope you enjoyed")
    
    main_count += 1


main()