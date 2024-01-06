# Calulate tip amount
def main():
  import sys
  dollars = dollars_to_float(input("How much was the meal? "))
  percent = percent_to_float(input("What percentage would you like to tip? "))
  tip = dollars * percent
  print(f"Leave ${tip:.2f}")
  sys.exit()


# Convert a sring to a float
def dollars_to_float(price):
  price = float(price.removeprefix("$"))
  return price


# Convert percent to float
def percent_to_float(tip):
  tip = float(tip.removesuffix("%")) / 100

  return tip


main()
