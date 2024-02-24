# palindrome of a string using reverse method
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]

# word = input("Enter the palindrome word: ")

# if is_palindrome(word):
#     print(f"{word} is a palindrome!")
# else:
#     print(f"{word} is not a palindrome!")

#palindrome usind loop method
# def is_palindrome_loop(s):
#     s=s.replace(" ","").lower()
#     length=len(s)
#     for i in range(length//2):
#         if s[i]!=s[length-i-1]:
#             return False
#         return True
# word = input("Enter the palindrome word: ")   
# if is_palindrome_loop(word):
#     print(f"{word} is a palindrome!")
# else:
#     print(f"{word} is not a palindrome!")

#code to check whether the numbers are palindrome are not
# def num_palindrome(num):
#     n=str(num)
#     return n==n[::-1]
# number = input("Enter the palindrome number: ")   
# if num_palindrome(number):
#     print(f"{number} is a palindrome!")
# else:
#     print(f"{number} is not a palindrome!")

#slice method to check whether the given word is palindrome or not
text: str = input("Enter the word to check palindrome or not?")
myslice = slice(None, None,-1)
if (text[myslice]==text):
    print(f"{text} is an palindrome!")
else:
    print(f"{text} is not a palindrome!")

        



