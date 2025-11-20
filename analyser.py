letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettercount = []
frequency = []

totalcount = 0

filepath = "texts/test.txt"

with open(filepath, 'r') as file:
    text = file.read().lower()

for letter in letters:
    count = text.count(letter)
    totalcount += count
    lettercount.append(count)
    print(letter + ": " + str(count))

for count in lettercount:
    freq = (count / totalcount) * 100
    frequency.append(freq)

print(totalcount)

print(letters)
print(lettercount)
print(frequency)