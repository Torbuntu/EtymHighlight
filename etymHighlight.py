# Etymology highlighter
# Sorensen, Tor
# /5/17

# import scraping technology
from lxml import html
import requests

# obligatory I didn't do it warning.
print("WARNING: This software only attempts to find the French origin on words. It is prone to fail due to the difficulties of scraping from etymonline.com. An update in the future will fix this. But until then, take all results with a grain (or spoon) of salt.")

# useful variables



# Game loop function!
def mainFunction():
    x = True
    contains = False
    count = 0


    #Instructions
    print("type 'Exit' to quit.")

    lang = input("Which language would you like to use for origin?: ")

    
    while(x):

        # Grab users input, Exit on capital E exit.
        phrase = input("Enter word or phrase to check for "+lang+": ")
        if(phrase == "Exit"):
            x = False
            break
            

        # Split phrase for testing individual words.
        phrase = [str(x) for x in phrase.split()]
        for j in range(0, len(phrase)):

            # grab etymology from etymonline.com parse content to checker variable
            page = requests.get('http://www.etymonline.com/index.php?term=' + phrase[j])
            tree = html.fromstring(page.content)
            checker = tree.xpath('//dd[@class="highlight"][position()<3]/text()')

            # If anything in the checker gets a hit on Middle or Old French, true!
            for i in range(0,len(checker)):
                if(('Old '+lang) in checker[i] or ('Middle '+lang) in checker[i]):
                    contains = True
                    break
                else:
                    contains = False

            
            # Output the French origin words.
            if(contains):
                print(lang+" origin: "+ phrase[j])
                count = count + 1

         
        # Finish up with results.
        print("You used " + str(count) +" "+ lang+" words in that phrase")
        count = 0
##########################################################
mainFunction()
