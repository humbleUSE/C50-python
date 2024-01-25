# Output reward
def main():
  import sys
  reward = get_reward()
  print(reward)
  sys.exit()


# Get reward
def get_reward():

  # Prompt for greeting
  greeting = input("greeting: ").strip().lower()

  # Check greeting
  if greeting.startswith("hello"):
    return "$0"
  elif greeting.startswith("h"):
    return "$20"
  return "$100"


main()
