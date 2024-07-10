age = int(input("Provide me an age: \n"))

if age < 13 :
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age > 19 and age < 60:
    print("Adult")
else:
    print("Senior")