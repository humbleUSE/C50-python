# Validate a vanity plate number
def main():
  import sys
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")

  sys.exit()


# Helper function to check if a string is a valid plate number
def is_valid(plate):
  import re
  match = re.fullmatch(r"(?=[a-z0-9]){2,6}^[a-z]{2}([a-z]{0,3}((?(?<![a-z])0{0,3}|[1-9]{1,4})(?<=[1-9])(\d){0,3}))?$",
                       plate, re.I)
  return bool(match)


if __name__ == "__main__":
  main()
