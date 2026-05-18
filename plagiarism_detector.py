def load_essay(filename):
    with open(filename, "r") as f:
        text = f.read()
    return set(text.lower().split())

words1 = load_essay("lab2_plagiarism/essay-1.txt")
words2 = load_essay("lab2_plagiarism/essay-2.txt")

print("Essay 1 loaded:", len(words1), "unique words")
print("Essay 2 loaded:", len(words2), "unique words")

def check_plagiarism(words1, words2):
    common = words1 & words2
    total = words1 | words2
    percentage = (len(common) / len(total)) * 100

    print("Common words:", len(common))
    print("Total unique words:", len(total))
    print("Plagiarism: " + str(round(percentage, 2)) + "%")

    if percentage >= 50:
        print("Verdict: PLAGIARISM DETECTED!")
    else:
        print("Verdict: No plagiarism found.")

check_plagiarism(words1, words2)

def show_common_words(words1, words2):
    common = words1 & words2
    print("\nCommon words found:")
    for word in common:
        print("- " + word)

show_common_words(words1, words2)

def search_word(filename, word):
    with open(filename, "r") as f:
        text = f.read().lower()
    
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count

search = input("Enter a word to search: ").lower()

count1 = search_word("lab2_plagiarism/essay-1.txt", search)
count2 = search_word("lab2_plagiarism/essay-2.txt", search)

if count1 == 0 and count2 == 0:
    print(False)
else:
    print("Essay 1: " + str(count1) + " times")
    print("Essay 2: " + str(count2) + " times")