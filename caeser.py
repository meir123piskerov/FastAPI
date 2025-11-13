def caesar(text):
  new_text = ""
  for ch in range(len(text)):
    if ch == 0:
      new_text += text[ch]
    elif ch % 2 == 0 and ch != 0:
      new_text += text[ch]
  for ch in range(len(text)):
    if ch % 2 != 0:
      new_text += text[ch]
  return new_text

print(caesar("meir"))
