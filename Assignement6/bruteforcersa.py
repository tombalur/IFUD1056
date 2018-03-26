import Assignement6.listingprimes as listingprimes
import Assignement6.rsa as rsa

def findprimefactors(number):
    primes = listingprimes.listprimes(number=publickeyn)
    i = 0
    while 2 * primes[i] <= publickeyn:
        x = 0
        while primes[i] * primes[x] <= publickeyn:
            if primes[i] * primes[x] == publickeyn:
                return primes[i], primes[x]
            x += 1
        i += 1
    return None

ciphertext1 = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
ciphertext2 = [84620]
publickeyn = 100127
publickeye = 29815
#ciphertext1 = [98819, 16103, 79169, 12585, 270, 79169, 12585, 270, 87278, 270, 12585, 78338, 104760, 107919, 78338, 91523, 270, 23500, 78338, 12585, 12585, 87278, 56228, 78338]
#ciphertext2= [98819]
#publickeyn = 121859
#publickeye = 27541
primefactors = findprimefactors(number=publickeyn)
privatekeyn = (primefactors[0]-1)*(primefactors[1]-1)
k = 1
while k <= 1000000:
    privatekeyd = (k*privatekeyn+1)//publickeye
    try:
        message = rsa.decrypt((privatekeyd, publickeyn), ciphertext2)
        if message.lower().startswith('h'):
            print(rsa.decrypt((privatekeyd, publickeyn), ciphertext1))
            print('k =', k)
    except ValueError:
        print('Error')
    k += 1
#print(rsa.decrypt((71965, publickeyn), ciphertext))

#https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA
#k = 19284


