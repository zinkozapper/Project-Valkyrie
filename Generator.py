#This is the generator py file that will be used to generate the actualy prompts
#The app.py file will create the UI and the rest of the app.

import random
import linecache
from pathlib import Path


localPath = Path(__file__).absolute().parent

    
def makeGen(reader): #Is used by rawGenCount
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024*1024)

def rawGenCount(filename): #Determines # of lines in file
    f = open(filename, 'rb')
    f_gen = makeGen(f.raw.read)
    return sum( buf.count(b'\n') for buf in f_gen ) 
    
    
def genWord(length = 'Custom', wordList = localPath/'wordlist_long.txt'): #Generates a word of long, medium, or short length
    
    if (length=='long'):
        wordList = localPath/'wordlist_long.txt'     
    if(length=='medium'):
        wordList = localPath/'wordlist_medium.txt'
    elif(length=='short'):
        wordList = localPath/'wordlist_short.txt'
    elif(length=='Custom'):
        pass
     
    rnum = random.randrange(1,rawGenCount(wordList))
    return linecache.getline(str(wordList),rnum).rstrip('\n') # grabs word from line and removes \n

def multiGenWord(wc,length): # returns a list of words
    rels = []
    for i in range (wc):
        rels.append([genWord(length)])
    return[rels]

