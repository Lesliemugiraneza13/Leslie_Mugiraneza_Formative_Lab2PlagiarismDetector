# Plagiarism Detector
### By Leslie Mugiraneza

---

## What This Project Does

This program compares two essays and determines whether one has been plagiarized from the other. It does this by analyzing the words in both essays, finding what they have in common, and calculating a plagiarism percentage using set operations.

---

## How to Run It

1. Make sure Python is installed on your computer
2. Place your two essay files in the same folder as the program
3. Name them exactly: `essay-1.txt` and `essay-2.txt`
4. Open a terminal in that folder
5. Run the program:
```
python plagiarism_detector.py
```
6. When prompted, type a word to search for in both essays

---

## How the Code Works — Line by Line

---

### Setting Up File Paths

```python
FILE1 = "lab2_plagiarism/essay-1.txt"
FILE2 = "lab2_plagiarism/essay-2.txt"
```

These two lines store the file paths as variables. This means if the file location ever changes, you only need to update it in one place instead of hunting through the whole code.

---

### Function 1: load_essay(filename)

```python
def load_essay(filename):
    with open(filename, "r") as f:
        text = f.read()
    return set(text.lower().split())
```

**What it does:** Opens an essay file and converts it into a set of unique words.

**Line by line:**
- `with open(filename, "r") as f:` — Opens the file in read mode. The `with` statement automatically closes the file when done, even if an error occurs.
- `text = f.read()` — Reads the entire content of the file into a variable called text.
- `text.lower()` — Converts all text to lowercase so that "The" and "the" are treated as the same word.
- `.split()` — Splits the text into individual words by spaces.
- `set(...)` — Converts the list of words into a set, which automatically removes all duplicate words.

**Why use a set here?** Because for plagiarism detection we only care whether a word EXISTS in both essays, not how many times it appears. Sets are perfect for this because they store only unique values and support powerful comparison operations like intersection and union.

---

### Function 2: check_plagiarism(words1, words2)

```python
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
```

**What it does:** Calculates the plagiarism percentage and gives a verdict.

**Line by line:**
- `common = words1 & words2` — Uses the set intersection operator `&` to find words that appear in BOTH essays.
- `total = words1 | words2` — Uses the set union operator `|` to find ALL unique words across both essays.
- `percentage = (len(common) / len(total)) * 100` — Applies the plagiarism formula: divide common words by total unique words, then multiply by 100 to get a percentage.
- `round(percentage, 2)` — Rounds the percentage to 2 decimal places so it looks clean when printed.
- `str(...)` — Converts the number to a string so it can be joined with other text for printing.
- `if percentage >= 50:` — If 50% or more of the words are shared, the program flags it as plagiarism. This threshold is based on the lab requirements.

**The plagiarism formula:**
```
Plagiarism% = (Number of common words / Total unique words) x 100
```

---

### Function 3: show_common_words(words1, words2)

```python
def show_common_words(words1, words2):
    common = words1 & words2
    print("\nCommon words found:")
    for word in common:
        print("- " + word)
```

**What it does:** Displays every word that appears in both essays.

**Line by line:**
- `common = words1 & words2` — Gets the intersection of both sets again.
- `\n` inside the print — Adds a blank line before the heading for better readability.
- `for word in common:` — Loops through every word in the common set.
- `print("- " + word)` — Prints each word with a dash in front for formatting.

**Note:** Because sets are unordered, the words will not appear in alphabetical order. This is normal behavior for sets in Python.

---

### Function 4: search_word(filename, word)

```python
def search_word(filename, word):
    with open(filename, "r") as f:
        text = f.read().lower()
    
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count
```

**What it does:** Counts how many times a specific word appears in a given essay.

**Line by line:**
- `f.read().lower()` — Reads the file and converts everything to lowercase so the search is case insensitive. Searching for "The" and "the" will give the same result.
- `words = text.split()` — Splits the text into a list of individual words. This time we use a LIST not a set, because we need to count duplicates.
- `count = 0` — Sets a counter starting at zero.
- `for w in words:` — Loops through every word in the essay.
- `if w == word: count += 1` — Every time the word matches, increase the counter by 1.
- `return count` — Returns the final count after checking all words.

**Why use a list here instead of a set?** Because a set removes duplicates. If the word "the" appears 20 times in the essay, a set would only keep one copy and the count would always be 1. A list keeps all copies, so the count is accurate.

---

### Calling the Search and Displaying Results

```python
search = input("Enter a word to search: ").lower()

count1 = search_word(FILE1, search)
count2 = search_word(FILE2, search)

if count1 == 0 and count2 == 0:
    print(False)
else:
    print("Essay 1: " + str(count1) + " times")
    print("Essay 2: " + str(count2) + " times")
```

**Line by line:**
- `input(...)` — Asks the user to type a word.
- `.lower()` — Converts the input to lowercase so it matches the lowercased text in the essays.
- `count1` and `count2` — Store how many times the word appears in each essay.
- `if count1 == 0 and count2 == 0:` — If the word is not found in either essay, print False as required by the lab.
- Otherwise, print how many times the word appears in each essay.

---

## Common Errors and How to Fix Them

**FileNotFoundError**
```
FileNotFoundError: [Errno 2] No such file or directory: 'essay-1.txt'
```
This means the essay files are not in the same folder as the program. Make sure `essay-1.txt` and `essay-2.txt` are in the same location as `plagiarism_detector.py`.

---

**ZeroDivisionError**
```
ZeroDivisionError: division by zero
```
This happens if both essay files are completely empty. Make sure your essays have actual content in them.

---

**Wrong count when searching**
If your search is returning 0 when you expect a result, make sure you are typing the word in lowercase. The program converts everything to lowercase, so searching for "Python" will not match but "python" will.

---

## Things to Know

- The program is case insensitive — "Hello" and "hello" are treated as the same word.
- Punctuation attached to words may affect results. For example "hello," and "hello" are treated as different words.
- Sets are unordered, so common words will not appear in any particular order.
- The 50% threshold for plagiarism detection is based on the lab requirements and can be adjusted in the code.

---

## To Anyone Using This Program

I hope this plagiarism detector is useful to you. This was built as part of a Python programming course at African Leadership University. It uses core Python concepts including file handling, sets, loops, functions, and string operations.

If you have any questions about how the code works or want to improve it, feel free to reach out.

Good luck and write your own work! 🎯
