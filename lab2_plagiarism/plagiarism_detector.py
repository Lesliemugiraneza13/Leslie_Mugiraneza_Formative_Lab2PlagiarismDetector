import string

def load_essay(filename):
    with open(filename, "r") as f:
        text = f.read()
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return set(text.split())

def load_essay_list(filename):
    with open(filename, "r") as f:
        text = f.read()
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

words1 = load_essay("essay-1.txt")
words2 = load_essay("essay-2.txt")

words1_list = load_essay_list("essay-1.txt")
words2_list = load_essay_list("essay-2.txt")

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

def show_common_words(words1, words2, words1_list, words2_list):
    common = words1 & words2
    print("\nCommon words found:")
    for word in sorted(common):
        count1 = words1_list.count(word)
        count2 = words2_list.count(word)
        print("- " + word + " → Essay 1: " + str(count1) + " times | Essay 2: " + str(count2) + " times")

show_common_words(words1, words2, words1_list, words2_list)

def search_word(filename, word):
    with open(filename, "r") as f:
        text = f.read().lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count

search = input("\nEnter a word to search: ").lower().strip()

if not search:
    print("Please enter a word to search.")
else:
    count1 = search_word("essay-1.txt", search)
    count2 = search_word("essay-2.txt", search)

    if count1 == 0 or count2 == 0:
        print(False)
    else:
        print("Essay 1: " + str(count1) + " times")
        print("Essay 2: " + str(count2) + " times")