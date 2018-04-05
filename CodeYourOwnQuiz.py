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
Astley made a comeback in 2007, becoming an ..3.. phenomenon'. His music video
for "Never Gonna Give You Up" became integral to the meme known as ..4.. .
'''

#answers
l1 = {1:'Never', 2:'Single', 3:'Internet', 4:'rickrolling'}

#level 2: Robyn Rihanna Fenty
#text
Rihanna = '''
Rihanna is a Barbadian-born singer, ..1.. and actress. In 2005,
Rihanna rose to fame with the release of her ..2.. studio album Music of the Sun
and its follow-up A Girl like Me (2006). Many of her songs rank among the
worlds best-selling singles of all time, including the single ..3..,
Among numerous awards and accolades, Rihanna has won nine Grammy Awards,
twelve American MusicAwards and twelve ..4..  Music Awards.
'''

#answers
l2 = {1:'songwriter', 2:'debut', 3:'Umbrella', 4:'Billboard'}

#level 3: Madonna Louise Ciccone
#text
Madonna = '''
Madonna is an American singer, songwriter, actress, and ..1.. .
After performing as a ..2.., guitarist and vocalist in the music groups
Breakfast Club and Emmy, Madonna signed with Sire Records in 1982. Her other
ventures include fashion design, writing childrens books, opening of health
clubs, and filmmaking. She also contributed in various charities and founded
the ..3.. organization in 2006. Upon being confirmed in the Catholic Church in
1966, she adopted ..4.. as a confirmation name.
'''

#answers
l3 = {1:'businesswoman', 2:'drummer', 3:'Raising Malawi', 4:'Veronica'}

def game_level():
    ''' *Asks the player to choose a level for the quiz
        *Calls the function fill_in_the_blank with the artist (text with blanks)
        and level (dictionary with answers)'''
    print ('''Welcome to the world of music. In this game you can shine with
    your music knowledge!!!''')
    level = raw_input('''Choose a level easy, medium or hard: ''')
    # get level from user !!!! raw_input !!!
    if level == 'easy':
        print('''You have chosen the easy level, Good luck!''')
        fill_in_the_blank(Rick,l1)
    elif level == 'medium':
        print('''You have chosen the medium level, Try your best!''')
        fill_in_the_blank(Rihanna,l2)
    elif level == 'hard':
        print('''You have chosen the hard level, You need more than luck!''')
        fill_in_the_blank(Madonna,l3)
    else:
        print (''' >>> You did not choose a possible level. Try again! <<<''')
        game_level()

def fill_in_the_blank(artist,level):
    ''' *Prompts the text with blanks
        *asks the user to give the maximum number of wrong answers (integer)
        *loops through the blanks to fill in prompts the text with the blanks
         filled in
        *calls the function nextlevel() or
        *exits quiz when the max number of wrong answers is reached


    '''
    blank_no = 1
    #number of blank to fill in
    blank_max = 4
    #max number of blanks to fill in
    wrong_answer = 1
    #counts wrong answers
    wrong_answer_max = input('''How many tries do you want before the game
     quits? Chose a number 1, 2 or ... : ''')
    #sets the max number of wrong answers from user input
    print(artist)
    while blank_no <= blank_max:
        answer = raw_input('Fill the blank No'+ str(blank_no)+' : ')
        if answer.lower() == (level[blank_no]).lower():
            print(level[blank_no])
            artist = (artist.replace('..'+str(blank_no)+'..',(level[blank_no])))
            print (artist)
            blank_no = blank_no + 1
            wrong_answer = 1
        else:
            if wrong_answer < wrong_answer_max:
                wrong_answer = wrong_answer + 1
                print('Wrong answer. Try again:')
            else:
                print('''Sorry, You have exceeded the max number
                of wrong answers! Good Bye! ''')
                return
    nextlevel()

def nextlevel():
    ''' *asks the player to play again or to exit the quiz: string (yes/else)'''
    print('''
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        Congratulations !!! You know a lot about the artist:
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')
    yes_no = raw_input('Do you want to play again? yes or no: ')
    if yes_no == 'yes':
        game_level()
    else:
        print ('''
        Good Bye!
        ''')
        return

game_level()
