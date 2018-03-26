import re

class RLEString:
    def __init__(self, mystring):
        if re.match('^[a-zA-Z]+$', mystring):
            self.__mystring = mystring
        else:
            print('error')
        self.__iscompressed = False

    def compress(self):
        print('Compress')

    def decompress(self):
        print('Uncompress')

    def iscompressed(self):
        print('iscompressed')

    def __str__(self):
        return self.__mystring


rle = RLEString(mystring='aaabbbaaabbbaabb')
print(rle)