import requests
import json
from sys import exit, argv

def price_btc_USD(btc=1):
  try:  # check number of cmd line arguments
    cmdl_arg = len(argv[1:])
  except IndexError:
    exit("Missing command line argument")
  else:
    if cmdl_arg == 0:
      exit("Missing command line argument")
    elif cmdl_arg == 1:  # if one arg is given
      try:  # convert arg to float
        btc = float(argv[1])
      except ValueError:  # if arg is not a number
        exit("Command line argument is not a number")
      else:
        if btc < 0:  # check if btc is positive
          exit("Command line argument is not a positive number")
        else:  # if btc is positive
          try:
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            r = requests.get(url)
          except requests.exceptions.RequestException as e:
            exit("Error: " + str(e))
          else:
            if r.status_code == 200:
              bpi_USD = r.json()['bpi']['USD']['rate_float']
              amount = btc * bpi_USD
              # print(bpi_USD)
              print(f"${amount:,.4f}")
    else:
      exit("Command line argument is not a positive number")


if __name__ == "__main__":
  price_btc_USD()
