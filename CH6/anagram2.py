def are_anagrams(word1, word2):
    """Return True, if words are anagrams. """
    #2. Sort the characters in the words
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    #3. Check that the sorted words are identical
    return word1_sorted == word2_sorted

print("Anagram Test")

#1. Input two words. checking for error now
valid_input_bool = False
while not valid_input_bool:
    try:
        two_words = input("Enter two space separated words: ")
        word1, word2 = two_words.split()    #split the input string of words
        valid_input_bool = True
    except ValueError:
        print("BAd Input")

if are_anagrams(word1, word2):
    print("The words {} are anagrams.".format(word1, word2))
else:
    print("The words {} are not anagrams.".format(word1, word2))
