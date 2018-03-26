# File name: RLE.py
# Author: Tom Are Tørum
# Submission: Assignment 8
import re


class RLEString(object):
    """Run length encoder
    """
    def __init__(self, mystring):
        if re.match('^[a-zA-Z]+$', mystring):   #Regex checks alphabetic characthers only
            self.__mystring = mystring
            self.__iscompressed = False
        else:
            raise Exception('String contains nonalphabetic characters.')

    def compress(self):
        """Compress mystring
        :return: None
        """
        if not self.__iscompressed:
            count = 1
            previouschar = ''
            compressmystring = ''
            for char in self.__mystring:
                if char != previouschar:
                    if previouschar:
                        compressmystring += str(count) + previouschar
                    count = 1
                    previouschar = char
                else:
                    count += 1
            else:
                compressmystring += str(count) + previouschar
            self.__iscompressed = True
            self.__mystring = compressmystring
        else:
            raise Exception('String is already compressed')

    def decompress(self):
        """Decompress mystring
        :return:
        """
        if self.__iscompressed:
            decompressedmystring = ''
            multiplier = ''
            for i in range(0, len(self.__mystring)):
                if self.__mystring[i].isdigit():
                    multiplier += self.__mystring[i]
                else:
                    decompressedmystring += int(multiplier) * self.__mystring[i]
                    multiplier = ''
            self.__mystring = decompressedmystring
            self.__iscompressed = False
        else:
            raise Exception('String is not compressed')

    def iscompressed(self):
        """Return compression status of mystring
        :return bool self.__iscompressed:
        """
        return self.__iscompressed

    def __str__(self):
        """Return string
        :return string self.__mystring:
        """
        return self.__mystring


rle = RLEString(mystring='aaafffgeeesskksssssdfff')
rle.compress()
print(rle.__str__())
rle.decompress()
print(rle.__str__())