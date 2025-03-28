import random

def generate_Post_Code():
  number_list = [random.randint(0, 9) for _ in range(10)]
  number = ''.join(map(str, number_list))
  return number

def get_two_digit_numbers(postCode):
  two_digit_numbers = [int(postCode[i:i + 2]) for i in range(0, len(postCode), 2)]
  return two_digit_numbers

def generate_first_name(postCode):
  two_digit_numbers = get_two_digit_numbers(postCode)
  first_name = ''
  for number in two_digit_numbers:
      first_name += chr((number % 26) + ord('a'))
  return first_name

def generate_last_name(postCode):
  two_digit_numbers = get_two_digit_numbers(postCode)
  last_name = ''
  for number in two_digit_numbers:
      last_name += chr(ord('z') - (number % 26))
  return last_name

def generate_new_customer_test_data():
  postcode = generate_Post_Code()
  first_name = generate_first_name(postcode)
  last_name = generate_last_name(postcode)
  return postcode, first_name, last_name