

__all__ = ["LogicGates","BinaryConversion"]

import random
import binascii

class LogicGates:
    """
    6/9/2020
    Daniel Brescia

    This module allows the user to input binary strings into standard logic gates.

    x & y should be the inputs that are binary strings 
    ex:
        "01001010"

    Methods are capitalized to avoid interference with Python Standard Keywords.
    """
    def __init__(self):
        pass
        
    #Helperfunctions for Gates and Binary Conversion Methods
    def equateLengths(self,x,y):
        """
        Takes in 2 binary strings x & y. 
        Inserts "0"'s @ the beginnning until the strings are of equal lenght.
        Returns a list of two binary strings [x,y].
        """
        if self.validateBinary(x) and self.validateBinary(y):
            while len(x) > len(y):
                y = "0" + y
            while len(y) > len(x):
                x = "0" + x
            return [x,y]
        else:
            print("Only enter binary strings")
    
        
    #Gates
    def AND(self,x,y):
        """
        Takes in two binary strings.
        Returns a third binary string according to AND logic.
        """
        if self.validateBinary(x) and self.validateBinary(y):
            andLogic = ""
            equatedBinaries = self.equateLengths(x,y)
            x = equatedBinaries[0]
            y = equatedBinaries[1]
            binaryLength = len(x)  
            for bit in range(binaryLength):
                if x[bit] == y[bit] and x[bit] == "1":
                    andLogic += "1"
                else:
                    andLogic += "0"
            return andLogic
        else:
            print("Only enter binary strings")
    
    def OR(self,x,y):
        """
        Takes in two binary strings.
        Returns a third binary string according to OR logic.
        """
        
        orLogic = ""
        equatedBinaries = self.equateLengths(x,y)
        x = equatedBinaries[0]
        y = equatedBinaries[1]
        binaryLength = len(x)  
        for bit in range(binaryLength):
            if x[bit] == "1" or y[bit] == "1":
                orLogic += "1"
            else:
                orLogic += "0"
        return orLogic
    
    def XOR(self,x,y):
        """
        Takes in two binary strings.
        Returns a third binary string according to XOR logic.
        """
        xOrLogic = ""
        equatedBinaries = self.equateLengths(x,y)
        x = equatedBinaries[0]
        y = equatedBinaries[1]
        binaryLength = len(x)  
        for bit in range(binaryLength):
            if x[bit] == y[bit]:
                xOrLogic += "0"
            else:
                xOrLogic += "1"
        return xOrLogic
    
    def NAND(self,x,y):
        """
        Takes in two binary strings.
        Returns a third binary string according to NAND logic.
        """
        nAndLogic = ""
        equatedBinaries = self.equateLengths(x,y)
        x = equatedBinaries[0]
        y = equatedBinaries[1]
        binaryLength = len(x)  
        
        for bit in range(binaryLength):
            if x[bit] == y[bit] and x[bit] == "1":
                nAndLogic += "0"
            else:
                nAndLogic += "1"
        return nAndLogic
    
    def XNOR(self,x,y):
        """
        Takes in two binary strings.
        Returns a third binary string according to XNOR logic.
        """
        xNorLogic = ""
        equatedBinaries = self.equateLengths(x,y)
        x = equatedBinaries[0]
        y = equatedBinaries[1]
        binaryLength = len(x)  
        
        for bit in range(binaryLength):
            if x[bit] == y[bit]:
                xNorLogic += "1"
            else:
                xNorLogic += "0"
        return xNorLogic
    
    def NOT(self,x):
        """
        Takes in one binary string.
        Returns a second binary string according to NOT logic.
        """

        notLogic = ""
        binaryLength = len(x)
        
        for bit in range(binaryLength):
            if x[bit] == "1":
                notLogic += "0"
            else:
                notLogic += "1"
        return notLogic
        
    def NOR(self,x,y):
        """
        Takes in two binary strings.
        Returns a third binary string according to NOR logic.
        """
    
        nOrLogic = ""
        equatedBinaries = self.equateLengths(x,y)
        x = equatedBinaries[0]
        y = equatedBinaries[1]
        binaryLength = len(x)  
        
        for bit in range(binaryLength):
            if x[bit] == "1" or y[bit] == "1":
                nOrLogic += "0"
            else:
                nOrLogic += "1"
        return nOrLogic
        
    def validateBinary(self,x):
        """
        Takes in a string to be evaluated.
        If the string only contains 1's and 0's and is thus a true binary the function will return True
        Otherwise it returns false
        """
        for bit in x:
            if bit == "1" or bit == "0":
                pass;
            else:
                return False
        return True
        
        
        
class BinaryConversion:
    def __init__(self):
        pass
    def binaryToDecimal(self,binary):
        """
        Takes a binary string, and returns a decimal number.
        """
        decimal = int(binary,2)
        return decimal
    
    def plainTextToBinary(self,plainText):
        """
        Takes a string of regular text, and converts it into a binary string
        """
        PT = plainText
        PTAscii = [ord(x) for x in PT]
        PTBinary = [format(y,'08b') for y in PTAscii]
        PTBinary = "".join(PTBinary)
        return PTBinary
    
    def createRandomKey(self,bit):
        """
        Creates a random binary key string of specified length
        """
        key = ""
        bit = int(bit)
        for binary in range(bit):
            newBinary = random.randint(0,1)
            newBinary = str(newBinary)
            key = key + newBinary
        return key
    