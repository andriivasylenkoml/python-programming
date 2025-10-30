word = input("Enter word: ").lower()

repeated_letters = {ch for ch in word if word.count(ch) > 1}

if repeated_letters:
    print("Same letters in the word:" , ", ".join(sorted(repeated_letters)))
else:
    print("There are no identical letters in the word")