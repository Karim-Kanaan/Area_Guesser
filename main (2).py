length = int(input("Enter rectangle length: "))
width = int(input("Enter rectangle width: "))

area = length * width

guess = int(input("Size of the area: "))

if guess == area:
    print("You guessed it right")
else:
    print("you are wrong, the area was", area ) 