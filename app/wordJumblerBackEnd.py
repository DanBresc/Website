#This will provide the logic for the word jumbler app in order to better organize and keep routes.py neat and readable.
import time
import random
import string

def load_words():
        with open('app\\english-words\\english-words\\words_alpha.txt') as word_file:
            valid_words = set(word_file.read().split())

        return valid_words

def jumbleWords(jWord):
    newWord = ""
        
    intList = []
    newWordList = []
    
    
    english_words = load_words()
    
    length = len(jWord)
    
    timeAllowed = length**2 + 10
    
    print("TIME ALLOWED: %d" %timeAllowed)
    
    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        if elapsed_time > timeAllowed:
            break
        
        word = list(jWord)
        num = len(word)
        for letter in range(len(word)):                
            rInt = random.randint(0,(len(word)-1))
            while rInt in intList:
                rInt = random.randint(0,(len(word)-1))
            intList.append(rInt)
            newWord = newWord + word[rInt]
        
        if newWord in english_words and newWord not in newWordList:        
            newWordList.append(newWord)
        
        intList = []
        newWord = ""
    print(newWordList)
    return newWordList
        
