#This is the generator py file that will be used to generate the actualy prompts
#The app.py file will create the UI and the rest of the app.

import random
import linecache
from itertools import islice
    
    
def makeGen(reader): #Is used by rawGenCount
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024*1024)

def rawGenCount(filename): #Determines # of lines in file
    f = open(filename, 'rb')
    f_gen = makeGen(f.raw.read)
    return sum( buf.count(b'\n') for buf in f_gen ) 
    
    
def genWord(length): #Generates a word of long, medium, or short length

    if (length=='long'):
        wordList = 'wordlist_long.txt'      
    elif(length=='medium'):
        wordList = 'wordlist_medium.txt'
    elif(length=='short'):
        wordList = 'wordlist_short.txt'
    else:
        wordList='wordlist_medium.txt'
        rnum=99999
        print("Invalid length input! Please check your code (genWord function within Generator.py)!")
    rnum = random.randrange(1,rawGenCount(wordList))
    return linecache.getline(wordList,rnum).rstrip('\n') # grabs word from line and removes \n

def multiGenWord(wc,length): # returns a list of words
    rels = []
    for i in range (wc):
        rels.append([genWord(length)])
    return[rels]
