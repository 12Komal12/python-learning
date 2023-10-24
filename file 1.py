Name = input("Enter your name:\n").lower()
txt = Name[::-1]
print(txt)

if Name == txt:
         print("palindrome possible")
elif Name != txt:
         print("palindrome not possible")