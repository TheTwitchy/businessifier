#!/usr/bin/env python

VERSION="1.0"

import sys
import signal
import re

#Try to import argparse, not available until Python 2.7
try:
    import argparse
except ImportError:
    sys.stderr.write("error: Failed to import argparse module. Needs python 2.7+.")
    quit()

#Define the class used to do pattern matching
#Pretty much just used to keep patterns and anti-patterns matched (see configfile for explanation)
class BfrPattern:
    pattern = ""
    antipattern = ""
    
    def __init__(self, pattern, antipattern=""):
        self.pattern = pattern
        self.antipattern = antipattern


def signalHandler(signal, frame):
    print ""
    quit()

#Import the list of regexes to use against the wordlist
def importConfig(configFd):
    results = []
    
    #Walk the config file, ignore any lines that start with '#' or are empty, and return them all as a list
    for line in configFd.readlines():
        line = line.strip()
        if line == "" or line[0] == "#":
            pass
        else:
            #Look for a '~' in the config item to see if there is a related anti-pattern
            if "~" in line:
                results.append(BfrPattern(line.split("~")[0], antipattern=line.split("~")[1]))
            else:
                results.append(BfrPattern(line))
    return results

def main():
    #Signal handler to catch CTRL-C (quit immediately)
    signal.signal(signal.SIGINT, signalHandler)
    
    #Setup the argparser and all args
    parser = argparse.ArgumentParser(prog="businessifier", description="Businessify wordlists by removing inapproprate content", epilog="Written by TheTwitchy. For more information, see https://github.com/TheTwitchy/businessifier")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s "+VERSION)
    parser.add_argument("-c", "--configfile", help="override the default config file", type=argparse.FileType("r"), default="businessifier.conf")
    parser.add_argument("-i", "--input", help="input filename, defaults to stdin", type=argparse.FileType("r"), default="-")
    parser.add_argument("-o", "--output", help="output filename, defaults to default.bfr_out", type=argparse.FileType("w"), default="default.bfr_out")
    args = parser.parse_args()
    
    #Send the config file to be parsed to get a list of regexes to run.
    bfrPatterns = importConfig(args.configfile)
    
    #Import the wordlist from input
    wordlist = args.input.readlines()
    for i in range(0, len(wordlist)):
        wordlist[i] = wordlist[i].strip()
    
    #Init an empty list to hold any removed words for later review
    removedWords = []
    
    for pattern in bfrPatterns:
        for word in wordlist:
            result = re.search(pattern.pattern, word, re.M|re.I)
            if result:
                #A pattern matched. If there is an antipattern, check against that. If not, add it to the removed list.
                if not pattern.antipattern == "":
                    result = re.search(pattern.antipattern, word, re.M|re.I)
                    if not result:
                        removedWords.append(word)
                        #print "debug: " + pattern.pattern + " caused removal of " + word
                else:
                    removedWords.append(word)
                    #print "debug: " + pattern.pattern + " caused removal of " + word
    
    #Remove all flagged words from the full list and output any that pass to the outputfile
    for word in wordlist:
        removed = False
        
        #This could probably be improved to if word in removedWords, but it's late and I want to commit this.
        for removedWord in removedWords:
            if removedWord == word:
                removed = True
                break
        if not removed:
            args.output.write(word+"\n")
        removed = False
    

    #Show a list of removed words so they can be manually checked
    print "The following words have been removed from the wordlist:"
    for word in removedWords:
        print " " + word
    print "\nIf you see a mistake, please open a new issue at\nhttps://github.com/TheTwitchy/businessifier\nand include the word and wordlist source."

if __name__ == "__main__":
    main()
