from sys import exit
print("Sorry, but we can't check capitals (yet).")
possible = [0,1,2,3,4,5,6,7,8,9,"a", "b", "c","d", "e", "f","g", "h", "i","j", "k", "l","m", "n", "o", "p","q", "r", "s","t", "u", "v","w", "x", "y","z"]
digits = int(input("Number of digits in your password?\n"))
numbers = input("Does it have numbers?\n")
letters = input("Does it have letters?\n")
if "yes" in numbers:
    possible = [0,1,2,3,4,5,6,7,8,9]
if "yes" in letters:
    possible = ["a", "b", "c","d", "e", "f","g", "h", "i","j", "k", "l","m", "n", "o", "p","q", "r", "s","t", "u", "v","w", "x", "y","z"]
if "yes" in letters and "yes" in numbers:
    possible = [0,1,2,3,4,5,6,7,8,9,"a", "b", "c","d", "e", "f","g", "h", "i","j", "k", "l","m", "n", "o", "p","q", "r", "s","t", "u", "v","w", "x", "y","z"]
if "no" in letters and "no" in numbers or digits == 0:
    print("Sorry, no outputs")
    exit()
print("These are all the possible passwords:")
if digits == 1:
    for i in range(len(possible)):
        print(possible[i])
if digits == 2:
    for i in range(len(possible)):
        for j in range(len(possible)):
            print(f"{possible[i]}{possible[j]}")
if digits == 3:
    for i in range(len(possible)):
        for j in range(len(possible)):
            for a in range(len(possible)):
                print(f"{possible[i]}{possible[j]}{possible[a]}")
