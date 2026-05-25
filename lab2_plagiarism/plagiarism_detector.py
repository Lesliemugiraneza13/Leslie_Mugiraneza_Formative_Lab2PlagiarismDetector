# Import the string module to access punctuation characters for text cleaning
import string

# Function to load an essay as a set of unique words (used for set operations like intersection and union)
def load_essay(filename):
    # Open the file in read mode
    with open(filename, "r") as f:
        text = f.read()
    # Convert all text to lowercase so comparisons are case-insensitive
    text = text.lower()
    # Remove all punctuation so words like "engineering." and "engineering" are treated the same
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Split into words and return as a set to remove duplicates
    return set(text.split())

# Function to load an essay as a list of all words including duplicates (used for counting occurrences)
def load_essay_list(filename):
    # Open the file in read mode
    with open(filename, "r") as f:
        text = f.read()
    # Convert to lowercase for consistent comparison
    text = text.lower()
    # Remove punctuation characters from the text
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Split into a list and return — duplicates are kept so we can count how many times a word appears
    return text.split()

# Load both essays as sets for plagiarism detection
words1 = load_essay("essay-1.txt")
words2 = load_essay("essay-2.txt")

# Load both essays as lists for word frequency counting
words1_list = load_essay_list("essay-1.txt")
words2_list = load_essay_list("essay-2.txt")

# Display how many unique words were found in each essay
print("Essay 1 loaded:", len(words1), "unique words")
print("Essay 2 loaded:", len(words2), "unique words")

# Function to calculate and display the plagiarism percentage using set operations
def check_plagiarism(words1, words2):
    # Find words that appear in both essays using set intersection
    common = words1 & words2
    # Find all unique words across both essays using set union
    total = words1 | words2
    # Calculate plagiarism percentage: (common words / total unique words) * 100
    percentage = (len(common) / len(total)) * 100

    # Display the results
    print("Common words:", len(common))
    print("Total unique words:", len(total))
    print("Plagiarism: " + str(round(percentage, 2)) + "%")

    # If 50% or more words are shared, flag it as plagiarism
    if percentage >= 50:
        print("Verdict: PLAGIARISM DETECTED!")
    else:
        print("Verdict: No plagiarism found.")

# Run the plagiarism check on both essays
check_plagiarism(words1, words2)

# Function to display all common words and how many times each appears in each essay
def show_common_words(words1, words2, words1_list, words2_list):
    # Get the intersection of both sets to find shared words
    common = words1 & words2
    print("\nCommon words found:")
    # Loop through common words in alphabetical order for readability
    for word in sorted(common):
        # Count how many times the word appears in each essay list
        count1 = words1_list.count(word)
        count2 = words2_list.count(word)
        print("- " + word + " → Essay 1: " + str(count1) + " times | Essay 2: " + str(count2) + " times")

# Display all common words with their counts
show_common_words(words1, words2, words1_list, words2_list)

# Function to search for a specific word in an essay file and return how many times it appears
def search_word(filename, word):
    # Open and read the file, converting to lowercase immediately
    with open(filename, "r") as f:
        text = f.read().lower()
    # Remove punctuation so the search matches correctly
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Split into a list of individual words
    words = text.split()
    # Start a counter at zero
    count = 0
    # Loop through every word and increment the counter when a match is found
    for w in words:
        if w == word:
            count += 1
    return count

# Prompt the user to enter a word to search, converting to lowercase and removing extra spaces
search = input("\nEnter a word to search: ").lower().strip()

# Validate that the user actually typed something
if not search:
    print("Please enter a word to search.")
else:
    # Search for the word in both essays
    count1 = search_word("essay-1.txt", search)
    count2 = search_word("essay-2.txt", search)

    # If the word is not found in either essay, return False as required
    if count1 == 0 or count2 == 0:
        print(False)
    else:
        # Display how many times the word appears in each essay
        print("Essay 1: " + str(count1) + " times")
        print("Essay 2: " + str(count2) + " times")