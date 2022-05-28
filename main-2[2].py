# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


#a program that checks if two words or phrases are anagrams.
def find_anagrams(word,anagram):
    word_letters="" #a variable to store letters of the 1st word string
    anagram_letters="" #a variable to store letters of 2nd word string
    for i in word.lower():
        if i.isalpha(): #to check if the 1st word string elements are letters
            word_letters+=i 
    for j in anagram.lower():#to check if the 2nd word string elements are letters
        if j.isalpha():
            anagram_letters+=j
    if sorted(anagram_letters)==sorted(word_letters): #compares both strings letters in alphabetical order
        return True
    else:
        return False

print(find_anagrams("A gentleman","Elegant Man"))

print(find_anagrams("Santa","fanta"))

print(find_anagrams("Racecar","Car Race!"))



    

