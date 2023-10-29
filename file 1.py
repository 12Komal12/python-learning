# 1. Write a Python program to sum all the items in a list

List = [1,4,9,16,25,36,49,64]
txt = sum(List)
print(txt)

# 2. Write a Python program to multiply all the items in a list

List = [1, 4, 9, 16, 25, 36, 49, 64]
def multiply(list):
      chr = 1
      for i in list:
          chr *= i
      return chr
print(List)

# 3. Write a Python program to get the largest number from a list

List = [1, 4, 9, 16, 25, 36, 49, 64]
print(max(List))

## 4. Write a Python program to get the smallest number from a list.

List = [1, 4, 9, 16, 25, 36, 49, 64]
print(min(List))

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

List = ['abca','6661' 'xyz', 'aba', '4444']
def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr
print(match_words(List))
