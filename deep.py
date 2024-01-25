def main():
  answer = input(
      "What is the answer to the Great Question of Life, the Universe, and Everything? "
  )

  # Strip and lowercase answer
  answer = answer.strip().lower()
  
  # Check if answer is correct
  match answer:
    case "42" | "forty two" | "forty-two":
      print("Yes")
    case _:
      print("No")

main()
