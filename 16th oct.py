#Task 1

score= int(input("Enter your score:-"))
#print(score)

if (90 <= score) and (score >= 100):
      print("A")
elif (89 <= score) and (score >= 80):
      print("B")
elif (79 <= score) and (score >= 70):
      print("C")
elif (69 <= score) and (score >= 60):
      print("D")
elif (59 <= score) and (score >= 0):
      print("E")
else:
      print("Fail")
