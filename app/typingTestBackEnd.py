
import time
phrase = "The quick brown fox jumps over the lazy dog."

phraseList = phrase.split(" ")
numWords = len(phraseList)

t0 = float(time.time())
print(phrase)
attempt = input("Type the phrase as fast as you can: \n")
print(type(attempt))
attemptList = attempt.split(" ")
t1 = float(time.time())

mistakes = 0
for i in range(len(phraseList)):
    try: 
        if attemptList[i] != phraseList[i]:
            mistakes = mistakes + 1
    except:
        print("Index out of range")




print("\n\nStatistics:")
print("Mistakes: %d" %mistakes)
timeElapsed= t1-t0
timeElapsedMin = (t1-t0) / 60
print("Number of Words: %d" %numWords)
print("Time Elapsed: %f Minutes"%timeElapsedMin)
print("Time Elapsed: %f Seconds"%timeElapsed)
WPM =numWords / timeElapsedMin
print("WPM: %f)"%WPM)
