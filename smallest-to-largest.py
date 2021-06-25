#------------find largest and smallest num--------
largest = None
smallest = None
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try:
        num = int(inp)
    except:
        print("Invalid input")
        continue
    count = count + 1

    if smallest == None:
        smallest = num
    elif num < smallest:
        smallest = num

    if largest == None:
        largest = num
    elif num > largest:
        largest = num

    # print(num)

print("Maximum is", largest)
print("Minimum is", smallest)


