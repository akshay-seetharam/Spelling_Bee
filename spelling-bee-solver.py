import json
from regex import fullmatch
import os

# os.chdir(input("What is the full path to your home directory? You can get this by typing 'echo $HOME' in the terminal.\n"))
path = os.path.join(input("What is the parent directory of Spelling_Bee?\n"), "Spelling_Bee")
os.chdir(path)
# This solves the NYT spelling-bee puzzle

required = input("What is the center letter?\n").lower()
print("Enter the other letters one at a time.")
others = ""
for i in range(6):
	letter = input()
	if len(letter) == 1:
		others += letter
	else:
		raise(Exception("You need to enter one letter at a time"))

a = input("Would you like the list filtered by common words? (y/n): ")
others = others.lower()
pattern = "[" + others + required + "]+"
print("Pattern is", pattern)
with open(os.path.join(path,'english-words/words_dictionary.json')) as json_file:
	words = json.load(json_file)

print("Searching", len(words), "WORDS")

correct = {}
matched = 0
for i in words:
	if fullmatch(pattern, i.lower()) and fullmatch(".*" + required + ".*", i.lower()) is not None:
		correct[i] = len(i)
		matched += 1

sorted = {k: v for k, v in sorted(correct.items(), key=lambda item: item[1], reverse = True)}

print("Matched", matched, "WORDS")
count = 0
for i in sorted:
	if count % 20 == 0 and count != 0:
		if input("Would you like more? y/n?: ") == "n":
			break
	if a == "y":
		with open(os.path.join(path,'english-words/words_alpha.txt')) as f:
			if i not in f.read():
				continue
	if len(set(i)) >= 7:
		print("-----\nPANGRAM")
	print(i, sorted[i])
	print("-----")
	count += 1
