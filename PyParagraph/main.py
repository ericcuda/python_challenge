#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Filename:  main.py    PyParagraph challenge
# EXTRA ASSIGNMENT
# Used to analyze and show stats for literature submissions
# Eric Staveley   MWSa
# Read in a file and gather info from its paragraph
# Desired output (sample) Adam Wayne snip    :
#Paragraph Analysis
#-----------------
#Approximate Word Count: 122
#Approximate Sentence Count: 5
#Average Letter Count: 4.6
#Average Sentence Length: 24.0

# import the os module...to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Module to introduce Perl-like search and expression capability for strings
import re


# In[11]:


def readfile(myfile):
    totlettercount = 0
    totwordcount = 0
    totsentcount = 0
       
    with open("raw_data/" + myfile) as file_object: 
        lines = file_object.readlines()
        print("The file you chose:")
        for paragraph in lines: 
            print("paragraph:")
            print(paragraph)
            #re.split("(?<=[.!?]) +", paragraph)
            wordlist = re.split(" ", paragraph)    #split on spaces
            #print(wordlist[0])
            #for word in wordlist:
            #    print(word)
            #    print(wordlist.index(word))
            #track the word to index position assignment...since I did not obtain exactly what the Adam Wayne sample showed...
            #I am 2 words off (I show 120 words....but notepad+ and the example say 122)
            #print(word + ":" + str(wordlist.index(word))
            wordcount = len(wordlist)  #word count (REQUIRED)
            totwordcount = totwordcount + wordcount  # to account for possible multiple paragraphs in file
            #print(wordcount)
            #sentencelist = re.split(".!?", paragraph)    #split on .!?
            sentencelist = re.split("(?<=[.!?]) +", paragraph)    # thanks for the hint in the instrs!!
            sentcount = len(sentencelist)
            totsentcount = totsentcount + sentcount

            #to determine average letter count of a word....go thru the word list
            #take a sum of each char in a word and divide by the number of words
            for word in wordlist:
                lettercount = len(word)
                totlettercount = totlettercount + lettercount
            avglettercount = totlettercount / wordcount     # REQUIRED

            #to determine avg sentence length..just divide wordcount by sentencecount
            avgsentencelength = wordcount / sentcount     # REQUIRED


            #print(wordlist)
            #print(paragraph)
            #joe = input("Input something here")

    print("\n#Paragraph Analysis")
    print("#-----------------")
    print(f"#Approximate Word Count: + {totwordcount}")
    print(f"#Approximate Sentence Count:  + {totsentcount}")
    print(f"#Average Letter Count: + {avglettercount}")
    print(f"#Average Sentence Length:  + {avgsentencelength}")
    print("\nFinished!")
         
       


# In[22]:


userinput = input("Select (1) for file paragraph_1.txt or (2) for file paragraph_2.txt or (3) for Adam Wayne snippet for processing..")
if userinput == "1":
    chosenfile = "paragraph_1.txt"
    readfile(chosenfile)
elif userinput == "2":
    chosenfile = "paragraph_2.txt"
    print("Not quite working on ALL the paragraphs at one pop, within this file, yet!")
    readfile(chosenfile)
elif userinput == "3":
    chosenfile = "AdamWayne.txt"
    print("I'm 2 words off in my count. README.md says 122 words and so does Notepad++, I get 120!")
    readfile(chosenfile)
else:
    print("Pease pick a valid number for your file selection.  Please re run the program")
    chosenfile = ""


# In[ ]:




