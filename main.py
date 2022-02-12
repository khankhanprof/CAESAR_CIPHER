from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(text,shift_no,direction):
  new_text=[]
  if direction=="encode":
    for char in text:
      new=int(alphabet.index(char)+shift_no)
      try:
        new_text.append(alphabet[new])
      except:
        a=(new%25)-1
        new_text.append(alphabet[a])
    print("the decoded text is","".join(new_text))
  elif direction=="decode":
    for char in text:
      new=int(alphabet.index(char)-shift_no)
      try:
        new_text.append(alphabet[new])
      except:
        a=new+24
        new_text.append(alphabet[a])
    print("the encoded text is","".join(new_text))
  
   
ceaser(text,shift,direction)

