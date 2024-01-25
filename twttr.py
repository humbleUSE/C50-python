# Removes a vowel in a word
def remove_vowels():
  import sys
  word = input("Enter a word: ").strip()
  vowels = "aeiou"
  result = ""
  for char in word:
    if char.lower() not in vowels:
      result += char
  print(result)
  sys.exit()

if __name__ == "__main__":
  remove_vowels()
