#Logic for the Caesar Cipher
import string

def encodeMessage(inputString, cipherKey):
    alphaList = list(string.ascii_lowercase)
    alphaList.append(" ")
    inputList =  list(inputString)
    encodedString = ""
    for char in inputList:
        originalIndex = alphaList.index(char)
        newIndex = cipherKey + originalIndex
        if newIndex > 26:
            newIndex = newIndex - 27
        newChar = alphaList[newIndex]
        encodedString = encodedString + newChar
    return encodedString
    
def decodeMessage(inputString, cipherKey):
    alphaList = list(string.ascii_lowercase)
    alphaList.append(" ")
    inputList = list(inputString)
    decodedString = ""
    for char in inputList:
        originalIndex = alphaList.index(char)
        newIndex = originalIndex - cipherKey
        newChar = alphaList[newIndex]
        decodedString = decodedString + newChar
    return decodedString