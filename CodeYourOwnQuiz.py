'''Music Quiz:
all questions are derived from Wikipedia:

Wikipedia contributors. (2018, March 13). Rick Astley. In Wikipedia,
The Free Encyclopedia. Retrieved 14:47, March 27, 2018, from
https://en.wikipedia.org/w/index.php?title=Rick_Astley&oldid=830205124

Wikipedia contributors. (2018, March 29). Rihanna. In Wikipedia,
The Free Encyclopedia. Retrieved 17:44, March 29, 2018, from
https://en.wikipedia.org/w/index.php?title=Rihanna&oldid=833024608

Wikipedia contributors. (2018, March 27). Madonna (entertainer). In Wikipedia,
The Free Encyclopedia. Retrieved 18:00, March 29, 2018, from
https://en.wikipedia.org/w/index.php?title=Madonna_(entertainer)&oldid=832678186
'''

#level 1: Richard Paul Astley
#text
Rick = '''
Rick Astleys 1987 song ..1.. Gonna Give You Up was a No. 1 hit single
in 25 countries. The song won the 1988 Brit Award for Best British ..2.. .
Astley made a comeback in 2007, becoming an ..3.. phenomenon'.
His music video for "Never Gonna Give You Up" became
integral to the meme known as ..4.. .
'''

#answers
level1_answer = ['Never', 'Single', 'Internet', 'rickrolling']

#level 2: Robyn Rihanna Fenty
#text
Rihanna = '''
Rihanna is a Barbadian-born singer, ..1.. and actress. In 2005,
Rihanna rose to fame with the release of her ..2.. studio album
Music of the Sunand its follow-up A Girl like Me (2006).
Many of her songs rank among the worlds best-selling singles of all time,
including the single ..3.. . Among numerous awards and accolades,
Rihanna has won nine Grammy Awards, twelve American Music Awards and
twelve ..4..  Music Awards.
'''

#answers
level2_answer = ['songwriter', 'debut', 'Umbrella', 'Billboard']

#level 3: Madonna Louise Ciccone
#text
Madonna = '''
Madonna is an American singer, songwriter, actress, and ..1.. .
After performing as a ..2.., guitarist and vocalist in the music groups
Breakfast Club and Emmy, Madonna signed with Sire Records in 1982.
Her other ventures include fashion design, writing childrens books,
opening of health clubs, and filmmaking. She also contributed in various
charities and founded the ..3.. organization in 2006. Upon being confirmed
in the Catholic Church in 1966, she adopted ..4.. as a confirmation name.
'''

#answers
level3_answer = ['businesswoman', 'drummer', 'Raising Malawi', 'Veronica']

wrong_answer_max = ''
#The maximum of wrong answers per blank set by player (global variable)
level = ''
#Game level easy, medium or hard choosen by player (global variable)

def start():
    ''' *prompts the user to choose the maximum number of wrong answers per blank
        to fill and to choose a game level
        *values are stored in global variables for later use'''
    print ('''
    ************************************************************
    Welcome to the world of music. Before we start please answer
            the following questions:''')
    wrong_answer_max = input('''
    How many tries do you want before the game quits?
             Chose a number 1, 2 or ... : ''')
    # get maximal number of tries from player as integer
    level = raw_input('''
    Choose a level easy, medium or hard: ''')
    # get level from user !!!! raw_input in python 2.7 !!!
    game_level(wrong_answer_max, level)

def game_level(wrong_answer_max, level):
    ''' *Calls the text with blanks and the list of answers according to the
        level choosen by playerself.
        *Input: wrong_answer_max and level'''
    if level == 'easy':
        print('''
        You have chosen the easy level, Good luck!''')
        fill_in_the_blank(Rick, level1_answer, wrong_answer_max)
    elif level == 'medium':
        print('''
        You have chosen the medium level, Try your best!''')
        fill_in_the_blank(Rihanna, level2_answer, wrong_answer_max)
    elif level == 'hard':
        print('''
        You have chosen the hard level, You need more than luck!''')
        fill_in_the_blank(Madonna,level3_answer, wrong_answer_max)
    else:
        print ('''
        >>> You did not choose a possible level. Try again! <<<''')
        start()

def fill_in_the_blank(artist, level, wrong_answer_max):
    ''' *Prompts the text with blanks
        *loops through the blanks to fill in  and prompts the text again
        with the blank replaced by the right answer
        *exits quiz when the max number of wrong answers is reached
        *Inputs: artist, level and wrong_answer_max
    '''
    wrong_answer = 1
    #counts wrong answers
    print(artist)
    index = 1
    for i in (level):
        answer = raw_input('Fill the blank No'+ str(index)+' : ')
        if answer.lower() == (i).lower():
            artist = (artist.replace('..'+str(index)+'..',(level[int(index)-1])))
            index = index + 1
            print (artist)
            wrong_answer = 1
        elif wrong_answer < wrong_answer_max:
                wrong_answer = wrong_answer + 1
                print('Wrong answer. Try again:')
        elif wrong_answer == wrong_answer_max:
                print('Sorry, You have too many wrong answers! Good Bye! ')
                return
    nextlevel()

def nextlevel():
    ''' *asks the player to play again or to exit the quiz: string (yes/else)'''
    print('''
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        Congratulations !!! You know a lot about the artist:
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')
    yes_no = raw_input('Do you want to play again? yes or no: ')
    if yes_no == 'yes' or yes_no == 'y':
        start()
    else:
        print ('''
        Good Bye!
        ''')
        return

start()
