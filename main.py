name = input("Enter your first name:")
print("Hello"+" "+ name +"!")

mood = input("How do you feel today?")

if mood =="happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Make a list of 3 things you are grateful for")
elif mood == "excited":
    print("Great!!! Take the opportunity to do something you love ")
elif mood == "relaxed":
    print("Great!!! Enjoy")
else:
    print("I don't recognize this mood")