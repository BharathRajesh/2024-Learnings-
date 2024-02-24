import string
alphabets=list(string.ascii_lowercase)
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabets[new_position]
        else:
            cipher_text+=char
    print(f"the encrypted data is {cipher_text}")
def decryption(cipher_text,shiftkey):
    plain_text=""
    for char in cipher_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabets[new_position]
        else:
            plain_text+=char
    print(f"the encrypted data is {plain_text}")

wanna_cont=False
while not wanna_cont:
    action=input("Enter if you wanna encrypt or decrypt:")
    text=input("enter the text that you wanna perform action:")
    shift_key=int(input("enter how many shifts:"))
    if action=="encrypt":
        encryption(text,shift_key)
    elif action=="decrypt":
        decryption(text,shift_key)
    want_cont=input("enter yes if you wanna continue:").lower()
    if want_cont=="yes":
        wanna_cont=False
    else:
        wanna_cont=True
        print("ok bye")
