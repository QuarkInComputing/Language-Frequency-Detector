import json

### Vars that can be adjusted
tolerance = 0.1 
filepath = "texts/beemovie.txt"
###

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettercount = []
frequency = []

totalcount = 0

languages = ["English", "French", "German", "Spanish", "Portuguese", "Italian", "Turkish", "Swedish", "Polish", "Dutch", "Danish", "Icelandic", "Finnish", "Czech", "Hungarian", "Welsh"]
with open("frequency.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def textFrequency(text):
    global totalcount, lettercount, frequency
    for letter in letters:
        count = text.count(letter)
        totalcount += count
        lettercount.append(count)
        print(letter + ": " + str(count))

    for count in lettercount:
        freq = (count / totalcount) * 100
        frequency.append(freq)

with open(filepath, 'r', encoding='utf-8') as file:
    text = file.read().lower()

textFrequency(text)

# Collect language frequencies
freq_arrays = {lang: [] for lang in languages}
for entry in data:
    letter = entry["Letter"].lower()
    if letter in letters:
        for lang in languages:
            value = entry.get(lang, "0").replace("%", "").replace("~", "").strip()
            print(value)
            freq_arrays[lang].append(float(value))

similarity = {}

for lang in languages:
    matches = sum(1 for i in range(len(letters))
                  if abs(frequency[i] - freq_arrays[lang][i]) <= tolerance)
    sim = matches / len(letters) * 100 
    similarity[lang] = sim

closest = sorted(similarity.items(), key=lambda x: x[1], reverse=True)

print("Language similarity:")
for lang, score in closest:
    print(f"{lang}: {score:.2f}%")