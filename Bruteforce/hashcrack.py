import hashlib
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


words = []


def wordlisting():
    try:
        wordlist = str(input(bcolors.OKBLUE + bcolors.BOLD + 'Enter the name of the wordlist (.txt): '))
        with open(wordlist + '.txt', 'r') as all_wordlist:
            for word in all_wordlist:
                words.append(word.strip())
    except FileNotFoundError:
        print(bcolors.FAIL + "File Not Found! Please check the file name again")
        wordlisting()


def hash_coding():
    hash_code = (str(input(bcolors.OKBLUE+bcolors.BOLD+'Enter the hashcode: '))).lower()
    if len(hash_code) == 64:
        for each in words:
            encoded = each.encode('utf-8')
            hashed = hashlib.sha256(encoded)
            hashed = hashed.hexdigest()
            hashed = hashed
            if hashed == hash_code:
                print(bcolors.HEADER + 'Word Found!')
                print(bcolors.OKBLUE + 'The word is: ' + bcolors.OKGREEN + bcolors.UNDERLINE + '{0}'.format(each))
                break
            else:
                print(bcolors.FAIL + 'Hash didn\'t match')
    else:
        print(bcolors.FAIL+'Required Length didn\'t meet, 64 characters required!')
        hash_coding()


wordlisting()
hash_coding()
