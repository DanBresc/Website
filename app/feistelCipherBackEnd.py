import binascii
import random
from logicGates import LogicGates as lg
from logicGates import BinaryConversion as bc


def feistel(plainText):
    LG = lg(2)
    BC = bc()
    print("Plain Text: ", plainText)
    bin = BC.plainTextToBinary(plainText)
    print("Converted Binary: ", bin)
    
    
    #Splitting the binary message in two
    n = int(len(bin))//2
    lBin1 = bin[0:n]
    rBin1 = bin[n::]
    m = len(rBin1)
    
    #Creating Keys for two rounds
    K1 = BC.createRandomKey(m);
    K2 = BC.createRandomKey(m);
    
    #Round I:
    f1 = LG.XOR(rBin1,K1)
    rBin2 = LG.XOR(f1,lBin1)
    lBin2 = rBin1
    
    #Round II:
    f2 = LG.XOR(rBin2, K2)
    rBin3 = LG.XOR(f2,lBin2)
    lBin3 = rBin2
    
    #Converting the fully ciphered text:
    encodedBinary = lBin3 + rBin3
    encodedString = ' '
    
    for i in range(0, len(encodedBinary), 7):
        #Grabbing the data in 8 bit chunks
        temp = encodedBinary[i:i+7]  
        encodedDecimal = BC.binaryToDecimal(temp)
        encodedString = encodedString + chr(encodedDecimal)
    print("Encoded String: ",encodedString)
    return[encodedString,K1,K2]
    
def deFeistel(encodedString,K1,K2):
    LG = lg(2)
    BC = bc()
    print("EncodedString: ", encodedString)
    bin = BC.plainTextToBinary(encodedString)
    print("Converted Binary: ", bin)
    
    n = int(len(bin))//2
    lBin1 = bin[0:n]
    rBin1 = bin[n::]

    f1 = LG.XOR(lBin1,K2)
    lBin2 = LG.XOR(rBin1,f1)
    rBin2 = lBin1
    
    f2 = LG.XOR(lBin2,K1)
    lBin3 = LG.XOR(rBin2,f2)
    rBin3 = lBin2
    
    decodedBinary = lBin3 + rBin3
    decodedDecimal = int(decodedBinary,2)
    
    decodedString = binascii.unhexlify('%x'%decodedDecimal)
    print("Decoded String: ", decodedString)
    

if __name__ == "__main__":
    fList = feistel("Daniel Brescia")
    eString = fList[0]
    K1 = fList[1]
    K2 = fList[2]
    deFeistel(eString, K1, K2)
    
    
   
    
  