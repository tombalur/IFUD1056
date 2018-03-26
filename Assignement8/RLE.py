import re

class RLEString(object):
    def __init__(self, mystring):
        if re.match('^[a-zA-Z]+$', mystring):
            self.__mystring = mystring
            self.__iscompressed = False
        else:
            raise Exception('String contains nonalphabetic characters.')

    def compress(self):
        if not self.__iscompressed:
            count = 1
            previouschar = ''
            encodedmystring = ''
            for char in self.__mystring:
                if char != previouschar:
                    if previouschar:
                        encodedmystring += str(count) + previouschar
                    count = 1
                    previouschar = char
                else:
                    count += 1
            else:
                encodedmystring += str(count) + previouschar
            self.__iscompressed = True
            self.__mystring = encodedmystring
        else:
            raise Exception('String is already compressed')


    def decompress(self):
        if self.__iscompressed:
            decompressedmystring = ''
            for i in range(0, len(self.__mystring), 2):
                decompressedmystring += int(self.__mystring[i]) * self.__mystring[i + 1]
            self.__mystring = decompressedmystring
            self.__iscompressed = False
        else:
            raise Exception('String is not compressed')


    def iscompressed(self):
        return self.__iscompressed

    def __str__(self):
        return self.__mystring


#rle = RLEString(mystring='aaabbbaaabbbaabb')
#rle.compress()
#print(rle.__str__())
#rle.decompress()
#print(rle.__str__())