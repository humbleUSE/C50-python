def fuel_guage():
  import sys
  x =fuel_status("Fraction: ")
  print(x)
  sys.exit()

def fuel_status(prompt):
  import re
  while True:
        frac =input(prompt).strip()
        match=re.fullmatch(r"([a-z\d]+)/([a-z\d]+)", frac, re.I)
        if match:
          try:
            X, Y = [int(num) for num in frac.split("/")]
          except ValueError:
            pass
          else:
            if X>Y:
              pass
            else:
                  try:
                    percent = round((X/Y)*100)
                  except ZeroDivisionError:
                    pass
                  else:
                    match percent:
                        case percent if percent>99:return "F"
                        case percent if 0<=percent<=1:return "E"
                        case _:return f"{percent}%"
        else:
          return "Invalid Fuel Guage"

if __name__ == "__main__":
  fuel_guage()

