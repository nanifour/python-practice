#------------Convert score to letter grades--------
score = input("Enter Score: ")
try:
    #try what you want to work
    sc = float(score)
except:
    print("Error, please enter a number")

if (sc < 0.0) or (sc > 1.0):
    print("Error, score is out of range")
    exit()
elif sc >= 0.9:
    letter = 'A'
elif sc >= 0.8:
    letter = 'B'
    print(letter)
elif sc >= 0.7:
    letter = 'C'
elif sc >= 0.6:
    letter = 'D'
elif sc < 0.6:
    letter = 'F'

print(letter)
